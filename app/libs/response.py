from app.libs.error_code import Success


# 'state': task.state,
#                 'current': task.info.get('current', 0),
#                 'total': task.info.get('total', 1),
#                 'status': task.info.get('status', '')

class ResultResponse(Success):
    data = {
        # "state": '',
        # "current": 0,
        # "total": 100,
        # "images": [],
        # "pbb": [],
    }
