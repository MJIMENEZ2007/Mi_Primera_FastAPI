from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "mysql+pymysql://aaa2f3_marco:infoplus1234@mysql8010.site4now.net:3306/db_aaa2f3_marco"
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit= False , autoflush=False, bind=engine)
Base = declarative_base()