import pytest 
from bank import Bankaccount
#Test case 01
def test_initial_balance():
    account=Bankaccount()
    assert account.total_balance==0
#Test case 02
def test_deposite():
    account=Bankaccount(1000)
    assert account.deposite(1000) #True
    assert account.get_balance()==2000 #True
#Test case 03
def test_withdraw_success():
    account=Bankaccount(500)
    assert account.withdraw(100)
    assert account.total_balance==400

#Test Case 04 
def test_withdraw_fail():
    account=Bankaccount(500)
    assert not account.withdraw(600) #False ,This will not allow withdraw
    assert account.get_balance()==500 #True

#For testing multiple testCases we use parametrize
@pytest.mark.parametrize("initial_bal,depositeAmnt,expectedbal",[(0,1000,1000),(1000,500,1500),(1000,-100,1000)])
def test_deposite_multiple_case(initial_bal,depositeAmnt,expectedbal):
    account=Bankaccount(initial_bal)
    account.deposite(depositeAmnt) # not return true ,false when negative bal ,so it doesn;t affect our testcase result
    assert account.get_balance()==expectedbal

#@pytest.fixture -- fixture provide a basic setup to use everytime (like data or object in our case)
@pytest.fixture
def default_account():
    return Bankaccount(1000) #will initial a account with initial balance 1000

def test_fixture_balance(default_account):
    assert default_account.get_balance()==1000 #using fixture ,not seperatly creating object

def test_fixture_deposite(default_account):
    default_account.deposite(500)
    assert default_account.get_balance()==1500