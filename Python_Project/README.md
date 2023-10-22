# Library Catalog Python Project

## Overview
This Python project is a terminal-based library catalog system that allows users to manage a collection of books. The program includes functionalities for adding new books to the library, checking out books, returning books, reserving books, and obtaining information about specific books. It is designed as a collaborative project to demonstrate Git version control.

## Team Members
- Alina Khan (NIM-BSCS-2021-42): Implemented the initial project setup and provided the basic structure. 
- Laiba Fatima (NIM-BSCS-2021-43): Added key functions for book management, including adding, checking out, returning, and reserving books.
- Amina Ahmad (NIM-BSCS-2021-27): Contributed to conflict resolution and ensuring code consistency.

## Code Details

### Initialization (Alina Khan)
- Created the project structure and initialized the Git repository.
- Added the initial Python script, which serves as the entry point for the program.
- Performed the project setup and version control management.

### Book Management Functions (Laiba Fatima)
- Implemented functions for adding, checking out, returning, and reserving books in the library.
- Ensured proper book data storage and management within the code.
- Validated user inputs and managed the library's status accordingly.

### Conflict Resolution (Amina Ahmad)
- Worked on conflict resolution when team members made changes to the same parts of the code in different branches.
- Ensured that code changes were merged smoothly to maintain code consistency.

## Usage
This is a terminal-based program, and there is no graphical user interface. Users can interact with the program by running the `main.py` script.

The program offers the following options:

1. **Add a new book to the library:** Utilizing the `book_addition` function, this feature allows users to add new books to the library catalog, including author details and publication dates.

2. **Check out a book:** With the `book_checkout` function, users can check out available books. The program tracks book status and records the borrower's name.

3. **Return a book:** Using the `return_book` function, users can return books they've checked out. The program updates the book's status and acknowledges returns.

4. **Reserve a book:** The `book_reservation` function allows users to reserve books in the catalog. It updates the book's status to "Reserved."

5. **Get information about a book:** Through the `book_information` function, users can access detailed information about any book in the library, including the author, publication date, and current status.

6. **Exit the program:** Allows users to exit the program when their tasks are completed.

The program's functionalities are implemented using these functions, and it's designed for smooth library catalog management.


Follow the on-screen instructions to perform these actions. The program's functionalities are implemented according to the code details mentioned above.

## Project Structure
- `main.py`: The entry point of the program.
- `README.md`: This document, providing project information.
- Other project files and Python code for library catalog functionality.

Feel free to explore the project, collaborate, and further improve its functionality as needed.
