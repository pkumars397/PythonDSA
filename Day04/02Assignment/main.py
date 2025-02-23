from books import add_books,remove_book,show_books
from borrow import borrowBooks,bookReturning
from library_system.users import registerUsers,show_users
from library_system.fines import fineAmount

add_books("untouchable","indian author")
add_books("Prejuidce","Jane")
add_books("Westland","T S elliot")
#show books details
show_books()

#register users
registerUsers("Prashant Kumar")
registerUsers("Binu")
show_users()

#Borrow and return
borrowBooks("unkown people")
borrowBooks("Westland")
show_books()

bookReturning("Westland","T S elliot")
show_books()

#calculate_fines:
print(fineAmount(5))
