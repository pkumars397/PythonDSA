import json
myjsonfile=open("example.json","r")
jsonData=myjsonfile.read()
print(jsonData,type(jsonData)) #string 

#Reading data from jsonfile
obj=json.loads(jsonData)

print(str(obj['firstName']),type(obj))

list=obj['Address']
print(f"{list} length : {len(list)}")
print(list[0]["street"])