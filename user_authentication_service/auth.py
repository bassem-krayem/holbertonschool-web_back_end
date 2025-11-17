#!/usr/bin/env python3
"""auth module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt.
    Args:
        password (str): The plain text password to hash
    Returns:
        bytes: The hashed password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a new UUID string.
    Returns:
        str: A new UUID string
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.
        Args:
            email (str): The user's email
            password (str): The user's plain text password
        Returns:
            User: The newly created User object
        Raises:
            ValueError: If a user with the given email already exists
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user login.
        Args:
            email (str): The user's email
            password (str): The user's plain text password
        Returns:
            bool: True if the login is valid, False otherwise
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Create a new session for a user.
        Args:
            email (str): The user's email
        Returns:
            str: The session ID
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Get a user from a session ID.
        Args:
            session_id (str): The session ID
        Returns:
            User: The User object associated with the session ID
        if session_id is None:
            return None
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroy a user's session.
        Args:
            user_id (int): The user's ID
        Returns:
            None
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """
        Generate a password reset token for a user.
        Args:
            email (str): The user's email
        Returns:
            str: The password reset token
        Raises:
            ValueError: If no user is found with the given email
        """
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError()

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Update a user's password using a reset token.
        Args:
            reset_token (str): The password reset token
            password (str): The new plain text password
        Returns:
            None
        Raises:
            ValueError: If no user is found with the given reset token
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(user.id,
                                 hashed_password=hashed_password,
                                 reset_token=None)
        except NoResultFound:
            raise ValueError()
