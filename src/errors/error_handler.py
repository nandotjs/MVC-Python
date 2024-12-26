from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.error_types.http_not_found import HttpNotFoundError
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.views.http_types.http_response import HttpResponse

def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError, HttpNotFoundError, HttpBadRequestError):
        return HttpResponse(error.status_code, body={
            "title": error.error_type, 
            "detail": error.message,
        })
    return HttpResponse(500, body={
        "title": "internal_server_error", 
        "detail": str(error),
    })
