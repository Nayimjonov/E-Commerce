from rest_framework.response import Response
from rest_framework import status

def success_response(data, code=status.HTTP_200_OK):
    return Response({
        "success": True,
        "data": data
    }, status=code)


def error_response(field, message, code="INVALID_REQUEST", http_status=status.HTTP_400_BAD_REQUEST):
    return Response({
        "success": False,
        "error": {
            "code": code,
            "message": "The provided data is invalid",
            "details": {
                "field": field,
                "message": message
            }
        }
    }, status=http_status)
