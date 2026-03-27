import logging
import os
from sqlalchemy import create_engine

def initDB(address='dbAddress'):
    logging.disable(logging.WARNING)
    db = os.getenv(address)
    engine = create_engine(db, future=True)
    return engine

