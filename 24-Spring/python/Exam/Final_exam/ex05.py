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

class StudentManger:
    def __init__(self):
        self.students = {}

    def add_student(self, student: object):
        self.students[student.student_id] = student

    # Student ID를 받아 student 객체를 반환
    def get_students(self, student_id):
        return self.students[student_id]

    # get_students 함수를 호출하여 Student ID로 학생정보 반환
    def print_students_avg(self, student_id):
        student = self.get_students(student_id)
        student.cal_average()
        print(f'Student ID: {student.student_id}, ', end='')
        print(f'Average Grade: {student.avg}')


manager = StudentManger()

student1 = Student("Alice", "SOO1")
student2 = Student("Bob", "SOO2")

manager.add_student(student1)
manager.add_student(student2)

student1.add_grade(95)
student1.add_grade(88)
student1.add_grade(90)

student2.add_grade(78)
student2.add_grade(85)
student2.add_grade(92)

manager.print_students_avg("SOO1")
manager.print_students_avg("SOO2")

# 예상출력
# 'Student ID': 'SOO1', 'Average Grade': 91.0
# 'Student ID': 'SOO2', 'Average Grade': 85.0