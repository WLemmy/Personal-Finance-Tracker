from models import Category, Transaction
from datetime import date
from colorama import Fore, Style, init
from datetime import datetime
from tabulate import tabulate

init(autoreset=True)

purple = Fore.MAGENTA  # Define a new Fore color for purple

def create_category():
    name = input(Fore.YELLOW + 'Enter category name: ')
    category = Category.create(name)
    print(purple + f'Created category: {category}')
    headers = ["ID", "Name"]
    data = [[category.id, category.name]]  # Assuming the Category object has 'id' and 'name' attributes
    print( purple + tabulate(data, headers=headers, tablefmt="grid"))

def delete_category():
    category_id = int(input(Fore.YELLOW + 'Enter category ID to delete: '))
    category = Category.find_by_id(category_id)
    if category:
        Category.delete(category_id)
        print(purple + 'Category deleted.')
    else:
        print(purple + 'Category not found.')


def display_all_categories():
    categories = Category.get_all()
    headers = ["ID", "Name"]
    data = [[category.id, category.name] for category in categories]
    print(purple + tabulate(data, headers=headers, tablefmt="grid"))


def find_category_by_id():
    category_id = int(input(Fore.YELLOW + 'Enter category ID: '))
    category = Category.find_by_id(category_id)
    headers = ["ID", "Name"]
    if category:
        data = [[category.id, category.name]]
        print(purple + tabulate(data, headers=headers, tablefmt="grid"))
    else:
        print(purple + 'Category not found.')

def find_category_by_name():
    name = input(Fore.YELLOW + 'Enter category name: ')
    category = Category.find_by_name(name.lower())
    if category:
        print(purple + str(category))
    else:
        print(purple + 'Category not found.')

def create_transaction():
    while True:
        date_input = input(Fore.YELLOW + 'Enter date (YYYY-MM-DD): ')
        try:
            date_obj = datetime.strptime(date_input, '%Y-%m-%d').date()
            break
        except ValueError:
            print(Fore.RED + 'Invalid date format. Please enter the date in the format YYYY-MM-DD.')

    amount = float(input('Enter amount: '))
    category_id = int(input('Enter category ID: '))
    type_input = input('Enter type (income/expense): ')
    description = input('Enter description: ')
    
    # Convert type_input to lowercase
    type = type_input.lower()

    transaction = Transaction.create(date=date_obj, amount=amount, category_id=category_id, type=type, description=description)
    print(purple + f'Created transaction: {transaction}')

def delete_transaction():
    transaction_id = int(input(Fore.YELLOW + 'Enter transaction ID to delete: '))
    Transaction.delete(transaction_id)
    print(purple + 'Transaction deleted.')

def display_all_transactions():
    transactions = Transaction.get_all()
    headers = ["Date", "Amount", "Category", "Type", "Description"]
    data = [[transaction.date, transaction.amount, transaction.category.name, transaction.type, transaction.description] for transaction in transactions]
    print(purple + tabulate(data, headers=headers, tablefmt="grid"))

def find_transaction_by_id():
    transaction_id = int(input(Fore.YELLOW + 'Enter transaction ID: '))
    transaction = Transaction.find_by_id(transaction_id)
    if transaction:
        print(purple + str(transaction))
    else:
        print(purple + 'Transaction not found.')

def find_transaction_by_description():
    description = input(Fore.YELLOW + 'Enter transaction description: ')
    transaction = Transaction.find_by_description(description.lower())
    if transaction:
        print(purple + str(transaction))
    else:
        print(purple + 'Transaction not found.')

def display_total_categories():
    total = Category.total_categories()
    print(purple + f'Total number of categories: {total}')

def display_total_transactions():
    total = Transaction.total_transactions()
    print(purple + f'Total number of transactions: {total}')

def display_total_transactions_per_category():
    totals = Category.total_transactions_per_category()
    for category_name, total in totals:
        print(purple + f'Total transactions for category {category_name}: {total}')

