from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine('postgresql://andriypovzun:112233@localhost/store')

__session = sessionmaker(engine, autocommit=True)
session: Session = __session()
