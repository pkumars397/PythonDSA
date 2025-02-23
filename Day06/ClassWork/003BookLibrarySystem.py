class Library:
    def __init__(self):
        self.books=[]
    def display_books(self):
        if not len(self.books):
            print("No books in the library")
        else:
            print("Available books in the library")
            for book in self.books:
                print(f"{book}")
    def add_book(self,bookName):
        self.books.append(bookName)
        print(f"{bookName} has been added to the library")
    def borrow_books(self,bookName):
        if bookName in self.books:
            self.books.remove(bookName)
            print(f"You have borrowed {bookName}.Please return it soon")
        else:
            print(f"Sorry {bookName} is not available or already borrowed")
    def return_book(self,bookName):
        self.books.append(bookName)
        print(f"Thank you for returning {bookName}")

lib1=Library() #will create a books list as attribute of lib1
lib1.add_book("Python DSA")
lib1.add_book("DSA")
lib1.display_books()

lib1.borrow_books("Python DSA")
lib1.borrow_books("Python DSA") #will not allow borrow cause this book already borrowed
lib1.display_books()

lib1.return_book("Python DSA")
lib1.display_books()