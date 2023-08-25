import random
from school import School
class Persons:
    def __init__(self,name) -> None:
        self.name = name
    
class Teacher(Persons):
    def __init__(self, name) -> None:
        super().__init__(name)
        # self.subject= subject
    def teach(self):
        pass
    def evalauate_exam(self):
        marks = random.randint(0,100)
        return marks


class Stduent(Persons):
    def __init__(self, name,classroom) -> None:
        super().__init__(name)
        self.__id = None
        self.classroom = classroom
        self.marks = {}
        self.subject_grade = {}
        self.grade = None
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id = value
    
    def calculate_final_grade(self):
        sum = 0
        for grade in self.subject_grade.values():
            point = School.grade_to_value(grade)
            sum+=point
        poinst_avg = sum/len(self.subject_grade)
        self.grade = School.value_to_grade(poinst_avg)
        print(f'{self.name} final grade: {self.grade} with points avg {float(poinst_avg)}')

