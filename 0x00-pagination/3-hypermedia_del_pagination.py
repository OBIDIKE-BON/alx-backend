#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


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

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return dict of pagination data.
            Dict key/value pairs consist of the following:
              index - the start index of the page
              next_index - the start index of the next page
              page_size
              page_size - the number of items on the page
              data - the data in the page itself
        """
        data_len = len(self.indexed_dataset())
        assert index >= 0 and index < data_len
        indexed_dataset = self.indexed_dataset()

        pages = []
        i = index
        while (i < data_len and len(pages) < page_size):
            if indexed_dataset.get(i):
                pages.append(indexed_dataset[i])
            i += 1

        return {
            'index': index,
            'next_index': i,
            'page_size': page_size,
            'data': pages,
        }
