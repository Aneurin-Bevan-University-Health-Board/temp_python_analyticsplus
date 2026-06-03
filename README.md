# Python Analytics+ Template

Extended analytics starter for heavier workloads. Same GCP tooling as `temp_python_analytics` plus a higher-spec Codespaces machine and additional libraries for larger datasets and ML preprocessing.

**Use this when:** you're working with large DataFrames, doing feature engineering, running batch scoring, or processing data at a scale where the standard devcontainer feels slow.

---

## Quick Start

1. Click **Use this template** → create your repo
2. Open in GitHub Codespaces — the devcontainer requests a **8-core / 32GB** machine automatically
3. Authenticate with GCP (see [GCP Login](#gcp-login))
4. Start coding in `src/`

---

## Folder Structure

```
.
├── .devcontainer/       # High-power Codespaces config
├── src/                 # Python source code
├── notebooks/           # Jupyter notebooks
├── tests/               # Unit tests
├── data/                # Local sample data (gitignored)
├── scripts/             # Utility/run scripts
├── requirements.txt     # Python dependencies
└── .env.example         # Environment variable template
```

---

## GCP Login

### Option 1 — Application Default Credentials (recommended for Codespaces)

```bash
gcloud auth application-default login
```

Opens a browser flow and stores credentials locally. All GCP client libraries pick these up automatically.

### Option 2 — Service Account Key (CI / non-interactive)

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
```

Never commit service account keys. Use Secret Manager or GitHub Secrets instead.

### Verify your auth

```bash
gcloud auth list
gcloud config get-value project
```

---

## What's Different from `temp_python_analytics`

| Feature | analytics | analyticsplus |
|---------|-----------|---------------|
| Codespaces machine | 2-core / 8GB (default) | 8-core / 32GB |
| pandas / numpy | ✔ | ✔ |
| BigQuery / GCS / Vertex / SecretManager | ✔ | ✔ |
| polars (fast DataFrame) | ✘ | ✔ |
| dask (parallel/out-of-core) | ✘ | ✔ |
| scikit-learn | ✘ | ✔ |
| mlflow (experiment tracking) | ✘ | ✔ |
| pytest + coverage | basic | ✔ |

---

## GCP Services

### BigQuery
```python
from google.cloud import bigquery
client = bigquery.Client(project="your-gcp-project")
df = client.query("SELECT * FROM `project.dataset.table`").to_dataframe()
```

### Cloud Storage
```python
from google.cloud import storage
client = storage.Client()
bucket = client.bucket("your-bucket")
bucket.blob("file.parquet").download_to_filename("local.parquet")
```

### Secret Manager
```python
from google.cloud import secretmanager
client = secretmanager.SecretManagerServiceClient()
name = "projects/your-project/secrets/your-secret/versions/latest"
value = client.access_secret_version(request={"name": name}).payload.data.decode()
```

### Vertex AI
```python
from google.cloud import aiplatform
aiplatform.init(project="your-gcp-project", location="europe-west2")
```

---

## Environment Variables

```bash
cp .env.example .env
```

Never commit `.env`.

---

## Running Tests

```bash
pytest tests/ --cov=src
```
