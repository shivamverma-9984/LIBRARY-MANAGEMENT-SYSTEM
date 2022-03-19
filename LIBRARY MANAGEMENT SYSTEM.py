
class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def show_available_books(self):
        print(f"\n{len(self.books)}  BOOKS ARE AVAILABLE: ")
        for book in self.books:
            print(" *) " + book)
        print("\n")

    def borrow_book(self, name, book_name):
        if book_name not in self.books:
            print(
                f"{book_name} BOOK IS NOT AVAILABLE EITHER TAKEN BY SOMEONE ELSE, WAIT UNTIL HE RETURNED.\n")
        else:
            track.append({name: book_name})
            print("BOOK ISSUED : THANK YOU KEEP IT WITH CARE AND RETURN ON TIME.\n")
            self.books.remove(book_name)

    def return_Book(self, book_name):
        print("BOOK RETURNED : THANK YOU! \n")
        self.books.append(book_name)

    def donateBook(self, book_name):
        print("BOOK DONATED : THANK YOU VERY MUCH, HAVE A GREAT DAY AHEAD.\n")
        self.books.append(book_name)


class st():
    def requet_for_book(self):
        print("So, you want to borrow book!")
        self.book = input("Enter name of the book you want to borrow: ")
        return self.book

    def return_Book(self):
        print("So, you want to return book!")
        name = input("Enter your name: ")
        self.book = input("Enter name of the book you want to return: ")
        if {name: self.book} in track:
            track.remove({name: self.book})
        return self.book

    def donateBook(self):
        print("Okay! you want to doante book!")
        self.book = input("Enter name of the book you want to donate: ")
        return self.book


if __name__ == "__main__":

    library_book = Library(
        ["Python programming", "C++ programming","Java programming","C programming","DBMS ", "Operating system","Compiler Design"])
    student = st()
    track = []
    
    print("\n\n\t\t\t\t♦♦♦♦♦♦♦ WELCOME TO THE LIBRARY ♦♦♦♦♦♦♦\n")
    print("""CHOOSE THE OPTION YOU WANT :-\n1. Listing of Available books\n2. Borrow books\n3. Return books\n4. Donate books\n5.Track books\n6. exit the library\n""")

    while (True):
        try:
            response = int(input("Enter the choice: "))

            if response == 1: 
                library_book.show_available_books()
            elif response == 2: 
                library_book.borrow_book(
                    input("Enter your name: "), student.requet_for_book())
            elif response == 3:  
                library_book.return_Book(student.return_Book())
            elif response == 4:  
                library_book.donateBook(student.donateBook())
            elif response == 5: 
                for i in track:
                    for K, V in i.items():
                        H = K
                        book = V
                        print(f"{book} book is taken/issuedby {H}.")
                print("\n")
                if len(track) == 0:
                    print("NO BOOKS ARE ISSUED!. \n")
            
            elif response == 6: 
                print("THANK YOU ! \n")
                exit()
            else:
                print("INVAILD INPUT! \n")
        except Exception as e:              
            print(f"{e}---> INVALID INPUT! \n")