from books import book_list

#borrowing books
def borrowBooks(bName):
 if bName in book_list:
   del book_list[bName]
 else:
   print(f"{bName} is not in library")
   
#returning book
def bookReturning(bName,author):
 book_list[bName]=author


