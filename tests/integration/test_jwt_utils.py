from app.utils.jwt import verify_jwt_token

def test_jwt_invalid_token():
    invalid_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyQGV4YW1wbGUuY29tIn0.invalidsignature"
    try:
        verify_jwt_token(invalid_token)
        assert False  # Should not reach here
    except Exception as e:
        assert "Signature verification failed" in str(e)
