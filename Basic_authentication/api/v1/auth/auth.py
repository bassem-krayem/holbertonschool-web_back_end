#!/usr/bin/env python3
"""
Module for authentication routes
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Authentication class to manage API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determine if authentication is required for a given path.

        Args:
            path (str): The request path.
            excluded_paths (List[str]): List of paths that
            do not require authentication.
        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is not None and excluded_paths is not None:
            if path[-1] != '/':
                path += '/'
            if path in excluded_paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieve the Authorization header from the request.

        Args:
            request: The Flask request object.
        Returns:
            str: The value of the Authorization header or None if not present.
        """
        if request is not None:
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieve the current user based on the request.

        Args:
            request: The Flask request object.
        Returns:
            TypeVar('User'): The current user or None if not authenticated.
        """
        return None
