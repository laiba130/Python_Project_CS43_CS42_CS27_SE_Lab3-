# parnter c = Amina Ahmad (NIM-BSCS-2021-27) part:
def main():
    """
    A user interface
    :return: None
    """
    book = LibraryCatalog()
    while True:
        print(""" Instructions:
        1. for new book addition in library
        2. For checking out any book
        3. For returning any book
        4. For reserving any book
        5. For getting any book information
        6. Exit""")
        try:
            user_choice = int(input("Enter your choice: "))
        except Exception as a:
            print("Value Error. Enter only integer numbers. Try Again!")
        else:
            if user_choice == 1:
                book.book_addition()
            elif user_choice == 2:
                book.book_checkout()
            elif user_choice == 3:
                book.return_book()
            elif user_choice == 4:
                book.book_reservation()
            elif user_choice == 5:
                book.book_information()
            elif user_choice == 6:
                break
            else:
                print("Enter number only of given options.")


main()
