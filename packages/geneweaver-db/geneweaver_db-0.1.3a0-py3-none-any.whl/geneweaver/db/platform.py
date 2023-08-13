from typing import List

from psycopg import Cursor


def by_id(cursor: Cursor, platform_id: int) -> List:
    cursor.execute(
        """
            SELECT *
            FROM odestatic.platform
            WHERE pf_id = %(platform_id)s;
        """,
        {"platform_id": platform_id},
    )
    return cursor.fetchall()
