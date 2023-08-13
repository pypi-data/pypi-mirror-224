"""Utilities for the GeneWeaver database functions."""
from typing import List

from geneweaver.db.exceptions import GeneweaverDoesNotExistError, GeneweaverValueError
from psycopg.rows import Row


def unpack_one_item_fetchall_results(results: List[Row]) -> List:
    """Unpack a single column from multiple rows of results.

    :param results: The results from a fetchall call.

    :raises GeneweaverDoesNotExistError: If the result is empty.
    :raises GeneweaverTooManyResultsError: If the result has more than one row.

    :return: The single row from the results.
    """
    if len(results) == 0:
        raise GeneweaverDoesNotExistError("No results found.")

    if len(results[0]) > 1:
        raise GeneweaverValueError("Too many results to unpack.")

    return [t[0] for t in results]
