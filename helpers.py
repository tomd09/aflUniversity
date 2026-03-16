import logging
import os
from sqlalchemy import create_engine

def initDB():
    logging.disable(logging.WARNING)
    db = os.getenv('dbAddress')
    engine = create_engine(db, future=True)
    return engine

