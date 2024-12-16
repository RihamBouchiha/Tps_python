class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    #getter pour grade de l'etudiant
    def get_grade(self):
        return self.grade
    
    #getter to name
    """def getNom(self):
        return self.name"""
    
    #classe course
class Course : 
        def __init__(self,name,max_students,students=[]):
            self.name = name
            self.max_students = max_students
            self.students = students

# method to verify size of class
        def add_student(self,student):
            if len(self.students) < self.max_students:
                self.students.append(student)
                print(f"l'etudiant{self.student} est ajouté avec succès")
            else:
                print("la classe a atteint son maximum")

#method to return te average of grade
        def get_average_grade(self):
            somm = 0
            moyenne = 0
            for student in self.students:
                somm += student.get_grade()
            moyenne = somm/len(self.students)

            print(f"la moyenne des etudiants est : {moyenne}")

stud1 = Student("riham",21,20)
stud2 = Student("siham",22,18)
stud3 = Student("issam",22,19)

crs = Course("python",2,[stud1,stud2])

crs.get_average_grade()

crs.add_student("iss")
