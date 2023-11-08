# Student Database Management Program

Python program for managing a student database using SQLite. It provides a menu-driven interface to perform operations such as importing data from a CSV file, printing student records, updating student information, soft-deleting students, and searching for students by different criteria.

## Program Features

The program will display a menu with the following options:
- Import Data: To import student data from a CSV file.
- Print Data: Print all non-deleted students.
- Update Student: To update the field of a specific student, given an ID.
- Soft Delete Student: Change the `isDeleted` field to 1.
- Search Students: Search for students by major, GPA, city, state, or advisor.
- Quit: EXIT.

## Program Structure

The program is organized into a class-based structure for better modularity and maintainability. The `StudentDatabase` class represents the database and encapsulates methods for data operations. You can find the database connection setup, data manipulation methods, and the main menu within the class.

## Contributions

- [GeeksforGeeks - Encapsulation in Python](https://www.geeksforgeeks.org/encapsulation-in-python/)

