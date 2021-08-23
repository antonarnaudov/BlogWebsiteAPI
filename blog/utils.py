from django.db import ProgrammingError, IntegrityError
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        if isinstance(exc, ProgrammingError):
            response = Response(str(exc), status=status.HTTP_404_NOT_FOUND)

        if isinstance(exc, ValidationError) or isinstance(exc, ValueError) or isinstance(exc, IntegrityError):
            response = Response(str(exc), status=status.HTTP_400_BAD_REQUEST)

    return response
