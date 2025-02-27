class Student:
    def __init__(self,name,grades):
        self.name = name 
        self.grades = grades
    
    def average_grade(self) -> float:
        if(len(self.grades) == 0):
            return 0
        avg_grade = sum(self.grades)/len(self.grades)
        return round(avg_grade,2)

class GradeBook:
    def __init__(self):
        self.students = []
    
    def add_student(self,student):
        self.students.append(student)

    def print_student_info(self):
        print("Students Info:")
        for student in self.students:
            print(f"Name:{student.name} Averge Grade: {student.average_grade()}")

    def print_student_with_index(self):
        print("List of Students")
        for index,student in enumerate(self.students,start=1):
            print(f"{index}:{student.name}")

    def improve_grade(self):
        index = 0
        while index < len(self.students):
            student = self.students[index]
            for ind,grade in enumerate(student.grades):
                if(grade < 70):
                    student.grades[ind] += 10
            index += 1
        
    def get_first_three_student(self):
         for i in range(min(3, len(self.students))):
            student = self.students[i]
            print(f"Student {student.name} - Average Grade: {student.average_grade()}")

gradebook = GradeBook()
stu1 = Student("Gautam",[60,72,55])
stu2 = Student("Abhinav",[35,50,23])
stu3 = Student("Nishant",[63,80,81])
stu4 = Student("Vivek",[64,76,87])
stu5 = Student("Aditya",[91,94,97])

gradebook.add_student(stu1)
gradebook.add_student(stu2)
gradebook.add_student(stu3)
gradebook.add_student(stu4)
gradebook.add_student(stu5)

gradebook.print_student_info()
gradebook.improve_grade()
gradebook.get_first_three_student()
gradebook.print_student_with_index()
gradebook.get_first_three_student()