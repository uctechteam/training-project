from flask import Flask
from access_tables import StudentCourses

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route("/get-courses/<student>")
def get_courses(student):
    courses = get_student_courses(student)
    return {"courses": courses}
    # return {"courses": ["Class0", "Class1"]}

@app.route("/add-course/<student>", methods=["POST"])
def add_course(student):

if __name__ == "__main__":
    app.run(debug=True)
