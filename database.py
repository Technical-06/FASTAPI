from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
password="Guruji@143"
DATABASE_URL = "mysql+mysqlconnector://root:"+password+"@localhost:3306/serversiderendering"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()