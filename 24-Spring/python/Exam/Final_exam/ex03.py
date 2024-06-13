class Student:
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.grades = []
        self.avg = 0

    def add_grade(self, grade):
        self.grades.append(grade)

    def cal_average(self):
        total = 0
        for grade in self.grades:
            total += grade
        count = 0
        for _ in self.grades:
            count += 1
        self.avg = total / count

    def print_information(self):
        print(f'Name: {self.name}, ', end='')
        print(f'Student ID: {self.student_id}, ', end='')
        print(f'Average Grade: {self.avg}')

student1 = Student("Alice", "SOO1")
student2 = Student("Bob", "SOO2")

student1.add_grade(95)
student1.add_grade(88)
student1.add_grade(90)

student2.add_grade(78)
student2.add_grade(85)
student2.add_grade(92)

student1.cal_average()
student2.cal_average()

student1.print_information()
student2.print_information()
