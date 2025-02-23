#Doremon Task
import sys 
try:
 if len(sys.argv)>1:
  with open("doraemon_gadgets.txt","a") as file:
    for items in sys.argv[1:]:
      file.write(f"{items}\n")
 else:
     raise ValueError("Please enter gadgets! ")
except ValueError as e:
    print(e)
else:
    print("📃 Doraemon's Gadget List 📃")
    print("------------------------------")
    try:
     with open("doraemon_gadgets.txt","r") as file:
      for line in file:
        print(line)
     print("Gadgets saved successfully 🚀")
    except FileNotFoundError:
        print("File is not there!")
    print("-------------------------------")
    