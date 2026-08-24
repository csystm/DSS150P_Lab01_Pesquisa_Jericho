# DSS150P Lab 01 – Data Engineering Workspace and Source Assessment

**Student Name:** Pesquisa, Jericho B.
**Student Number:** 2024111404

## Purpose of the Laboratory

This laboratory establishes a reproducible local data-engineering workspace and performs a first-pass technical assessment of several source systems. It covers environment setup, source profiling, API inspection, relational database inspection, schema creation, and data contract definition. The goal is to build evidence that the development environment works and to document how data will move from source systems to a downstream consumer.

## Software Requirements

- Python 3.x
- Git
- Docker Desktop / Docker Engine with Docker Compose
- A code editor (VS Code recommended)
- Terminal/command-line shell
- Internet access (for API and package installation)

## Steps to Reproduce the Environment

1. Clone or create the repository folder.
2. Open a terminal in the repository root.
3. Create and activate a Python virtual environment:
   ```bash
   python -m venv .venv
   # Windows PowerShell:
   .\.venv\Scripts\Activate.ps1
   # macOS/Linux:
   source .venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the PostgreSQL container:
   ```bash
   docker compose up -d
   ```
6. Run the environment verification script:
   ```bash
   python src/verify_environment.py
   ```
7. (Optional) Load the PostgreSQL sample table if not already present:
   ```bash
   Get-Content sql/seed_support_tickets.sql | docker exec -i dss150p-postgres psql -U dss150p -d dss150p_lab
   ```
8. Run profiling and API inspection scripts as needed.

## Exact Commands to Start and Stop PostgreSQL

**Start:**
```bash
docker compose up -d
```

**Stop:**
```bash
docker compose down
```

**Stop but keep data volume (safe for later restart):**
```bash
docker compose down
```
(The named volume `dss150p_pgdata` persists, so data remains.)

## How to Run Each Python Script

- **Verify environment (PostgreSQL connection):**
  ```bash
  python src/verify_environment.py
  ```
- **Profile CSV, JSON, and Parquet sources:**
  ```bash
  python src/profile_sources.py
  ```
- **Inspect REST API and save snapshot:**
  ```bash
  python src/inspect_api.py
  ```
- **Inspect PostgreSQL source metadata:**
  ```bash
  python src/inspect_postgres.py
  ```

## Description of Each Source

| Source | Format | Description |
|--------|--------|-------------|
| `customers.csv` | CSV | 250 rows with customer contact/location info, signup date, and segment. Contains deliberate missing and duplicate values. |
| `orders.json` | JSON | 250 order records with timestamp, numeric measures, and a nested `shipping` object. |
| `products.parquet` | Parquet | 200 product rows with identifiers, category, brand, and numeric fields. |
| REST API | JSON | Public API (`jsonplaceholder.typicode.com/posts`) or local fallback returning 100 records. |
| PostgreSQL | Table | `support_tickets` table with 250 rows; `ticket_id` is primary key. |

## Known Limitations or Unresolved Questions

- The API snapshot may be static, but its long-term availability is not guaranteed; the timestamp documents the retrieval time.
- `customers.csv` contains duplicate rows and non-unique `customer_id`; further cleaning or deduplication policy is needed.
- The nested `shipping` object in `orders.json` was flattened for the relational schema; future changes to that nested structure require monitoring.
- The source owner for all provided data is unknown, so business rules and update patterns need confirmation.