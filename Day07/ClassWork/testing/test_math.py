import pytest
def add(a,b):
    return (a+b)
#Test case1
def test_add():
    assert add(3,4)==7
    assert add(3,7)==10
    assert add(3,8)==11

#multiple test cases
@pytest.mark.parametrize("a,b,expected",[(3,5,8),(56,4,60),(34,5,39)])
def test_multiple_cases(a,b,expected):
    assert add(a,b)==expected
