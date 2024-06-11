from models import Category, Transaction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

engine = create_engine('sqlite:///finance_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()