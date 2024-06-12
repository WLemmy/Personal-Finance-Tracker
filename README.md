# Personal-Finance-Tracker
## Introduction
This is a simple personal finance tracker application built using Python and SQLite. The Personal Finance Tracker CLI simplifies the task of tracking income and expenses, categorizing transactions, and generating financial summaries, all from a command-line interface. This tool is designed to be user-friendly, efficient, and powerful, allowing users to stay on top of their finances effortlessly.

## Minimum Viable Product(MVP)
The MVP of the Personal Finance Tracker CLI includes core functionalities that allow users to manage their finances effectively. 

## Features
- Create Category: Users can add new categories to organize their transactions.
- Delete Category: Users can remove categories that are no longer needed.
- Display All Categories: Users can view a list of all existing categories.
- Find Category by ID: Users can search for a specific category using its unique ID.
- Find Category by Name: Users can search for a specific category by its name.
- Create Transaction: Users can log new income or expense transactions, specifying details such as date, amount, category, type (income/expense), and description.
- Delete Transaction: Users can remove transactions that are no longer relevant.
- Display All Transactions: Users can view all recorded transactions.
- Find Transaction by ID: Users can search for a specific transaction using its unique ID.
- Find Transaction by Description: Users can search for transactions based on their description.
- Display total transaction amout
- Display total transaction amount per category.

## Objectives
- To create a user-friendly command-line interface for managing personal finances.
- Create categories that help users classify their financial transactions for better tracking and analysis.
- Delete outdated or unused categories to keep their financial records clean and relevant.
- Allow users to view a comprehensive list of all their categories, making it easier to manage and utilize them effectively.
- Allow users to quickly locate a specific category using its unique identifier, streamlining the process of managing transactions.
- Enable users to find categories by name, making it simpler to locate and manage categories.
- Create Transactions to allow users to easily log income and expense transactions with relevant details, ensuring accurate and comprehensive financial records.
- Enable users to remove transactions that are no longer relevant, ensuring that their financial data remains accurate and current.
- Allow users to view all recorded transactions, giving them a clear picture of their financial activities.
- Allow users to quickly locate specific transactions using unique identifiers, facilitating easy management and review.
- Enable users to find transactions based on descriptions, making it easier to track and review specific financial activities.
- Display total transaction amount to give users a clear overview of their financial situation.
- Display total transaction amount per category to help users understand their spending habits and make informed financial decisions.

## Technologies used
- Python: The primary programming language used for developing the Personal Finance Tracker CLI.
- [SQLite](https://www.sqlite.org/index.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Colorama](https://pypi.org/project/colorama/)
- [Tabulate](https://pypi.org/project/tabulate/)
- [Datetime](https://docs.python.org/3/library/datetime.html)
- [Git](https://www.git-scm.com/)

## Get Started
1. Clone the repository
```bash
git@github.com:WLemmy/Personal-Finance-Tracker.git 
```
2. Install dependencies and create a virtual environment
```bash
 pipenv install 
 ```
 3.Enter the virtual environment
 ```bash
 pipenv shell 
 ```
 4. Run the application
 ```bash
 python lib/db/cli.py 
 ```
 5. Follow the prompts to interact with the application

 ## Requirements
- Programming knowledge, Python, SQL
- Visual Studio as code editor
- SQLite for database management
- SQLAlchemy for database operations
- Colorama for colorful output
- Tabulate for table formatting
- Datetime for date and time operations
- Git for version control

## Contributions
Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

## Author
- [Wilfred Ketere](https://github.com/WLemmy)
- [Morris Mburu](https://github.com/mrrsmburu)
- [Lewis Wambugu](https://github.com/Wambuguu)
- [Sylvia Chebet](https://github.com/SylviaT01)

## Copyright and License Information
The project is licensed under [MIT License](LICENSE)






