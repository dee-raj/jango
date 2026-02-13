from rest_framework import status
from rest_framework.views import exception_handler
from core.utils.response import ErrorResponse
from django.conf import settings


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    isDebug = settings.DEBUG
    if isDebug and response is None:
        print(f"Exception: {exc}\nContext: {context}\nResponse: {response}", end="\n")

    if response is None:
        return ErrorResponse(
            message="Internal server error",
            errors=str(exc) if isDebug else "Something went wrong",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return ErrorResponse(
        message="Request failed",
        errors=response.data,
        status_code=response.status_code,
    )
