from typing import List, Optional

from geneweaver.db.exceptions import GeneweaverDoesNotExistError
from psycopg import Cursor, rows


def add_to_geneset(
    cursor: Cursor, geneset_id: int, ontology_id: int, geneset_ontology_ref_type: str
) -> None:
    """Add an ontology to a geneset.

    This function will call cursor.connection.commit() to commit the changes to the
    database.

    :param cursor: The database cursor.
    :param geneset_id: The geneset ID to add the ontology to.
    :param ontology_id: The ontology ID to add to the geneset.
    :param geneset_ontology_ref_type: The type of ontology reference.

    :return: None
    """
    cursor.execute(
        """
        INSERT INTO extsrc.geneset_ontology
            (gs_id, ont_id, gso_ref_type)
        VALUES
            (%(geneset_id)s, %(ontology_id)s, %(geneset_ontology_ref_type)s);
        """,
        {
            "geneset_id": geneset_id,
            "ontology_id": ontology_id,
            "geneset_ontology_ref_type": geneset_ontology_ref_type,
        },
    )
    cursor.connection.commit()


def get_ids_by_refs(cursor: Cursor, ontology_ref_ids: List[int]) -> List[int]:
    """Get the ont_ids (if they exist) for each of the given ont_ref_ids.

    :param cursor: The database cursor.
    :param ontology_ref_ids: list of the ontology reference IDs

    :return: List of ont_ids
    """
    cursor.execute(
        """
        SELECT ont_id
        FROM extsrc.ontology
        WHERE ont_ref_id = ANY(%s)
        """,
        (ontology_ref_ids,),
    )

    result = cursor.fetchall()

    if not result:
        return []

    return [t[0] for t in result]


def get_refs_by_ids(cursor: Cursor, ontology_ids: List[int]) -> List[str]:
    """Get the ont_ref_ids (if they exist) for each of the given ont_ids.

    :param cursor: The database cursor.
    :param ontology_ids: list of the ontology IDs

    :return: List of ont_ref_ids
    """
    cursor.execute(
        """
        SELECT ont_ref_id
        FROM extsrc.ontology
        WHERE ont_id = ANY(%s)
        """,
        (ontology_ids,),
    )

    result = cursor.fetchall()

    if not result:
        return []

    return [t[0] for t in result]


def sources(cursor: Cursor, ontology_source_id: Optional[int] = None) -> List:
    """Get all ontology sources from the database, optionally by ID.

    :param cursor: The database cursor.
    :param ontology_source_id: The ontology database ID. Returns all if None or not set.

    :raises GeneweaverDoesNotExistError: If the ontology source does not exist.

    :return: List of ontology sources
    """
    if ontology_source_id is None:
        cursor.execute(
            """
            SELECT * FROM odestatic.ontologydb;
            """
        )
        result = cursor.fetchall()
    else:
        result = [source_by_id(cursor, ontology_source_id)]

    return result


def source_by_id(cursor: Cursor, ontology_source_id: int) -> rows.Row:
    """Get the ontology source by ID.

    :param cursor: The database cursor.
    :param ontology_source_id: The ontology database ID.

    :raises GeneweaverDoesNotExistError: If the ontology source does not exist.

    :return: The ontology source.
    """
    cursor.execute(
        """
        SELECT * FROM odestatic.ontologydb WHERE ontdb_id = %(ontology_source_id)s;
        """,
        {"ontology_source_id": ontology_source_id},
    )
    result = cursor.fetchone()
    if result is None:
        raise GeneweaverDoesNotExistError(
            f"Ontology source with ID {ontology_source_id} does not exist."
        )
    return result


def source_id_by_name(cursor: Cursor, ontology_name: str) -> int:
    """Get the ontology source ID by name.

    :param cursor: The database cursor.
    :param ontology_name: The name of the ontology source to get the ID for.

    :raises GeneweaverDoesNotExistError: If the ontology source does not exist.

    :return: The ontology source ID.
    """
    cursor.execute(
        """
        SELECT ontdb_id FROM odestatic.ontologydb WHERE ontdb_name = %(ontology_name)s;
        """,
        {"ontology_name": ontology_name},
    )
    result = cursor.fetchone()
    if result is None:
        raise GeneweaverDoesNotExistError(
            f"Ontology source with name '{ontology_name}' does not exist."
        )
    return result[0]
