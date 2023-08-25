
from school import School
from classroom import ClassRoom
from persons import Stduent,Teacher
from subject import Subject

def main():
    school = School("Adam jee","Utta")


    cls_eight = ClassRoom("eight")
    school.add_classroom(cls_eight)

    cls_nine = ClassRoom("nine")
    school.add_classroom(cls_nine)

    cls_ten = ClassRoom("ten")
    school.add_classroom(cls_ten)

    saki = Stduent("saki",cls_eight)
    school.student_admission(saki)

    sk = Stduent("sk",cls_eight)
    school.student_admission(sk)

    mb = Stduent("mb",cls_eight)
    school.student_admission(mb)


    physics_teacher=Teacher("topon")
    physics = Subject("physics",physics_teacher)
    cls_eight.add_subject(physics)

    chemistry_teacher=Teacher("shopon")
    chemistry = Subject("chemistry",chemistry_teacher)
    cls_eight.add_subject(chemistry)

    biology_teacher=Teacher("noyon")
    biology = Subject("biology",biology_teacher)
    cls_eight.add_subject(biology)


    cls_eight.taket_semester_final()


    print(school)

if __name__ == '__main__':
    main()