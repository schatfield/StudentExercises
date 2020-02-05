# You must define a custom type for representing a student in code. A student can only be in one cohort at a time. A student can be working on many exercises at a time.

# Properties
# First name
# Last name
# Slack handle
# The student's cohort
# The collection of exercises that the student is currently working on
# Cohort

from NSSPerson import NSSPerson

class Student(NSSPerson):
    def __init__(self, first_name, last_name, slack_handle, cohort):
        NSSPerson.__init__(self, first_name, last_name, slack_handle)
        self.cohort = cohort
        self.current_exercises = []

# 

# class Student():

#     def __init__(self, first, last, handle, cohort):
#         self.first_name = first
#         self.last_name = last
#         self.slack_handle = handle
#         self.cohort = cohort

def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort_name}'
