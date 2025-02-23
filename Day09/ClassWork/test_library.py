import pytest 
from library import Library

#created fixute for using this obj .
@pytest.fixture
def library():
    return Library()

@pytest.mark.parametrize("book,expected",[("Python 101","Borrowed Python 101"),("AI Basics","Borrowed AI Basics"),("Unkown book","Book Not Available")])

def test_mul_borrow_book(library,book,expected):
    assert library.borrow_book(book)==expected
