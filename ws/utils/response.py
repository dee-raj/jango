from rest_framework.response import Response
from rest_framework import status


class BaseResponse(Response):
    def __init__(
        self,
        success,
        message,
        data=None,
        errors=None,
        code:200
        status_code=status.HTTP_200_OK,
    ):
        payload = {
            "success": success,
            "message": message,
            "data": data,
            "errors": errors,
            "code":code,
        }
        super().__init__(payload, status=status_code)

        self.exception = True


class SuccessResponse(BaseResponse):
    def __init__(self, message="Success", data=None, status_code=status.HTTP_200_OK):
        super().__init__(True, message, data=data, status_code=status_code)


class ErrorResponse(BaseResponse):
    def __init__(
        self, message="Error", errors=None, status_code=status.HTTP_400_BAD_REQUEST
    ):
        super().__init__(False, message, errors=errors, status_code=status_code)
