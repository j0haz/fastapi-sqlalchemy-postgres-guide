import os
import sqlalchemy as sqla

DATABASE_FILE = os.getenv("SQLITE_DB")

DATABASE_URL = f"sqlite:////app/databases/{DATABASE_FILE}"

engine = sqla.create_engine(DATABASE_URL)

Base = sqla.orm.declarative_base()

# Dependency
SessionLocal = sqla.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()