from flask import Flask, request, jsonify, render_template
from access_tables import StudentCourses

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/get-courses/<student>")
def get_courses(student):
    student_courses_obj = StudentCourses()
    courses = student_courses_obj.get_student_courses(student)
    # student = "Irina"
    # courses = [["course name 1", start time, end time], ["course 2", start time, end time]]
    courses_json = {"student": student, "courses": courses}
    return jsonify(courses_json), 200

@app.route("/add-course", methods=["POST"])
def add_course():
    student_courses_obj = StudentCourses()
    data = request.form
    # data = {"student": student, "course": [a single course]}
    print(data)
    course_name = data["course"]
    student = data["student"]
    start = data["start_time"]
    end = data["end_time"]
    course = [course_name, start, end]
    student_courses_obj.add_student_course(student, course)
    return jsonify(data), 201
    
if __name__ == "__main__":
    app.run(debug=True)
