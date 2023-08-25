from school import School
class Subject:
    def __init__(self,name,teacher) -> None:
        self.name = name
        self.teacher =teacher
        self.max_marks = 100
        self.pass_marks = 30
    def exam(self,students):
        for student in students:
            mark = self.teacher.evalauate_exam()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = School.calculate_grade(mark)