students = ["Hermione","Harry","Ron"]

for student in students:
    print(student)

for i in range(len(students)):
    print(i+1,students[i])

houses = ["Gryffindor","Gryffindor","Gryffindor","Slytherin"]

DirAlum = {
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin"
}

for s in DirAlum:
    print(s,DirAlum[s],sep=" - ")

studiantes = [
    {"name":"Hermione","house":"Griffindor","Patronus":"Otter"},
    {"name":"Harry","house":"Griffindor","Patronus":"Stag"},
    {"name":"Ron","house":"Griffindor","Patronus":"Jack Russell terrier"},
    {"name":"Draco","house":"Slytherin","Patronus":None}
]
for estudiante in studiantes:
    print(estudiante["name"],estudiante["house"],estudiante["Patronus"], sep=" - ")

