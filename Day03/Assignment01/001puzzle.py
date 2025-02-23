#puzzle
clues_found={"key","map","torch","key","note","map","compass","torch"}
puzzle_codes=(312,789,456,123,654,789)
secret_symbols={"@","#","$","&","%","@"}
lock_mechanisms={"Alpha Lock":"312","Beta Lock":"torch","Gamma Lock":"@","Delta Lock":"golden_key"}
#1 unique clues
print(f"Unique Clues: {set(clues_found)}")

#2 verify puzzle code
code=int(input("Enter your puzzle code: "))
if code in puzzle_codes:
  print("Valid Code")
else:
  print("Invalid code")
  
#3 compare clues with locks
unique_clues=set(clues_found)
for key in unique_clues:
  for k,value in lock_mechanisms.items():
    if value==key:
     print(f"{k} -> {key}")
     
#4 match screte symbols
ss=set(secret_symbols)
for key in ss:
 for k,v in lock_mechanisms.items():
  if key==v:
   print(f"{k}->>{key}")

#5 update clue list
if "golden_key" not in unique_clues:
 unique_clues.add("golden_key")
print(unique_clues)

#6 final unlock
count=0
for k,v in lock_mechanisms.items():
 if v in unique_clues or v in puzzle_codes or v in secret_symbols:
  count+=1
if count>=3:
 print("Escape Successful!")
else:
 print("Still locked! find more clues!")
