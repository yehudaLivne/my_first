from person import person
class teacher(person):


    def __init__(self,name,age,salary = 5000):
        super(teacher,self).__init__(name,age)
        self.__salary = salary
        self.__average_grades = 0
        self.__grades = []

    def say(self):
        print("hello")

    def get_a_grade(self,grade):
        self.__grades.append(grade)
        self.__average_grades= self.__average_grades+ (grade-self.__average_grades)/len(self.__grades)


    def __str__(self):
         return "teacher {} is {} years old, he has a {} salary".format(self.get_name(),self.get_age(),self.__salary)


    def get_salary(self):
         return self.__salary

    def get_average_grades(self):
        return self.__average_grades

    def set_salary(self,salary):
         self.__salary = salary


class student(person):
    def __init__(self,name,age):
        super(student,self).__init__(name,age)

        self.__average_grades = 0
        self.__grades = []

    def say(self):
        print("hello")

    def get_a_grade(self,grade):
        self.__grades.append(grade)
        self.__average_grades= self.__average_grades+ (grade-self.__average_grades)/len(self.__grades)


    def __str__(self):
         return "student {} is {} years old, he has a {} avergae grades".format(self.get_name(),self.get_age(),self.__average_grades)



    def get_average_grades(self):
        return self.__average_grades




def main():
    teacher1 = teacher("Sd",3,3)
    print(teacher1)
    student1 = student('sd',3)
    print(student1)
    student1.get_a_grade(3)
    student1.get_a_grade(5)
    student1.get_a_grade(6)
    student1.get_a_grade(4)
    student1.get_a_grade(7)
    print(student1)
if __name__ == '__main__':
    main()
