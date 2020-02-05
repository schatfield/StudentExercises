# You must define a type for representing a cohort in code.

# The cohort's name (Evening Cohort 6, Day Cohort 26, etc.)
# The collection of students in the cohort.
# The collection of instructors in the cohort.
# Instructor

class Cohort:
    def __init__(self, cohort_name):
        self.cohort_name = cohort_name
        self.cohort_students = []
        self.cohort_instructors = []
        self.cohort_instructor = ""



    def __repr__(self):
        return f'{self.cohort_name}'