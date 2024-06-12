from models import Category, Transaction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

print("🌱 Seeding..")

engine = create_engine('sqlite:///finance_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

categories = [
    Category(name='Food'),
    Category(name='Utilities'),
    Category(name='Entertainment'),
    Category(name='Salary'),
]

session.add_all(categories)
session.commit()

transactions = [
    Transaction(date=date(2024, 6, 5), amount=1000, category_id=categories[3].id, type='income', description='Monthly salary'),
    Transaction(date=date(2024, 6, 6), amount=50, category_id=categories[0].id, type='expense', description='Groceries'),
]

session.add_all(transactions)
session.commit()

print("🌱 Seeding complete!")