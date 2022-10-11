from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json


with open("./secret.json", "r") as f:
    userData = json.load(f)

Base = declarative_base()

DATABASE_URL = f"mysql+mysqlconnector://{userData['USERNAME']}:{userData['PASSWORD']}@{userData['HOSTNAME']}:{userData['PORT']}/{userData['DBNAME']}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
