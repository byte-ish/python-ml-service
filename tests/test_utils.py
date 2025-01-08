from app.utils.jwt import create_jwt_token, verify_jwt_token

def test_create_jwt_token():
    payload = {"sub": "test@example.com"}
    token = create_jwt_token(payload)
    assert isinstance(token, str)

def test_verify_jwt_token():
    payload = {"sub": "test@example.com"}
    token = create_jwt_token(payload)
    decoded = verify_jwt_token(token)
    assert decoded["sub"] == "test@example.com"
