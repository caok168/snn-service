from app.libs.error import APIException

__author__ = 'kai.cao'


class Success(APIException):
    code = 200
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    code = 202
    error_code = 1


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999


class ServiceError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999

    def set_message(self, msg):
        self.msg = msg
        return self


class DbServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999

    def set_message(self, msg):
        self.msg = msg
        return self


class ClientTypeError(APIException):
    # 400 401 403 404
    # 500
    # 200 201 204
    # 301 302
    code = 400
    msg = 'client is invalid'
    error_code = 1006

