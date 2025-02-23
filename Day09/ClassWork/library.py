class Library:
    def __init__(self):
        self.books={
        "Python 101":3,
        "AI Basics":2,
        "Data Science":5
        }
    def borrow_book(self,book_name):
        if book_name in self.books and self.books[book_name]>0:
            self.books[book_name]-=1
            return f"Borrowed {book_name}"
        return "Book Not Available"
    
    def return_book(self,book_name):
        if book_name in self.books:
            self.books[book_name]+=1
            return f"Returned {book_name}"
        return "Book Not Available"
    
    def check_availability(self,book_name):
        return self.books.get(book_name,0)