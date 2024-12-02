from sqlmodel import create_engine, Session

#boilerplate
engine = create_engine(
    "sqlite:///carsharing.db",
    connect_args={"check_same_thread": False},  # Needed for SQLite
    echo=True  # Log generated SQL
)

#creates session
def get_session():
    with Session(engine) as session:
        yield session