book_list={}
#func for adding new books
def add_books(title,author):
 book_list[title]=author

#func for remove a book
def remove_book(bName):
 if bName in book_list:
  bName.pop(bName)
 else:
  print(f"{bName} is not in book_list")

#show all books
def show_books():
 print(f"Book list: {book_list}")


