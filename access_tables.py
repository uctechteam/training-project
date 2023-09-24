import sqlite3 

class StudentCourses:
    def __init__(self):
        # Connect to the database studentcourses, and create it if it doesn't exist
        self.con = sqlite3.connect("studentcourses.db")
        self.cur = self.con.cursor()
        # Initialize the table student_courses if DNE 
        self.cur.execute('''CREATE TABLE IF NOT EXISTS
            student_courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student TEXT NOT NULL, 
                course TEXT NOT NULL,
                start_time REAL NOT NULL, 
                end_time REAL NOT NULL
                )
                ''')
        self.con.commit()

    def close_connection(self):
        ''' Closes the cursor and the connection to the database'''
        self.cur.close()
        self.con.close()

    def print_table(self):
        self.cur.execute("SELECT * FROM student_courses")
        return self.cur.fetchall()
    
    def get_student_courses(self, student):
        '''Retrieve a list of courses associated with a student in the format
        {[course1, start_time, end_time], [course2, start_time, end_time]}'''
        select_statement = "SELECT * FROM student_courses WHERE student = '{student}' ".format(student=student)
        self.cur.execute(select_statement)
        return self.cur.fetchall()
    
    def delete_student(self, student):
        '''Delete all entries in the table for the given student'''
        delete_statement = "DELETE FROM student_courses WHERE student = '{student}' ".format(student=student)
        self.cur.execute(delete_statement)
        self.con.commit()
    
    def delete_student_course(self, student, course):
        '''Delete all entries in the table for the given student'''
        delete_statement = '''
            DELETE FROM student_courses WHERE student = '{student}' AND course = '{course}'
            '''.format(student=student, course=course)
        self.cur.execute(delete_statement)
        self.con.commit()
    
    def add_student_course(self, student, course):
        ''' Add a new course for the student if there are no overlaps, 
        else throw an error; also note that the operation is atomic,
        meaning either all or no courses are added '''
        # Validate that start and end times are valid
        curr_start, curr_end = course[1], course[2]
        if curr_end <= curr_start:
            raise Exception("Class ends before it begins!")

        # Get all the courses and sort by start time, check that none of the courses are invalid 
        old_courses = self.get_student_courses(student)
        old_courses.sort(key=lambda entry: entry[3]) # start time

        # Check for any overlapping times
        for i, old_course in enumerate(old_courses):
            _, _, _, start, end = old_course
            if (curr_start < end and curr_start >= start) or (curr_start <= start and curr_end > end): 
                raise Exception("Error: Overlapping courses!")
            
        # Insert the courses otherwise
        params = (student, course[0], course[1], course[2])
        select_statement = '''INSERT INTO 
            student_courses
            VALUES (NULL,?,?,?,?) '''
        self.cur.execute(select_statement, params)
        self.cur.execute("SELECT * FROM student_courses")
        res = self.cur.fetchall()
        self.con.commit()
        return res

def main():
    # initialize the studentcourses class
    studentcourses = StudentCourses()
    # Uncomment the following code if first time running script
    # Add first entry for student 'Abida'
    # studentcourses.add_student_course("Abida", ["Databases", 100, 200])
    # # Validate entry was added
    # res1 = studentcourses.get_student_courses("Abida")
    # # Delete (Abida, Databases) entry
    # studentcourses.delete_student_course("Abida", "Databases")
    # # Validate entry was deleted
    # res2 = studentcourses.get_student_courses("Abida")
    # # Add overlapping OS course
    # studentcourses.add_student_course("Abida", ["Databases", 100, 200])
    # # studentcourses.add_student_course("Abida", ["OS", 150, 250])
    # # Validate only DB was added
    # res3 = studentcourses.get_student_courses("Abida")
    # # Both Databases and OS should have been added
    # studentcourses.add_student_course("Abida", ["OS", 250, 260])
    # res4 = studentcourses.get_student_courses("Abida")
    # res5 = studentcourses.print_table()
    # print(res, res1, res2, res3, res4, res5)
    studentcourses.close_connection()

if __name__ == "__main__":
    main()