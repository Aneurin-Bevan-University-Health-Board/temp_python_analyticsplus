"""Reusable GCS helper."""
from google.cloud import storage


def download_blob(bucket_name: str, blob_name: str, destination: str) -> None:
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    bucket.blob(blob_name).download_to_filename(destination)
    print(f"Downloaded gs://{bucket_name}/{blob_name} -> {destination}")


def upload_blob(bucket_name: str, source_file: str, destination_blob: str) -> None:
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    bucket.blob(destination_blob).upload_from_filename(source_file)
    print(f"Uploaded {source_file} -> gs://{bucket_name}/{destination_blob}")
