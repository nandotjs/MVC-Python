from src.validators.owner_creator_validator import validate_owner_creator

class MockRequest:
    def __init__(self, body) -> None:
        self.body = body

def test_validate_owner_creator_request():
    request = MockRequest(body={"first_name": "John", "last_name": "Doe", "age": 30, "pet_id": 1})
    validate_owner_creator(request)

