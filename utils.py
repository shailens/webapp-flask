students = []


def print_all_students():
    for student in students:
        print(student)


def get_students_title_case():
    students_title_case = []
    for student in students:
        students_title_case.append(student["name"].title())
    return students_title_case


def print_students_title_case():
    student_title_case = get_students_title_case()
    print(student_title_case)


def add_students(name, student_id=111):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student.name + " " + student.last_name + "\n")
        f.close()
    except FileNotFoundError:
        print("File Not Found!")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_students(student)
        f.close()
    except FileNotFoundError:
        print("File Not found!")




