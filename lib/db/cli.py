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

if __name__ == '__main__':
    while True:
        print('1. Create Category')
        print('2. Delete Category')
        print('3. Display All Categories')
        print('4. Find Category by ID')
        print('5. Find Category by Name')
        print('6. Create Transaction')
        print('7. Delete Transaction')
        print('8. Display All Transactions')
        print('9. Find Transaction by ID')
        print('10. Find Transaction by Description')
        print('11. Display Total Categories')
        print('12. Display Total Transactions')
        print('13. Display Total Transactions Per Category')
        print('0. Exit')