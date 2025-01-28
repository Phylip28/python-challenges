class students:

    def __init__(self):
        self.studentsList = {}

    def addStudent(self, name, age, course):
        if self.validate_student(name):
            self.studentsList[name] = [age, course]
        else:
            print("Error: The name already exists.")

        return self.studentsList

    def validate_student(self, name):
        return name not in self.studentsList

    def getStudents(self):
        print("<------------------------ESTUDIANTES------------------------>")
        print("<------Nombre------>|<------Edad------>|<------Materia------>")
        for student, data in self.studentsList.items():
            print(f"{student}{" " * (20-len(student))}|{data[0]}{" "*16}|{data[1]}")


student = students()

student.addStudent("James Clare", 19, "Linux")
student.addStudent("Linux Tolvards", 20, "Calculus")
student.addStudent("Jose Martinez", 21, "Sports")

student.getStudents()
