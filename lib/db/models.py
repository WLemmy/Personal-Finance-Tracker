from sqlalchemy import Column, Integer, String, Float, Date, Enum, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///practice-finance.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()