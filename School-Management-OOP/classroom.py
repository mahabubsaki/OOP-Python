class ClassRoom:
    def __init__(self,name) -> None:
        self.name = name
        self.students = []
        self.subjects = []

    def add_student(self,student):
        serial_id = f'{self.name}-{len(self.students) + 1}'
        student.id = serial_id
        self.students.append(student)

    def taket_semester_final(self):
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
            student.calculate_final_grade()

    def add_subject(self,subject):
        self.subjects.append(subject)

    def __str__(self) -> str:
        return f'{self.name}-{len(self.students)}'

    def get_top_students(self):
        pass