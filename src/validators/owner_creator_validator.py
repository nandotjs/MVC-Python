from pydantic import BaseModel, constr
from src.views.http_types.http_request import HttpRequest
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from pydantic import ValidationError


def validate_owner_creator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        first_name: constr(min_length=1, max_length=50) # type: ignore
        last_name: constr(min_length=1, max_length=50) # type: ignore
        age: int
        pet_id: int

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
