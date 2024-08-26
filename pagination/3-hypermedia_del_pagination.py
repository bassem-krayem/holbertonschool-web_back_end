#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """ a method that return a dict with infos about pagination"""
        assert isinstance(page_size, int) and page_size > 0

        data = []
        with open('Popular_Baby_Names.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)

        max_index = len(data) - 1
        if index is None:
            index = 0
        else:
            assert isinstance(index, int) and 0 <= index <= max_index

        next_index = min(index + page_size, max_index + 1)
        return {
                'index': index,
                'next_index': next_index,
                'page_size': page_size,
                'data': data[index:next_index]
            }
