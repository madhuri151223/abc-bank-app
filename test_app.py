from app import login

def test_valid_login():
    result = login("customer", "bank123")
    assert result == "Login Successful"
