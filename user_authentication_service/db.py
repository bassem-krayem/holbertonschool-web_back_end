"""DB module"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(
        self,
        email: str,
        hashed_password: str
    ) -> User:
        """
        Add a new user to the database
        Args:
            email (str): The user's email
            hashed_password (str): The user's hashed password
        Returns:
            User: The newly created User object
        """
        new_user = User(email, hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user by given attributes
        Args:
            **kwargs: Arbitrary keyword arguments representing user attributes
        Returns:
            User: The User object that matches the criteria
        Raises:
            NoResultFound: If no user is found with the given attributes
            InvalidRequestError: If an invalid attribute is provided
        """
        query = self._session.query(User)
        for key, value in kwargs.items():
            if not hasattr(User, key):
                raise InvalidRequestError()
            query = query.filter(getattr(User, key) == value)
        user = query.one()
        return user
