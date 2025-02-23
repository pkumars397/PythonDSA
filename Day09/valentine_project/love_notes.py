class LoveNotesValidator:
    def __init__(self):
        self.listOfNotes={}
    def add_love_note(self,sender,recipient,msg):
        if (sender,recipient) not in self.listOfNotes:
            self.listOfNotes[(sender,recipient)]=msg
            return True
        else:
            return False
        
    def validate_note(self,sender,recipient,msg):
        if (sender,recipient) in self.listOfNotes:
            if self.listOfNotes[(sender,recipient)]==msg:
                return (f"Love Note is valid! Message: {self.listOfNotes[(sender,recipient)]}")
            else:
                return (f"FAKE LOVE NOTE ALERT! Message doesn't match")
        else:
            return (f"FAKE LOVE NOTE ALERT! Sender does not match")

    def list_love_notes(self):
       for key in self.listOfNotes: #(sender,recipient)
            print(f"{key[0]} sended love note to {key[1]} and message is {self.listOfNotes[key]}")
       return True

love1=LoveNotesValidator()
love1.add_love_note("John","Emily","You are my sunshine!")
love1.add_love_note("John","Emily","You are my sunshine!")
print(love1.listOfNotes)
print(love1.validate_note("John","Emily","You are my sunshine!"))
print(love1.validate_note("Jake","Emily","You are my sunshine!"))

love1.add_love_note("Alice","Davie","You make my heart skip a beat!")
print(love1.validate_note("Alice","Davie","You are my soulamte!"))

love1.list_love_notes()

print(love1.listOfNotes)