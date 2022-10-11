from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json


with open("./secret.json", "r") as f:
    userData = json.load(f)

print(userData)
DATABASE_URL = f"mysql+mysqlconnector://{userData['USERNAME']}:{userData['PASSWORD']}@{userData['HOSTNAME']}:{userData['PORT']}/{userData['DBNAME']}"
print(DATABASE_URL)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
