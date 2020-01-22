# You must define a type for representing an instructor in code.
# First name
# Last name
# Slack handle
# The instructor's cohort
# The instructor's specialty (e.g. dad jokes, excitement, dancing, etc.)
# A method to assign an exercise to a student
from NSSPerson import NSSPerson
 
class Instructor(NSSPerson):
    def __init__ (self, first_name, last_name, slack_handle, instructors_cohort, instructors_specialty):
        NSSPerson.__init__(self, first_name, last_name, slack_handle)
        self.instructors_cohort = instructors_cohort
        self.instructors_specialty = instructors_specialty     

    def add_exercise(self, student, new_exercise):
        student.current_exercises.append(new_exercise)


        

        # Pass in the student - aka meat_lovers
        # Append/add? current_exercises on that student