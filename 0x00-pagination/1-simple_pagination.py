#!/usr/bin/env python3
import csv
from typing import List
"""Module to gets the compuye indeces and return dataset correctly
"""


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the dataset to be used"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cache dataset and return it
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Function that gets the right dataset or pages"""

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_idx, end_idx = index_range(page, page_size)
        dataset = self.dataset()

        if (start_idx >= len(dataset)):
            return []

        return dataset[start_idx:end_idx]


def index_range(page: int, page_size: int) -> tuple:
    """function to return idices base on page & page size"""

    return ((page - 1)*page_size, page*page_size)
