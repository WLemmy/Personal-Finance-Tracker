from helpers import (
    create_category,
    delete_category,
    display_all_categories,
    find_category_by_id,
    find_category_by_name,
    create_transaction,
    delete_transaction,
    display_all_transactions,
    find_transaction_by_id,
    find_transaction_by_description,
    display_total_categories,
    display_total_transactions,
    display_total_transactions_per_category,
    
)
from colorama import init, Fore, Style

init(autoreset=True)

def print_menu():
    print(Fore.GREEN + '1. Create Category')
    print(Fore.GREEN + '2. Delete Category')
    print(Fore.GREEN + '3. Display All Categories')
    print(Fore.GREEN + '4. Find Category by ID')
    print(Fore.GREEN + '5. Find Category by Name')
    print(Fore.GREEN + '6. Create Transaction')
    print(Fore.GREEN + '7. Delete Transaction')
    print(Fore.GREEN + '8. Display All Transactions')
    print(Fore.GREEN + '9. Find Transaction by ID')
    print(Fore.GREEN + '10. Find Transaction by Description')
    print(Fore.GREEN + '11. Display Total Categories')
    print(Fore.GREEN + '12. Display Total Transactions')
    print(Fore.GREEN + '13. Display Total Transactions per Category')
    print(Fore.RED + '0. Exit')


if __name__ == '__main__':
     while True:
        print_menu()
        choice = input(Fore.YELLOW + 'Choose an option: ')
        if choice == '1':
            create_category()
        elif choice == '2':
            delete_category()
        elif choice == '3':
            display_all_categories()
        elif choice == '4':
            find_category_by_id()
        elif choice == '5':
            find_category_by_name()
        elif choice == '6':
            create_transaction()
        elif choice == '7':
            delete_transaction()
        elif choice == '8':
            display_all_transactions()
        elif choice == '9':
            find_transaction_by_id()
        elif choice == '10':
            find_transaction_by_description()
        elif choice == '11':
            display_total_categories()
        elif choice == '12':
            display_total_transactions()
        elif choice == '13':
            display_total_transactions_per_category()
        elif choice == '0':
            print(Fore.CYAN + 'Goodbye! ✋🏼')
            break
        else:
            print(Fore.RED + 'Invalid choice. Please try again.')
       

        