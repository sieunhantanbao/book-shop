from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import redis
import os
from app.settings import SQLALCHEMY_DATABASE_URL

def get_db_context():
    try:
        db = LocalSession()
        yield db
    finally:
        db.close()


engine = create_engine(SQLALCHEMY_DATABASE_URL)
 
LocalSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

redis_client = redis.Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], password= os.getenv('REDIS_PASSWORD', None), db=0)