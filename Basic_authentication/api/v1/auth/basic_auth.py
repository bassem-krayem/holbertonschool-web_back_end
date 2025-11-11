#!/usr/bin/env python3

"""Basic Authentication module."""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class for handling basic authentication.
    """
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        Extracts the Base64 part of the Authorization header.

        Args:
            authorization_header (str): The Authorization header.

        Returns:
            str: The Base64 part of the header or None if invalid.
        """
        if (authorization_header is not None
                and isinstance(authorization_header, str)):
            if authorization_header.startswith("Basic "):
                return authorization_header.split(" ")[1]
        return None
