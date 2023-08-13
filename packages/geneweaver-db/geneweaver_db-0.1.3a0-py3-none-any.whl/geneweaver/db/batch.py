""""""
from geneweaver.core.schema.batch import BatchUploadGeneset
from psycopg import Cursor


def prepare_batch_geneset_for_insertion(
    geneset: BatchUploadGeneset,
    user_id: int,
    file_id: int,
) -> dict:
    """Prepare a geneset for insertion into the database."""
    geneset_dict = geneset.dict(
        exclude={"values", "species", "score", "pubmed_id", "private"}
    )
    geneset_dict["count"] = len(geneset.values)
    geneset_dict["user_id"] = user_id
    geneset_dict["file_id"] = file_id

    # TODO: Get species ID
    geneset_dict["species_id"] = geneset.species

    # TODO: Get publication ID type
    geneset_dict["publication_id"] = 0

    # TODO: Get Threshold Type
    geneset_dict["threshold_type"] = "p"
    geneset_dict["threshold"] = 0.05

    return geneset_dict


def insert_user_geneset(
    cursor: Cursor, geneset: BatchUploadGeneset, user_id: int
) -> int:
    """Insert a geneset into the database."""
    geneset_dict = prepare_batch_geneset_for_insertion(geneset, user_id)

    cursor.execute(
        """
        INSERT INTO geneset
            (usr_id, file_id,
            gs_name, gs_abbreviation,
            pub_id, cur_id,
            gs_description, sp_id,
            gs_count,
            gs_threshold_type, gs_threshold,
            gs_groups,
            gs_gene_id_type,
            gs_created, gs_attribution)
        VALUES
            (%(user_id)s, %(file_id)s,
            %(name)s, %(abbreviation)s,
            %(publication_id)s, %(curation_id)s,
            %(description)s, %(species_id)s,
            %(count)s,
            %(threshold_type)s, %(threshold)s,
            %(groups)s,
            %(gene_id_type)s,
            %(created)s, %(attribution)s)
        RETURNING gs_id;
        """,
        geneset_dict,
    )

    cursor.connection.commit()

    return cursor.fetchone()[0]
