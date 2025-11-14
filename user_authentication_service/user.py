#!/usr/bin/env python3
"""
User module
Defines the User class for user authentication service
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    """
    User class
    Represents a user in the authentication service
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(
        self,
        email: str,
        hashed_password: str,
        session_id: str = None,
        reset_token: str = None
    ) -> None:
        """Initialize User instance"""
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id
        self.reset_token = reset_token
