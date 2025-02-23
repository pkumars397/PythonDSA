import os
if os.path.exists("textfile2.txt"):
    os.remove("textfile2.txt")
    print("File deleted successfully!")
else:
    print("file does not exist!")