#Dictionary
student={
"name":"prashant",
"age":30,
"grade":"A"
}
print(student)
print(student["name"])
print(student["age"])
#print(student["school"]) 
print(student.get("school","Not found"))
student["school"]="high school"
student["grade"]="A+"
print(student)

removed_grade=student.pop("grade")
print("removed grade: ",removed_grade)

student.popitem()
print(student)

#iterating
for key in student:
 print(key,"->",student[key])
for key,value in student.items():
 print(f"{key}:{value}")
print(student.keys())
print(student.values())
print(student.items())
