from src.consts import appctx
import arrow


def response(status_code, message=None, data=None, meta=None):
    status = {}
    status['code'] = status_code
    if status_code in appctx.success_status:
        status['status'] = appctx.success_status[status_code]
        status['message'] = message if message else appctx.success_status[status_code]
    elif status_code in appctx.failure_status:
        status['status'] = appctx.failure_status[status_code]
        status['message'] = message if message else appctx.failure_status[status_code]
    else:
        status['status'] = appctx.failure_status[status_code]
        status['message'] = message if message else appctx.failure_status[400]

    if data is not None:
        status['data'] = data
    if meta is not None:
        status['meta'] = meta
    return status