"""GCP Secret Manager helper."""
from google.cloud import secretmanager


def get_secret(project_id: str, secret_id: str, version: str = "latest") -> str:
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version}"
    return client.access_secret_version(request={"name": name}).payload.data.decode("UTF-8")
