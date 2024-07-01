#!/usr/bin/env python3
"""Module to get idices"""


def index_range(page: int, page_size: int) -> tuple:
    """function to return idices base on page & page size"""

    return ((page - 1)*page_size, page*page_size)
