class Student:
    def __init__(self, id, name, dob): #constructor
        self.__id = id
        self.__name = name
        self.__dob = dob
    
    # getters
    def _get_id(self):
        return self.__id
    
    def _get_name(self):
        return self.__name

    def _get_dob(self):
        return self.__dob

    # setters
    def set_id(self, id):
        self.__id = id
    
    def set_name(self, name):
        self.__name = name
    
    def set_dob(self, dob):
        self.__dob = dob

    # methods
    def display_student(self):
        print(f"{self.__name}\n"
              f"ID: {self.__id}\n"
              f"DOB: {self.__dob}\n")

class Students:
    def __init__(self):
        self.students = []

    def input_students(self, student):
        self.students.append(student)
    
    def list_students(self):
        for s in self.students:
            s.display_student()

class Course:
    def __init__(self, id, name): # constructor
        self.__id = id
        self.__name = name
        self.__marks = {} # {"student_id": float mark}
    
    # getters
    def _get_id(self):
        return self.__id
    
    def _get_name(self):
        return self.__name

    def _get_mark(self, student_id):
        return self.__marks.get(student_id)

    # setters
    def set_id(self, id):
        self.__id = id
    
    def set_name(self, name):
        self.__name = name

    def set_mark(self, student_id, mark):
        self.__marks[student_id] = mark

    # methods
    def display_course(self):
        print(f"{self.__name}\n"
              f"ID: {self.__id}\n")

    def display_marks(self, student_list):
        print(f"{self._get_name()} ({self._get_id()}):\n")
        if not self.__marks:
            print("No marks yet.")
            return
        
        for s in student_list:
            print(f"{s._get_id()} | {s._get_name()}: {self.__marks.get(s._get_id())}\n")

class Courses:
    def __init__(self):
        self.courses = []
    
    def input_courses(self, course):
        self.courses.append(course)

    def list_courses(self):
        for c in self.courses:
            c.display_course()

def main():
    student_list = Students()
    course_list = Courses()

    student_list.input_students(Student("2410310", "Lê Duy Hoàng", "04/12/2002"))
    student_list.input_students(Student("2410799", "Trần Tuấn Thành", "25/03/2001"))
    course_list.input_courses(Course("MAT2.007", "Probability"))
    course_list.input_courses(Course("MAT2.008", "Dynamical Systems"))
    
    course_list.list_courses()
    student_list.list_students()

    course = course_list.courses[0]
    for s in student_list.students:
        course.set_mark(s._get_id(), 17)
    course.display_marks(student_list.students)

if __name__ == "__main__":
    main()