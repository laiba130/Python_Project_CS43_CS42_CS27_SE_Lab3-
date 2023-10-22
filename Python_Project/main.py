class LibraryCatalog:
    #From here partner a (Alina khan = NIM-BSCS-2021-42)
    def __init__(self):
        self.all_books_record =  {
    "The Great Gatsby": {
        "author_name": "F. Scott Fitzgerald",
        "publication_date": "10-01-1925",
        "status": "Available"
    },
    "To Kill a Mockingbird": {
        "author_name": "Harper Lee",
        "publication_date": "11-07-1960",
        "status": "Available"
    },
    "1984": {
        "author_name": "George Orwell",
        "publication_date": "08-06-1949",
        "status": "Available"
    },
    "Pride and Prejudice": {
        "author_name": "Jane Austen",
        "publication_date": "28-01-1813",
        "status": "Available"
    },
    "The Catcher in the Rye": {
        "author_name": "J.D. Salinger",
        "publication_date": "16-07-1951",
        "status": "Available"
    },
    "Moby-Dick": {
        "author_name": "Herman Melville",
        "publication_date": "18-10-1851",
        "status": "Available"
    },
    "The Hobbit": {
        "author_name": "J.R.R. Tolkien",
        "publication_date": "21-09-1937",
        "status": "Available"
    },
    "War and Peace": {
        "author_name": "Leo Tolstoy",
        "publication_date": "01-01-1869",
        "status": "Available"
    },
    "Brave New World": {
        "author_name": "Aldous Huxley",
        "publication_date": "01-01-1932",
        "status": "Available"
    },
    "The Lord of the Rings": {
        "author_name": "J.R.R. Tolkien",
        "publication_date": "29-07-1954",
        "status": "Available"
    },
     "The Alchemist": {
        "author_name": "Paulo Coelho",
        "publication_date": "01-01-1988",
        "status": "Available"
    },
    "The Road": {
        "author_name": "Cormac McCarthy",
        "publication_date": "26-09-2006",
        "status": "Available"
    },
    "The Shining": {
        "author_name": "Stephen King",
        "publication_date": "28-01-1977",
        "status": "Available"
    },
    "Frankenstein": {
        "author_name": "Mary Shelley",
        "publication_date": "01-01-1818",
        "status": "Available"
    },
    "The Da Vinci Code": {
        "author_name": "Dan Brown",
        "publication_date": "18-03-2003",
        "status": "Available"
    },
    "The Grapes of Wrath": {
        "author_name": "John Steinbeck",
        "publication_date": "14-04-1939",
        "status": "Available"
    },
    "The Hitchhiker's Guide to the Galaxy": {
        "author_name": "Douglas Adams",
        "publication_date": "12-10-1979",
        "status": "Available"
    },
    "The Handmaid's Tale": {
        "author_name": "Margaret Atwood",
        "publication_date": "01-01-1985",
        "status": "Available"
    },
    "The Kite Runner": {
        "author_name": "Khaled Hosseini",
        "publication_date": "01-01-2003",
        "status": "Available"
    },
    "The Picture of Dorian Gray": {
        "author_name": "Oscar Wilde",
        "publication_date": "01-01-1890",
        "status": "Available"
    },
    "The Martian": {
        "author_name": "Andy Weir",
        "publication_date": "02-03-2014",
        "status": "Available"
    },
    "The Stranger": {
        "author_name": "Albert Camus",
        "publication_date": "01-01-1942",
        "status": "Available"
    },
    "The Adventures of Sherlock Holmes": {
        "author_name": "Arthur Conan Doyle",
        "publication_date": "14-10-1892",
        "status": "Available"
    },
    "The Sun Also Rises": {
        "author_name": "Ernest Hemingway",
        "publication_date": "01-01-1926",
        "status": "Available"
    },
    "The Silence of the Lambs": {
        "author_name": "Thomas Harris",
        "publication_date": "01-01-1988",
        "status": "Available"
    },
    "The Color Purple": {
        "author_name": "Alice Walker",
        "publication_date": "01-01-1982",
        "status": "Available"
    },
    "The Help": {
        "author_name": "Kathryn Stockett",
        "publication_date": "10-02-2009",
        "status": "Available"
    },
    "The Old Man and the Sea": {
        "author_name": "Ernest Hemingway",
        "publication_date": "01-09-1952",
        "status": "Available"
    },
    "The Secret Garden": {
        "author_name": "Frances Hodgson Burnett",
        "publication_date": "01-01-1911",
        "status": "Available"
    },
    "The Catcher in the Rye": {
        "author_name": "J.D. Salinger",
        "publication_date": "16-07-1951",
        "status": "Available"
    },
    "Dune": {
        "author_name": "Frank Herbert",
        "publication_date": "01-06-1965",
        "status": "Available"
    },
    "The Brothers Karamazov": {
        "author_name": "Fyodor Dostoevsky",
        "publication_date": "12-11-1880",
        "status": "Available"
    },
    "The Road Not Taken": {
        "author_name": "Robert Frost",
        "publication_date": "01-01-1916",
        "status": "Available"
    },
    "Crime and Punishment": {
        "author_name": "Fyodor Dostoevsky",
        "publication_date": "01-01-1866",
        "status": "Available"
    },
    "The Picture of Dorian Gray": {
        "author_name": "Oscar Wilde",
        "publication_date": "01-01-1890",
        "status": "Available"
    },
    "The Martian": {
        "author_name": "Andy Weir",
        "publication_date": "02-03-2014",
        "status": "Available"
    },
    "The Stranger": {
        "author_name": "Albert Camus",
        "publication_date": "01-01-1942",
        "status": "Available"
    },
    "The Adventures of Sherlock Holmes": {
        "author_name": "Arthur Conan Doyle",
        "publication_date": "14-10-1892",
        "status": "Available"
    },
    "The Sun Also Rises": {
        "author_name": "Ernest Hemingway",
        "publication_date": "01-01-1926",
        "status": "Available"
    },
    "The Silence of the Lambs": {
        "author_name": "Thomas Harris",
        "publication_date": "01-01-1988",
        "status": "Available"
    },
    "The Color Purple": {
        "author_name": "Alice Walker",
        "publication_date": "01-01-1982",
        "status": "Available"
    },
    "The Help": {
        "author_name": "Kathryn Stockett",
        "publication_date": "10-02-2009",
        "status": "Available"
    },
    "The Old Man and the Sea": {
        "author_name": "Ernest Hemingway",
        "publication_date": "01-09-1952",
        "status": "Available"
    },
    "The Secret Garden": {
        "author_name": "Frances Hodgson Burnett",
        "publication_date": "01-01-1911",
        "status": "Available"
    },
    "The Catcher in the Rye": {
        "author_name": "J.D. Salinger",
        "publication_date": "16-07-1951",
        "status": "Available"
    },
    "One Hundred Years of Solitude": {
        "author_name": "Gabriel García Márquez",
        "publication_date": "30-05-1967",
        "status": "Available"
    },
    "The Lord of the Flies": {
        "author_name": "William Golding",
        "publication_date": "17-09-1954",
        "status": "Available"
    },
    "Lord of the Rings: The Fellowship of the Ring": {
        "author_name": "J.R.R. Tolkien",
        "publication_date": "29-07-1954",
        "status": "Available"
    },
    "The Road": {
        "author_name": "Cormac McCarthy",
        "publication_date": "26-09-2006",
        "status": "Available"
    },
    "Fahrenheit 451": {
        "author_name": "Ray Bradbury",
        "publication_date": "01-10-1953",
        "status": "Available"
    },
    "Les Misérables": {
        "author_name": "Victor Hugo",
        "publication_date": "03-04-1862",
        "status": "Available"
    },
    "The Odyssey": {
        "author_name": "Homer",
        "publication_date": "01-01-8th Century BCE",
        "status": "Available"
    },
    "The Scarlet Letter": {
        "author_name": "Nathaniel Hawthorne",
        "publication_date": "16-03-1850",
        "status": "Available"
    },
    "The Great Expectations": {
        "author_name": "Charles Dickens",
        "publication_date": "01-01-1861",
        "status": "Available"
    },
        }
        self.checkout_history = []
        
    #  #Partner b (Laiba Fatima = NIM-BSCS-2021-43) had done her part here

    # def book_addition(self):
    #     """
    #     Add new book in library stock
    #     :return: None
    #     """
    #     book_name = input("Enter new book name: ")

    #     book_found_flag = False
    #     for book in self.all_books_record:
    #         if book.title() == book_name.title():
    #             book_found_flag - True
    #             print("This book is already present in library")
    #             break
    #     else:
    #         if book_found_flag is False:
    #             self.all_books_record[book_name.title()] = {}
    #             author_name = input("Enter author name: ")
    #             self.all_books_record[book_name.title()]["author_name"] = author_name.title()
    #             publication_date = input("Enter publication date (DD-MM-YYYY): ")
    #             self.all_books_record[book_name.title()]["publication_date"] = publication_date
    #             self.all_books_record[book_name.title()]["status"] = "Available"


    # def book_checkout(self):
    #     """
    #     Help in checking out any book
    #     :return: NOne
    #     """
    #     book_name = input("Enter book name: ")

    #     book_found_flag = False
    #     for book in self.all_books_record:
    #         if book_name.title() == book:
    #             book_found_flag = True
    #             if self.all_books_record[book]["status"] == "Available":
    #                 print("This book is issued to you")
    #                 self.all_books_record[book]["status"] = "Issued"
    #                 name = input("Enter your name please")
    #                 self.checkout_history.append(f"{book} issued by {name}")
    #                 break
    #             else:
    #                 print("Sorry, this book is already issued to someone else")
    #                 break
    #     else:
    #         if book_found_flag is False:
    #             print("Sorry, this book is not in library")

    # def return_book(self):
    #     """
    #     Help in returning any book
    #     :return: NOne
    #     """
    #     book_name = input("Enter book name: ")

    #     book_found_flag = False
    #     for book in self.all_books_record:
    #         if book == book_name.title():
    #             book_found_flag = True
    #             if self.all_books_record[book]["status"] == "Issued":
    #                 name = input("Enter your name: ")
    #                 self.checkout_history.append(f"{book} returned by {name}")
    #                 self.all_books_record[book]["status"] = "Available"
    #                 print("Thanks for choosing us")
    #             else:
    #                 print("This book is already present in library.")
    #             break
    #     else:
    #         if book_found_flag is False:
    #             print("This book is not from our libray")

    # def book_reservation(self):
    #     """
    #     Help in reserving any book
    #     :return: None
    #     """
    #     book_name = input("Enter book name: ")

    #     book_found_flag = False
    #     for book in self.all_books_record:
    #         if book == book_name.title():
    #             print(f"Current status of book = {self.all_books_record[book]['status']}")
    #             if self.all_books_record[book]["status"] == "Available":
    #                 print("This book is available, you can issue it now if you want, instead of reserving")
    #             else:
    #                 print("Book is reserved for you")
    #             self.all_books_record[book]["status"] = "Reserved"


    # def book_information(self):
    #     """
    #     Help in showing book information
    #     :return: None
    #     """
    #     book_name = input("Enter book name: ")

    #     book_found_flag = False
    #     for book in self.all_books_record:
    #         if book_name.title() == book:
    #             book_found_flag = True
    #             print(f""" Book name = {book}
    #     Author name = {self.all_books_record[book]["author_name"]}
    #     Publication Date = {self.all_books_record[book]["publication_date"]}
    #     Current status = {self.all_books_record[book]["status"]}""")
    #     else:
    #         if book_found_flag is False:
    #             print("This book is not in our library")