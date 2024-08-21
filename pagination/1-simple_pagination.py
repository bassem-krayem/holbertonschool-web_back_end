#!/usr/bin/env python3
"""
This module defines a `Server` class used to paginate a dataset of popular 
baby names. The dataset is loaded from a CSV file and cached for efficient 
pagination.

Module Contents:
- `Server` class: Handles the loading and pagination of the dataset.
  - Attributes:
    - `DATA_FILE` (str): The path to the CSV file containing the dataset.
    - `__dataset` (List[List]): A cached dataset read from the CSV file.
  - Methods:
    - `__init__()`: Initializes a new `Server` instance with an empty dataset.
    - `dataset() -> List[List]`: Loads the dataset from the CSV file if not 
      already cached and returns it, excluding the header row.
    - `get_page(page: int = 1, page_size: int = 10) -> List[List]`: Retrieves 
      a list of rows for a specified page and page size. It raises an 
      `AssertionError` if the page or page size are not positive integers.
- `index_range(page: int, page_size: int) -> Tuple[int, int]`: A helper 
  function that calculates the start and end indices for a specific page 
  based on the given page number and page size. 

Usage Example:
    server = Server()
    page_data = server.get_page(page=2, page_size=5)
    print(page_data)  # Output will be the rows for page 2 with 5 items per page
"""

import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server class with an empty dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load the dataset from the CSV file if not cached.

        Returns:
            List[List]: The dataset excluding the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a list of rows for a specific page.

        Args:
            page (int): The page number to retrieve.
            page_size (int): The number of items per page.

        Returns:
            List[List]: The list of rows for the requested page.

        Raises:
            AssertionError: If `page` or `page_size` are not positive integers.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        index: Tuple[int, int] = index_range(page, page_size)
        return self.dataset()[index[0]: index[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the start and end index for pagination.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: The start and end index for the page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
