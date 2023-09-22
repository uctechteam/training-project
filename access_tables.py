import sqlite3 

class StudentCourses:
    def __init__(self):
        # Connect to the database studentcourses, and create it if it doesn't exist
        self.con = sqlite3.connect("studentcourses.db")
        self.cur = self.con.cursor()
        # Initialize the table student_courses if DNE 
        # self.cur.execute('''CREATE TABLE IF NOT EXISTS
        #     student_courses (
        #         id INTEGER PRIMARY KEY AUTOINCREMENT,
        #         student TEXT NOT NULL, 
        #         course TEXT NOT NULL,
        #         start_time REAL NOT NULL, 
        #         end_time REAL NOT NULL
        #         )
        #         ''')
    
    def get_student_courses(self, student):
        '''Retrieve a list of courses associated with a student in the format
        {[course1, start_time, end_time], [course2, start_time, end_time]}'''
        select_statement = '''
            SELECT * FROM student_courses'''
        self.cur.execute(select_statement)
        return self.cur.fetchall()
    
    def delete_student(self, student):
        '''Delete all entries in the table for the given student'''
        select_statement = '''
            DELETE * FROM student_courses WHERE student = 'Abida' '''
        courses = self.cur.execute(select_statement)
    
    def delete_student_course(self, student, course):
        '''Delete all entries in the table for the given student'''
        select_statement = '''
            DELETE * FROM student_courses WHERE student = ''' + student + ''' AND course = ''' + course
        courses = self.cur.execute(select_statement)
    
    def add_student_courses(self, student, courses):
        ''' atomic '''
        for course in courses:
            params = (student, course[0], course[1], course[2])
            select_statement = '''INSERT INTO 
                student_courses
                VALUES (NULL,?,?,?,?) '''
            self.cur.execute(select_statement, params)
        res = self.cur.execute("SELECT * FROM student_courses")
        return self.cur.fetchall()

    def update_student_course(self, student, course):
        pass 

def main():
    # initialize the studentcourses class
    studentcourses = StudentCourses()
    studentcourses.add_student_courses("Abida", [["Databases", 100, 200]])
    res = studentcourses.get_student_courses("Abida")
    # add a student to the database 
    print(res)
    # get student course 

if __name__ == "__main__":
    main()