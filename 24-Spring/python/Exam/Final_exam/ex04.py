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

    def get_average(self):
        return self.avg

    def get_name(self) -> str:
        return self.name

    def get_student_id(self) -> str:
        return self.student_id

    def print_information(self):
        print(f'Name: {self.get_name()}, ', end='')
        print(f'Student ID: {self.get_student_id()}, ', end='')
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

student_informs = {}
st1_id = student1.get_student_id()
student_informs[st1_id] = {
    'Name': student1.get_name(),
    'Student ID': student1.get_student_id(),
    'Average Grade': student1.get_average()
}

st2_id = student2.get_student_id()
student_informs[st2_id] = {
    'Name': student2.get_name(),
    'Student ID': student2.get_student_id(),
    'Average Grade': student2.get_average()
}

st1_info = student_informs.get(st1_id)
st2_info = student_informs.get(st2_id)

print(st1_info)
print(st2_info)
