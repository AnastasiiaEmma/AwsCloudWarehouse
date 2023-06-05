"""
ETL Script.

This script performs the ETL process from S3 into Redshift
and then inserting the transformed data into final tables.

Author: Anastasiia Shvaiko
"""

import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Load data from S3 into staging tables in Redshift.

    Args:
        cur: Cursor object for executing SQL queries.
        conn: Connection object to Redshift.
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Insert data from staging tables into final tables in Redshift.

    Args:
        cur: Cursor object for executing SQL queries.
        conn: Connection object to Redshift.
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Entry point for ETL process.

    Connects to Redshift, loads data, and inserts into final tables.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect(
        "host={} dbname={} user={} password={} port={}".format(
            *config['CLUSTER'].values()
        )
    )
    cur = conn.cursor()

    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
