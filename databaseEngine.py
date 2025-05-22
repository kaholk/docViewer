
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from config_menager import appConfig
import pymssql
import pymysql

url_object = URL.create(
    drivername=appConfig.get('Database', 'Driver'),
    host=appConfig.get('Database', 'Host'),
    username=appConfig.get('Database', 'User'),
    password=appConfig.get('Database', 'Password'),
    database=appConfig.get('Database', 'Database'),
)

engine = create_engine(url_object, echo=False)
DbConnector = sessionmaker(engine)