from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timezone
import pytz
from config import DB_PATH 

DATABASE_URL = f"sqlite:///{DB_PATH}"
ua_tz = pytz.timezone('Europe/Kiev')

engine = create_engine(DATABASE_URL)
Base = declarative_base()

class JobData(Base):
    __tablename__ = 'job_data'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    parsed_at = Column(DateTime(timezone=True), default=lambda: datetime.now(ua_tz))
    vacancy_count = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
