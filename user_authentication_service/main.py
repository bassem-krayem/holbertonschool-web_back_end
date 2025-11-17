#!/usr/bin/env python3
"""End-to-end integration tests for the user authentication service"""
import requests

BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """Register a new user with the given email and password."""
    url = f"{BASE_URL}/users"
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)
    assert response.status_code == 200, "Failed to register user"
    assert response.json().get("email") == email, (
        "Email mismatch after registration"
    )


def log_in_wrong_password(email: str, password: str) -> None:
    """Attempt to log in with the wrong password."""
    url = f"{BASE_URL}/sessions"
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)
    assert response.status_code == 401, "Logged in with wrong password"


def log_in(email: str, password: str) -> str:
    """Log in with the given email and password, return session_id."""
    url = f"{BASE_URL}/sessions"
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)
    assert response.status_code == 200, "Failed to log in"
    assert response.json().get("email") == email, "Email mismatch after login"
    session_id = response.cookies.get("session_id")
    assert session_id is not None, "No session_id cookie returned"
    return session_id


def profile_unlogged() -> None:
    """Access profile without being logged in."""
    url = f"{BASE_URL}/profile"
    response = requests.get(url)
    assert response.status_code == 403, (
        "Unlogged profile access did not return 403"
    )


def profile_logged(session_id: str) -> None:
    """Access profile when logged in."""
    url = f"{BASE_URL}/profile"
    cookies = {"session_id": session_id}
    response = requests.get(url, cookies=cookies)
    assert response.status_code == 200, "Logged profile access failed"
    assert "email" in response.json(), "Profile response missing email"


def log_out(session_id: str) -> None:
    """Log out the user."""
    url = f"{BASE_URL}/sessions"
    cookies = {"session_id": session_id}
    response = requests.delete(url, cookies=cookies)
    assert response.status_code == 200, "Logout failed"


def reset_password_token(email: str) -> str:
    """Request a password reset token."""
    url = f"{BASE_URL}/reset_password"
    data = {"email": email}
    response = requests.post(url, data=data)
    assert response.status_code == 200, "Reset token request failed"
    token = response.json().get("reset_token")
    assert token is not None, "No reset token returned"
    return token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Update password using the reset token."""
    url = f"{BASE_URL}/reset_password"
    data = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password
    }
    response = requests.put(url, data=data)
    assert response.status_code == 200, "Password update failed"
    assert response.json().get("email") == email, (
        "Email mismatch after password update"
    )
    assert response.json().get("message") == "Password updated", (
        "Unexpected message"
    )


# Test credentials
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
