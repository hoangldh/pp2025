# <STUDENT MARK MANAGEMENT SYSTEM>

# Global variables
students = [] # list: dicts {"id": str, "name": str, "dob": (day, month, year)}
courses = [] # list: dicts {"id": str, "name": str}
marks = {} # dict: course_id -> {student_id: mark}

# 1. Input student information
def input_student_info():
    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\nStudent #{i+1}")
        id = input("ID: ")
        name = input("Name: ")

        dob_str = input("DOB (dd/mm/yyyy): ")
        d, m, y = dob_str.split("/")
        dob = (d, m, y)
        students.append({"id": id, "name": name, "dob": dob})

# 2. List students
def list_students():
    if not students:
        print("No students to list.")
        return
    
    print("\n<List of students>\n")
    for s in students:
        d, m, y = s["dob"]
        print(f"ID: {s["id"]}, Name: {s["name"]}, DOB: {d}/{m}/{y}\n")

# 3. Input course information
def input_course_info():
    n = int(input("Enter number of courses: "))

    for i in range(n):
        print(f"\nCourse #{i+1}")
        id = input("ID: ")
        name = input("Name: ")
        courses.append({"id": id, "name": name})


# 4. Input mark
def input_mark():
    if not courses:
        print("No courses available. Please input course information first.")
        return
    
    if not students:
        print("No students available. Please input student information first.")
        return
    
    for c in courses:
        print(f"{c["id"]} - {c["name"]}")
    id = input("\nEnter course ID: ")

    if id not in marks:
        marks[id] = {}

    for s in students:
        marks[id][s["id"]] = float(input(f"Mark for {s["name"]} ({s["id"]}): "))

# 5. List courses
def list_courses():
    if not courses:
        print("No courses to list.")
        return
    
    print("\n<List of courses>\n")
    for c in courses:
        print(f"ID: {c["id"]}, Name: {c["name"]}\n")
        

# 6. Show mark 
def show_mark():
    if not marks:
        print("No marks to list.")
        return
    
    print("\n<List of marked courses>\n")
    for cid in marks.keys():
        cname = None
        for c in courses:
            if c["id"] == cid:
                cname = c["name"]
                break
        if cname is None:
            cname = "(unknown)"
        print(f" {cid}: {cname}")
    
    course_id = input("Enter course ID: ")
    if course_id not in marks:
        print("No marks recorded for this course.")
        return
    
    print(f"\nCourse {course_id}\n")
    for (sid, m) in marks[course_id].items():
        sname = "(unknown)"
        for s in students:
            if s["id"] == sid:
                sname = s["name"]
                break
        print(f"Student {sid} - {sname}: {m}")

def menu():
    print("<STUDENT MARK MANAGEMENT SYSTEM>\n"
            "1. Input student information\n"
            "2. List students\n"
            "3. Input course information\n"
            "4. Input mark\n"
            "5. List courses\n"
            "6. Show mark\n"
            "0. Exit\n")

# TESTER
def main():
    while True:
        menu()
        choice = int(input("\nEnter option (0-6): "))

        match choice:
            case 1:
                input_student_info()
            case 2:
                list_students()
            case 3:
                input_course_info()
            case 4:
                input_mark()
            case 5:
                list_courses()
            case 6:
                show_mark()
            case _:
                break

if __name__ == "__main__":
    main()