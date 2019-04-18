from flask import Flask, render_template, redirect, url_for, request

from student import Student
from utils import save_file

students = []

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def students_page():
    if request.method == "POST":
        student_id = request.form.get("student-id", "")
        student_name = request.form.get("name", "")
        last_name = request.form.get("last-name", "")
        new_student = Student(student_name, last_name, student_id)
        students.append(new_student)
        save_file(new_student)
        return redirect(url_for("students_page"))

    return render_template("index.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)
