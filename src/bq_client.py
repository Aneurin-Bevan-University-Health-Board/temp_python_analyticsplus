"""Reusable BigQuery client helper."""
from google.cloud import bigquery


def get_client(project: str) -> bigquery.Client:
    return bigquery.Client(project=project)


def query_to_df(client: bigquery.Client, sql: str):
    return client.query(sql).to_dataframe()
