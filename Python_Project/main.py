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