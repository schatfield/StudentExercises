import sqlite3
from student import Student
from cohort import Cohort
from exercise import Exercise


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""
    # function definition to create a student, 
    # def create_student(self, cursor, row):
    #     return Student(row[1], row[2], row[3], row[5])

    def __init__(self):
        self.db_path = "/Users/shawnachatfield/workspace/pythonTime/StudentExercises/studentexercises.db"


    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
            row[1], row[2], row[3], row[5])               
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.student_cohort,
                c.cohort_name
            from Student s
            join Cohort c on s.student_cohort = c.cohort_id
            order by s.student_cohort
            """) 

            all_students = db_cursor.fetchall()

            # Extracting Individual Columns
            # this loop is extracting individual columns to display first name [1], last name [2], and cohort name [3]
            # for student in all_students:
            #     print(f'{student[1]} {student[2]} is in {student[5]}')

            # for student in all_students:
            #     print(f'{student.first_name} {student.last_name} is in {student.cohort}')
           

            for student in all_students:
                 print(student)
          # this replaces the for loop we originally had above


     # function definition to create a student, 
    # def create_cohort(self, cursor, row):
    #     return Cohort(row[1])


    def all_cohorts(self):

        """Retrieve all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory =lambda cursor, row: Cohort(
                row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.cohort_id,
                c.cohort_name
            from Cohort c
                """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort)


    def all_exercises(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.id,
                e.exercise_name,
                e.exercise_language
            from Exercise e
                """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)


reports = StudentExerciseReports()
reports.all_students()
reports.all_cohorts()
reports.all_exercises()


# if __name__ == "__main__":
#     print("I'm running this file as main")