import sqlite3


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/shawnachatfield/workspace/pythonTime/StudentExercises/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
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
            # Since a tuple is simply an immutable list, you can use square-bracket notation to extract individual items out of it. Displaying a tuple to the terminal as output is not good UX. Use the following code to just display the first name (second column), last name (third column), and cohort name (sixth column).
            # this loop is extracting individual columns to display first name [1], last name [2], and cohort name [3]
            for student in all_students:
                print(f'{student[1]} {student[2]} is in {student[5]}')

reports = StudentExerciseReports()
reports.all_students()


# if __name__ == "__main__":
#     print("I'm running this file as main")