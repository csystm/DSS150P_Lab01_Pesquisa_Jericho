# Source Inventory

## 1. CSV Source

| Field | Value |
|-------|-------|
| Source name | customers.csv |
| Source-system type | File-based (CSV) |
| Data format | CSV |
| Structured / semi-structured / unstructured | Structured |
| Expected update pattern | Batch (full snapshot) |
| Likely acquisition method | File download / local file read with pandas |
| Schema location or schema owner | Header row in file; owner unknown |
| Possible primary/business key | customer_id |
| Potential schema-evolution risk | New columns may be added; delimiter or encoding changes |
| Potential data-quality risk | Deliberate missing values and duplicate rows; inconsistent data types |

## 2. JSON Source

| Field | Value |
|-------|-------|
| Source name | orders.json |
| Source-system type | File-based (JSON) |
| Data format | JSON |
| Structured / semi-structured / unstructured | Semi-structured |
| Expected update pattern | Batch (full snapshot likely) |
| Likely acquisition method | File download / local file read with pandas |
| Schema location or schema owner | Nested structure defined by source; owner unknown |
| Possible primary/business key | order_id |
| Potential schema-evolution risk | Nested fields may change; arrays may vary; new optional fields may appear |
| Potential data-quality risk | Missing fields, varying types, duplicate records, nested object complexity |

## 3. Parquet Source

| Field | Value |
|-------|-------|
| Source name | products.parquet |
| Source-system type | File-based (Parquet) |
| Data format | Parquet |
| Structured / semi-structured / unstructured | Structured |
| Expected update pattern | Batch (full snapshot likely) |
| Likely acquisition method | File download / local file read with pandas |
| Schema location or schema owner | Embedded schema in Parquet metadata |
| Possible primary/business key | product_id or identifier field (to be confirmed) |
| Potential schema-evolution risk | Schema evolution handled by Parquet but may cause issues if not coordinated |
| Potential data-quality risk | Nulls, duplicate rows, invalid product prices or stock values |

## 4. REST API Source

| Field | Value |
|-------|-------|
| Source name | Public REST API: JSONPlaceholder /posts (fallback: local API /api/orders) |
| Source-system type | Web API |
| Data format | JSON |
| Structured / semi-structured / unstructured | Semi-structured |
| Expected update pattern | Unknown, likely on-demand or batch |
| Likely acquisition method | HTTP GET request with `requests` |
| Schema location or schema owner | API documentation / response structure |
| Possible primary/business key | id (for /posts) or order_id (for local /api/orders) |
| Potential schema-evolution risk | API version changes, field additions/removals |
| Potential data-quality risk | Network failures, rate limiting, missing data, malformed response |

## 5. PostgreSQL Source

| Field | Value |
|-------|-------|
| Source name | support_tickets |
| Source-system type | Relational database |
| Data format | Table |
| Structured / semi-structured / unstructured | Structured |
| Expected update pattern | Unknown, likely batch or incremental |
| Likely acquisition method | SQL query via SQLAlchemy / psycopg2 |
| Schema location or schema owner | Database schema (information_schema) |
| Possible primary/business key | ticket_id |
| Potential schema-evolution risk | ALTER TABLE changes, new columns, type changes |
| Potential data-quality risk | Nulls in assigned_agent and resolved_at; timestamp format issues; duplicate tickets |

---

**Retrieved API snapshot timestamp (UTC):** `2026-08-24T11:14:28.649020+00:00`