class School:
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address
        self.classrooms = {}
        self.teachers = {}
    def add_classroom(self,classroom):
        self.classrooms[classroom.name] = classroom
    def add_teacher(self,subject,teacher):
        if subject in self.teachers:
            self.teachers[subject] = teacher
        else:
            print(f'no subject named {subject}')
    def student_admission(self,student):
        className= student.classroom.name

        if className in self.classrooms:
            self.classrooms[className].add_student(student)
        else:
            print(f'no classroom as named {className}')
    def __repr__(self) -> str:
        for key,value in self.classrooms.items():
            print(key)
        eight = self.classrooms['eight']
        for student in eight.students:
            print(student.name)
        for subject in eight.subjects:
            print(subject.name,subject.teacher.name)
        for student in eight.students:
            for key,value in student.marks.items():
                print(student.name,key,value,student.subject_grade[key])
        return ''
    @staticmethod
    def calculate_grade(marks):
        if 80 <= marks <= 100:
            return 'A+'
        elif 70 <= marks < 80:
            return 'A'
        elif 60 <= marks < 70:
            return 'A-'
        elif 50 <= marks < 60:
            return 'B'
        elif 40 <= marks < 50:
            return 'C'
        elif 33 <= marks < 40:
            return 'D'
        else:
            return 'F'
    @staticmethod
    def grade_to_value(grade):
        grade_map = {"A+":5.00,"A":4.00,"A-":3.50,"B":3.00,"C":2.00,"D":1.00,"F":0.00}
        return grade_map[grade]
    @staticmethod
    def value_to_grade(value):
        if 4.5 <= value <= 5.00:
            return 'A+'
        elif 3.5 <= value < 4.5:
            return 'A'
        elif 3.0 <= value < 3.5:
            return 'A-'
        elif 2.5 <= value < 3.0:
            return 'B'
        elif 2.0 <= value < 2.5:
            return 'C'
        elif 1.0 <= value < 2.0:
            return 'D'
        else:
            return 'F'

