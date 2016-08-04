#Create three dictionaries: lloyd, alice, and tyler.
#mycode

lloyd = {"name": "Lloyd","homework": [],"quizzes": [],"tests": []}
alice = {"name": "Alice","homework": [],"quizzes" : [],"tests": []}
tyler ={"name": "Tyler","homework": [],"quizzes": [],"tests":[]}

#What's the Score?
#mycode
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

#Put It Together
students = [lloyd,alice,tyler]

#For the Record
for x in students:
    print x["name"]
    print x["homework"]
    print x["quizzes"]
    print x["tests"]