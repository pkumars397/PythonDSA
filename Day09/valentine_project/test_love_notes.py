import pytest 
from love_notes import LoveNotesValidator

@pytest.fixture
def default_loveList():
    return LoveNotesValidator()

#testcase01
def test_love_note1(default_loveList):
    assert default_loveList.add_love_note("binu","swati","You are my sunshine")==True
    assert default_loveList.validate_note("binu","swati","You are my sunshine")=="Love Note is valid! Message: You are my sunshine"

#testcase02
def test_love_note2(default_loveList):
    assert default_loveList.add_love_note("John","Emily","You are my sunshine")==True
    assert default_loveList.validate_note("jake","Emily","You are not my sunshine")=="FAKE LOVE NOTE ALERT! Sender does not match"
#testcase03
def test_love_note3(default_loveList):
    assert default_loveList.add_love_note("Alice","David","You skips my heart a beat!")==True
    assert not default_loveList.validate_note("Alice","David","You are my soulmate")=="FAKE LOVE NOTE ALERT! Message doesn't Match"

@pytest.mark.parametrize("sender,recipient,msg",[("John","Emily","You are my sunshine"),("Alice","David","You make my heart skip a beat")])

#Test Case 3 and 4
def test_multiple_cases(default_loveList,sender,recipient,msg):
    assert default_loveList.add_love_note(sender,recipient,msg)==True 
    assert default_loveList.validate_note("Prashant","Emily","You are not my sunshine")=="FAKE LOVE NOTE ALERT! Sender does not match"
    