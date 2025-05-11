
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker


url_object = URL.create(
    drivername="mssql+pymssql",
    host="192.168.0.9",
    username="KBT\\karol.brodka",
    password="Dutron2023!",
    database="BC_TEST",
)

engine = create_engine(url_object, echo=False)

SessionMaker = sessionmaker(engine)