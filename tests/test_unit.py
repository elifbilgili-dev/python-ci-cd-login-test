from app import validate_email


def test_validate_email():
    assert validate_email("elif@example.com") == True