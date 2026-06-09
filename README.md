Task Tracker CLI

A simple command-line task manager built with Python and SQLite.

Features

* Add tasks
* View all tasks
* Mark tasks as completed
* Delete tasks
* Persistent storage using SQLite
* Input validation for user commands

Technologies

* Python 3
* SQLite3

Project Structure

project/
│
├── main.py
├── tasks_service.py
├── db.py
└── tasks.db

Files

* main.py — command-line interface and menu.
* tasks_service.py — task management logic.
* db.py — database connection and table creation.
* tasks.db — SQLite database file.

How to Run

1. Clone the repository:

git clone <repository-url>

2. Open the project directory:

cd task-tracker-cli

3. Run the application:

python main.py

Available Commands

Command Description
1 Add a task
2 Show all tasks
3 Mark a task as completed
4 Delete a task
0 Exit the application

Learning Goals

This project was created to practice:

* Python functions
* Modular project structure
* SQLite basics
* CRUD operations
* Error handling
* Working with user input
