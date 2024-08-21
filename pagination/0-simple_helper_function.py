#!/usr/bin/env python3
"""
This module provides a utility function for calculating start and end
indexes for paginating a list of items based on a given page number
and page size.

Functions:
    index_range(page: int, page_size: int) -> Tuple[int, int]:
        Calculates the start and end indexes for a page of items.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for pagination based on the
    given page number and page size.

    This function is useful for dividing a list of items into pages
    for pagination purposes. The page numbers are 1-indexed, meaning
    the first page is represented by 1, the second by 2, and so on.

    Args:
        page (int): The current page number, where the first page is 1.
        page_size (int): The number of items that should be displayed
        on each page.

    Returns:
        tuple: A tuple containing two integers. The first integer is
        the start index, which is the index of the first item on the
        page. The second integer is the end index, which is one past
        the index of the last item on the page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
