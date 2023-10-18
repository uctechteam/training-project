from flask import Flask, request, jsonify
from access_tables import StudentCourses

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route("/get-courses/<student>")
def get_courses(student):
    student_courses_obj = StudentCourses()
    courses = student_courses_obj.get_student_courses(student)
    courses_json = {"courses": courses}
    return jsonify(courses_json), 200

@app.route("/add-course", methods=["POST"])
def add_course():
    student_courses_obj = StudentCourses()
    data = request.get_json()
    student = data["student"]
    course = data["course"]
    student_courses_obj.add_student_course(student, course)
    return jsonify(data), 201

# Show PUT request through deleting courses?

if __name__ == "__main__":
    app.run(debug=True)
