class Student:
    def __init__(self, name):
        self.__name = name  
        self.__grades = []  

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            print(f"Added grade: {grade} for {self.__name}.")
        else:
            print("Grade must be between 0 and 100.")

    def get_average(self):
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)  
        return 0

    def display_info(self):
        print(f"Student Name: {self.__name}, Average Grade: {self.get_average():.2f}")


student = Student("Da One")
student.add_grade(90)
student.add_grade(90)
student.add_grade(90)
student.display_info()