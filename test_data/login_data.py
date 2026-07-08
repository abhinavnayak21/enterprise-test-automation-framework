class LoginData:
    """Test data for login scenarios."""

    VALID_USERS = [
        ("Admin", "admin123"),
    ]

    INVALID_USERS = [
        ("Admin", "wrongpassword"),
        ("wronguser", "admin123"),
        ("wronguser", "wrongpassword"),
        ("", "admin123"),
        ("Admin", ""),
        ("", ""),
    ]
