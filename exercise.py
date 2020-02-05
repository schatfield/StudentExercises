# You must define a type for representing an exercise in code. An exercise can be assigned to many students.

# Name of exercise
# Language of exercise (JavaScript, Python, CSharp, etc.)

class Exercise:
    def __init__ (self, exercise_name, exercise_language):
        self.exercise_name = exercise_name
        self.exercise_language = exercise_language
        
    def __repr__(self):
        return f'{self.exercise_name}'