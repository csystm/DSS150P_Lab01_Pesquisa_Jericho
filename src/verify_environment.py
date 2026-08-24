from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://dss150p:dss150p_lab@localhost:5433/dss150p_lab")

with engine.connect() as conn:
    print("PostgreSQL version:")
    version = conn.execute(text("SELECT version();")).scalar()
    print(version)

    print("Current database:")
    current_db = conn.execute(text("SELECT current_database();")).scalar()
    print(current_db)