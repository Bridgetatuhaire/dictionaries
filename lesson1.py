#dictionary sytax {key:value}
student = {
    "name": "Bridget",
    "age": 25,
    "address": "Makerere",
    "cohort": 3
}
print(type(student))
print(student)

#accessing the dictionary items
print(student["name"])
#for using get() function
print(student.get("name"))
#using keys()
print(student.keys())

