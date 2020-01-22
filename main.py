# Once you have defined all of your custom types, go to main.py, import the classes you need, and implement the following logic.

from cohort import Cohort 
from exercise import Exercise
from instructor import Instructor
from student import Student


# Create 4, or more, exercises.

exercise_one = Exercise("dragon_dog", "javascript")
exercise_two = Exercise("chicken_monkey", "python")
exercise_three = Exercise("fish_bird", "SQL")
exercise_four = Exercise("koala_cat", "HTML" )

# Create 3, or more, cohorts.

cohort_one = Cohort("Cohort 1")
cohort_two = Cohort("Cohort 2")
cohort_three = Cohort("Cohort 3")

# Create 4, or more, students and assign them to one of the cohorts.

student_one = Student("Harry", "Potter", "@TheChosenOne", cohort_three)
student_two = Student("Lavendar", "Brown", "@LavvyB", cohort_three)
student_three = Student("Herminone", "Granger", "@BookLover23", cohort_two)
student_four = Student("Percy", "Weasley", "@IloveRules", cohort_one)

cohort_one.cohort_students.extend([student_four]) 
cohort_two.cohort_students.extend([student_three])
cohort_three.cohort_students.extend([student_one, student_two])

# Create 3, or more, instructors and assign them to one of the cohorts.

instructor_one = Instructor("Professor", "Sprout", "@NoDoubtImPSprout", cohort_one, "Plants")
instructor_two = Instructor("Professor Ron", "Burgandy", "@RonBurgandyNews", cohort_two, "Public Speaking")
instructor_three = Instructor("Professor Col", "Mustard", "@MustOrBust", cohort_three, "eating mustard")

cohort_one.cohort_instructor = instructor_one
cohort_two.cohort_instructor = instructor_two
cohort_three.cohort_instructor = instructor_three

# Have each instructor assign 2 exercises to each of the students.

# def add_exercise(self, student, new_exercise):
#         student.current_exercises.append(new_exercise)

students =[student_one, student_two, student_three, student_four]

for student in students:
    # srpout give student one chicken_moenky
    # srpout give student one koala_bird
    instructor_one.add_exercise(student, exercise_one)
    instructor_one.add_exercise(student, exercise_two)

    instructor_two.add_exercise(student, exercise_three)
    instructor_two.add_exercise(student, exercise_four)

    instructor_three.add_exercise(student, exercise_one)
    instructor_three.add_exercise(student,exercise_two)    
    