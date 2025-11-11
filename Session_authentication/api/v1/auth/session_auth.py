#!/usr/bin/env python3
""" Session authentication module """
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ SessionAuth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a Session ID for a user_id
        Args:
            user_id (str): The user ID
        Returns:
            str: The session ID
            or None if user_id is None or not a string
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Get a user_id based on a session_id
        Args:
            session_id (str): The session ID
        Returns:
            str: The user ID
            or None if session_id is None or not found
        """
        if (
            session_id is None and
            not isinstance(session_id, str)
        ):
            return None
        return self.user_id_by_session_id.get(session_id)
