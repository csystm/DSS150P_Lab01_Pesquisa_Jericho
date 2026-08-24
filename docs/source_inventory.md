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

**Retrieved API snapshot timestamp (UTC):** `2026-08-24T13:39:34.610465+00:00`

## 5. PostgreSQL Source

| Field | Value |
|-------|-------|
| Source name | support_tickets |
| Source-system type | Relational database |
| Data format | Table |
| Structured / semi-structured / unstructured | Structured |
| Expected update pattern | Unknown, likely batch or incremental |
| Likely acquisition method | SQL query via SQLAlchemy / psycopg2 |
| Schema location or schema owner | public schema |
| Possible primary/business key | ticket_id |
| Potential schema-evolution risk | ALTER TABLE changes, new columns, type changes |
| Potential data-quality risk | Nulls in assigned_agent and resolved_at; timestamp format issues; possible orphan customer_id references |

### Table Metadata

- **Table name:** `support_tickets`
- **Columns:**
  - `ticket_id` (integer, NO) - primary key
  - `customer_id` (character varying, NO)
  - `category` (character varying, NO)
  - `priority` (character varying, NO)
  - `assigned_agent` (character varying, YES) - nullable
  - `opened_at` (timestamp without time zone, NO)
  - `resolved_at` (timestamp without time zone, YES) - nullable
  - `status` (character varying, NO)
- **Constraints:**
  - `support_tickets_pkey` PRIMARY KEY (ticket_id)
- **Row count:** 250
- **Sample rows:**
  - `(1, 'C0246', 'Technical', 'High', 'J. Reyes', 2026-06-19 04:00:00, 2026-06-21 13:00:00, 'Resolved')`
  - `(2, 'C0130', 'Product', 'Medium', 'J. Reyes', 2026-05-26 07:00:00, 2026-05-26 23:00:00, 'Closed')`
  - `(3, 'C0094', 'Delivery', 'Medium', 'J. Reyes', 2026-03-28 09:00:00, 2026-03-31 17:00:00, 'Closed')`
  - `(4, 'C0057', 'Technical', 'High', 'L. Tan', 2026-04-25 19:00:00, NULL, 'In Progress')`
  - `(5, 'C0120', 'Delivery', 'High', 'R. Cruz', 2026-01-20 02:00:00, 2026-01-22 21:00:00, 'Resolved')`

