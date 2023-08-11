import asyncio
from typing import Any
from typing import Dict
from typing import Optional
from typing import Tuple

OPERATION_TRACKERS = {}


async def handle_operation(hub, ctx, rerun_data, resource_type: str) -> Dict[str, Any]:
    result = {
        "comment": [],
        "result": True,
        "rerun_data": None,
        "resource_id": None,
    }

    operation_id = rerun_data.get("operation_id")

    if operation_id is None:
        result["result"] = False
        result["comment"].append("Operation ID is not supplied")
        result["rerun_data"] = {"has_error": True}
        return result

    finished, response = await hub.tool.azure.operation_utils.check_operation_result(
        ctx,
        operation_id=operation_id,
        operation_headers=rerun_data.get("operation_headers"),
        resource_url=rerun_data.get("resource_url"),
    )

    if not finished:
        # Operation still hasn't finished -> reconcile.
        result["rerun_data"] = rerun_data
        return result

    if not response["result"]:
        operation_status = int(response["status"])
        if operation_status == 404:
            # ResourceNotFound
            result["comment"].append(response["comment"])
            return result
        elif operation_status >= 400:
            result["result"] = False
            if "error" in response.get("ret"):
                result["comment"].append(str(response["ret"]["error"]))
            result["rerun_data"] = {"has_error": True}
            return result

    resource_raw = response["ret"]
    if not resource_raw:
        result["rerun_data"] = rerun_data
        result["comment"].append(response["comment"])
        return result

    result["resource_id"] = resource_raw.get("id")
    return result


async def await_operation(hub, ctx, operation_headers, resource_url) -> Dict[str, Any]:
    """
    Awaits a long-running asynchronous Azure operation to complete. Performs an additional GET request when operation completes to fetch the resulting Azure resource.
    :param operation_headers: Headers from initial HTTP response from Azure API call which initiated the operation
    :param resource_url: Azure API URL, used to GET the resource produced by the operation
    """
    poller = OperationPoller(hub, ctx, operation_headers, resource_url)
    return await poller.await_operation()


async def check_operation_result(
    hub, ctx, operation_id, operation_headers, resource_url
) -> Tuple[bool, Dict[str, Any]]:
    """
    Awaits a long-running asynchronous Azure operation to complete. Performs an additional GET request when operation completes to fetch the resulting Azure resource.
    :param operation_id: Client-supplied unique operation ID
    :param operation_headers: Headers from initial HTTP response from Azure API call which initiated the operation
    :param resource_url: Azure API URL, used to GET the resource produced by the operation
    """
    poller = OPERATION_TRACKERS.get(operation_id)
    if not poller:
        poller = OperationPoller(hub, ctx, operation_headers, resource_url)
        OPERATION_TRACKERS[operation_id] = poller
    try:
        result = await poller.check_operation()
        finished = poller.operation_finished()
        if finished:
            del OPERATION_TRACKERS[operation_id]
        return finished, result
    except Exception as e:
        del OPERATION_TRACKERS[operation_id]
        return True, {"error": str(e)}


class OperationFailed(Exception):
    pass


class OperationStatus:
    """Operation status class.

    Operation status is used to indicate the status of an operation. It can be one of the following values: Succeeded, Failed, Canceled, Running.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    RUNNING = "Running"

    FINISHED_STATES = {SUCCEEDED.lower(), FAILED.lower(), CANCELED.lower()}
    FAILED_STATES = {FAILED.lower(), CANCELED.lower()}
    SUCCEEDED_STATES = {SUCCEEDED.lower()}

    @staticmethod
    def finished(status):
        return str(status).lower() in OperationStatus.FINISHED_STATES

    @staticmethod
    def failed(status):
        return str(status).lower() in OperationStatus.FAILED_STATES

    @staticmethod
    def succeeded(status):
        return str(status).lower() in OperationStatus.SUCCEEDED_STATES


class OperationPoller:
    def __init__(self, hub, ctx, operation_headers, resource_url):
        self._hub = hub
        self._ctx = ctx
        self._operation_headers = operation_headers
        self._resource_url = resource_url
        self._status_url = self._get_status_url()
        self._status = None
        self._error = None

    async def await_operation(self) -> Dict[str, Any]:
        return await self._poll()

    async def check_operation(self) -> Dict[str, Any]:
        return await self._check()

    def _get_status_url(self) -> Optional[str]:
        headers: Dict[str, Any] = self._operation_headers

        if "Azure-AsyncOperation" in headers:
            return headers["Azure-AsyncOperation"]
        elif "Location" in headers:
            return headers["Location"]
        else:
            return None

    def _get_retry_after(self) -> int:
        headers = self._operation_headers

        retry_after = headers.get("Retry-After")
        try:
            delay = int(retry_after)
        except ValueError:
            delay = 1

        return delay if delay > 1 else 1

    def operation_finished(self) -> bool:
        return OperationStatus.finished(self._status)

    def _operation_succeeded(self) -> bool:
        return OperationStatus.succeeded(self._status)

    async def _update_status(self):
        get_response = await self._hub.exec.request.json.get(
            self._ctx,
            url=self._status_url,
            success_codes=[200],
        )
        if "status" in get_response["ret"]:
            self._status = get_response["ret"]["status"].lower()
        else:
            self._status = None
        if "error" in get_response["ret"]:
            self._error = get_response["ret"]["error"]
        else:
            self._error = None

    async def _delay(self):
        await asyncio.sleep(self._get_retry_after())

    async def _poll(self):
        if not self.operation_finished():
            await self._update_status()
        while not self.operation_finished():
            await self._delay()
            await self._update_status()

        if not self._operation_succeeded():
            raise OperationFailed(
                f"Operation failed or has been canceled: {self._error}"
            )
        else:
            get_response = await self._hub.exec.request.json.get(
                self._ctx,
                url=self._resource_url,
                success_codes=[200],
            )
            return get_response

    async def _check(self):
        if not self.operation_finished():
            await self._update_status()

        if not self.operation_finished():
            return None
        elif not self._operation_succeeded():
            raise OperationFailed(
                f"Operation failed or has been canceled: {self._error}"
            )
        else:
            return await self._hub.exec.request.json.get(
                self._ctx,
                url=self._resource_url,
                success_codes=[200],
            )
