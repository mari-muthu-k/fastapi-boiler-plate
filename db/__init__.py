import os
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# environment dependencies
from env import appConfig as db

#MySQL connection
engine=create_engine("mysql+pymysql://"+db.MYSQL_USERNAME+":"+(db.MYSQL_PASS if db.MYSQL_PASS != None else "")+"@"+db.MYSQL_URL+"/"+db.MYSQL_DBNAME)
session =sessionmaker(bind=engine,autocommit=False)
Base=declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()