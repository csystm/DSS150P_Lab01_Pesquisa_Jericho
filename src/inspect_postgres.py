from sqlalchemy import create_engine, text

DB_URL = "postgresql+psycopg2://dss150p:dss150p_lab@localhost:5433/dss150p_lab"

engine = create_engine(DB_URL)
with engine.connect() as conn:
    print("Tables:")
    result = conn.execute(text("""
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_schema NOT IN ('pg_catalog','information_schema')
    """))
    for row in result:
        print(row)

    print("\nColumns of support_tickets:")
    result = conn.execute(text("""
        SELECT column_name, data_type, is_nullable
        FROM information_schema.columns
        WHERE table_name = 'support_tickets'
        ORDER BY ordinal_position
    """))
    for row in result:
        print(row)

    print("\nConstraints:")
    result = conn.execute(text("""
        SELECT conname, contype, pg_get_constraintdef(oid)
        FROM pg_constraint
        WHERE conrelid = 'support_tickets'::regclass
    """))
    for row in result:
        print(row)

    print("\nRow count:")
    print(conn.execute(text("SELECT COUNT(*) FROM support_tickets")).scalar())

    print("\nSample rows:")
    result = conn.execute(text("SELECT * FROM support_tickets LIMIT 5"))
    for row in result:
        print(row)