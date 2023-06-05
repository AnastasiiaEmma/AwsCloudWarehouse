"""
Create Tables Script.

It connects to Redshift and drops tables (if any) before creating new ones.

Author: Anastasiia
"""
import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Drop all the tables in the database.

    Args:
        cur: psycopg2 cursor object.
        conn: psycopg2 connection object.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Create all the tables in the database.

    Args:
        cur: psycopg2 cursor object.
        conn: psycopg2 connection object.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Entry point to drop and create.

    Drop and create tables in the Redshift cluster.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect(
        "host={} dbname={} user={} password={} port={}".format(
            *config['CLUSTER'].values()
        )
    )
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
