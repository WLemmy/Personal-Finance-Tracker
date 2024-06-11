from sqlalchemy import Column, Integer, String, Float, Date, Enum, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///finance_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    transactions = relationship('Transaction', backref='category')

    @classmethod
    def create(cls, name):
        category = cls(name=name)
        session.add(category)
        session.commit()
        return category
    
    @classmethod
    def delete(cls, category_id):
        category = session.query(cls).get(category_id)
        if category:
            session.delete(category)
            session.commit()

    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, category_id):
        return session.query(cls).get(category_id)
    
    @classmethod
    def find_by_name(cls, name):
        lowercase_name = name.lower()
        return session.query(cls).filter(func.lower(cls.name) == lowercase_name).first()

    
    @classmethod
    def total_categories(cls):
        return session.query(func.count(cls.id)).scalar()

    @classmethod
    def total_transactions_per_category(cls):
        return session.query(cls.name, func.count(Transaction.id)).join(Transaction).group_by(cls.name).all()


    def __repr__(self):
        return f'<Category(id={self.id}, name={self.name})>'

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    type = Column(Enum('income', 'expense', name='transaction_type'), nullable=False)
    description = Column(String)
    
    @classmethod
    def create(cls, date, amount, category_id, type, description):
        transaction = cls(date=date, amount=amount, category_id=category_id, type=type, description=description)
        session.add(transaction)
        session.commit()
        return transaction
    
    @classmethod
    def delete(cls, transaction_id):
        transaction = session.query(cls).get(transaction_id)
        if transaction:
            session.delete(transaction)
            session.commit()

    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, transaction_id):
        return session.query(cls).get(transaction_id)
    
    @classmethod
    def find_by_description(cls, description):
        return session.query(cls).filter(cls.description.ilike(f'%{description}%')).first()
    
    @classmethod
    def total_transactions(cls):
        return session.query(func.count(cls.id)).scalar()
    
    def __repr__(self):
        return f'<Transaction(id={self.id}, date={self.date}, amount={self.amount}, category={self.category.name}, type={self.type}, description={self.description})>'