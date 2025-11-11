#!/usr/bin/env python3

"""Basic Authentication module."""

from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Decodes the Base64 encoded Authorization header.

        Args:
            base64_authorization_header (str): The Base64 encoded header.

        Returns:
            str: The decoded string or None if decoding fails.
        """
        if (
            base64_authorization_header is not None
            and isinstance(base64_authorization_header, str)
        ):
            try:
                decoded_bytes = base64.b64decode(
                    base64_authorization_header.encode('utf-8'), validate=True
                )
                return decoded_bytes.decode('utf-8')
            except Exception:
                return None
        return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        if (
            decoded_base64_authorization_header is not None and
            isinstance(decoded_base64_authorization_header, str) and
            ':' in decoded_base64_authorization_header
        ):
            user, password = decoded_base64_authorization_header.split(':', 1)
            return user, password
        return None, None
