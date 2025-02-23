from WalletSystem import Walletsystem
import pytest as p

def test_initial_balance():
    wallet=Walletsystem()
    assert wallet.get_balance()==0

def test_add_funds():
    wallet=Walletsystem(100)
    assert wallet.add_funds(2000)
    assert wallet.get_balance()==2100

def test_make_payment():
    wallet=Walletsystem(10000)
    assert wallet.make_payment(5000)
    assert wallet.get_balance()==5000

def test_get_balance():
    wallet=Walletsystem(1000)
    assert wallet.get_balance()==1000

@p.mark.parametrize("initialBal,Deposite,paymentMade,expected",[(1000,1000,500,1500),(100,-100,50,50)])
def test_multiple_cases(initialBal,Deposite,paymentMade,expected):
    userWallet=Walletsystem(initialBal)
    userWallet.add_funds(Deposite)
    userWallet.make_payment(paymentMade)
    userWallet.get_balance()==expected

@p.fixture
def default_wallet():
    return Walletsystem(100)

def test_fixture_get_balance(default_wallet):
    assert default_wallet.get_balance()==100

def test_fixture_add_funds(default_wallet):
    assert default_wallet.add_funds(50)
    assert default_wallet.totalBalance==150

def test_transfer():
    sender=Walletsystem(100)
    receiver=Walletsystem(50)
    assert sender.transfer(30,receiver)
    assert sender.get_balance()==70
    assert receiver.get_balance()==80
    assert not sender.transfer(300,receiver)