try:
  file=open("textfile.txt","r")
  content=file.read()
  file.close()
  print("file content: ",content)
except FileNotFoundError:
  print("Error! file doesn't exit! ")