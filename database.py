from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import json, os

from dotenv import load_dotenv


load_dotenv()
Base = declarative_base()

DATABASE_URL = f"mysql+mysqlconnector://{os.environ.get('DBROOTUSERNAME')}:{os.environ.get('PASSWORD')}@{os.environ.get('HOSTNAME')}:{os.environ.get('PORT')}/{os.environ.get('DBNAME')}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
