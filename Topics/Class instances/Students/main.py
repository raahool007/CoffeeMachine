class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

        # calculate the student_id here
        self.student_id = self.name[0] + self.last_name + self.birth_year


name = input()
last_name = input()
birth_year = input()
student = Student(name, last_name, birth_year)
print(student.student_id)
