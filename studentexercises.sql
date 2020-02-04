DROP TABLE IF EXISTS 'Student';
DROP TABLE IF EXISTS 'Exercise';
DROP TABLE IF EXISTS 'Student Exercises';


CREATE TABLE Cohort (
	'cohort_id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'cohort_name' TEXT NOT NULL
);

CREATE TABLE Student (
	'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'first_name' TEXT NOT NULL,
	'last_name'  TEXT NOT NULL,
	'slack_handle' 	TEXT NOT NULL,
	'student_cohort' INTEGER NOT NULL,
    FOREIGN KEY(id) REFERENCES Cohort(id)
);

CREATE TABLE Instructor (
	'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'first_name'TEXT NOT NULL,
	'last_name'  TEXT NOT NULL,
	'slack_handle' 	TEXT NOT NULL,
	'teacher_specialty' TEXT NOT NULL,
	FOREIGN KEY(id) REFERENCES Cohort(id)
);

CREATE TABLE Exercise (
	'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'exercise_name' TEXT NOT NULL,
	'exercise_language' TEXT NOT NULL
);

CREATE TABLE Student_Exercises (
	'student_exercises' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'student_id' INTEGER,
	'exercise_id' INTEGER,
	FOREIGN KEY(student_id) REFERENCES Student(id),
	FOREIGN KEY(exercise_id) REFERENCES Exercise(id)	
);

INSERT INTO Cohort 
VALUES (null, 'Cohort 400');

INSERT INTO Cohort 
VALUES (null, 'Cohort 401');

INSERT INTO Cohort 
VALUES (null, 'Cohort 402');

INSERT INTO Exercise
VALUES (null, 'Chicken Monkey', 'Javascript');

INSERT INTO Exercise
VALUES (null, 'Dragon Dog', 'javascript');

INSERT INTO Exercise
VALUES (null, 'Fish Cake', 'Python');

INSERT INTO Exercise
VALUES (null, 'Panda Lamda', 'Python');

INSERT INTO Exercise 
VALUES (null, 'The Code War', 'SQL');

DELETE FROM Exercise
WHERE exercise_language = "Panda Lamda";

INSERT INTO Instructor 
VALUES (null, 'Professor', 'Sprout', 'noDoubtItsSprout', 'growing knowledge');

INSERT INTO Instructor
VALUES (null, 'Professor Ron', 'Burgundy', 'ImRonBurgundy', 'always in the know on current events');

INSERT INTO Instructor
VALUES (null, 'Professor cnl', 'mustard', 'mustardMan', 'always has mustard');

INSERT INTO Student
VALUES (null, 'Harry', 'Potter', 'theChosenOne', 'Cohort 401');

INSERT INTO Student
VALUES (null, 'Hermione', 'Granger', 'GrangerDanger', 'Cohort 401');

INSERT INTO Student
VALUES (null, 'Ronald', 'Weasley', 'GingerGuy', 'Cohort 401');

INSERT INTO Student
VALUES (null, 'Luna', 'Lovegood', 'Quibbler4Lyfe', 'Cohort 400');

INSERT INTO Student
VALUES (null, 'Neville', 'Longbottom', 'ItsLongBottom', 'Cohort 402');

INSERT INTO Student
VALUES (null, 'Angela', 'Bell', 'QuidditchPitch', 'Cohort 402');

INSERT INTO Student
VALUES (null, 'Draco', 'Malfoy', 'DracoMalfoy', 'Cohort 400');

INSERT INTO Student_Exercises
VALUES (null, (SELECT id FROM Student
WHERE first_name = 'Draco'), 
(SELECT id FROM Exercise
WHERE exercise_name = "Chicken Monkey"));

INSERT INTO Student_Exercises
VALUES (null, (SELECT id FROM Student
WHERE first_name = 'Draco'), 
(SELECT id FROM Exercise
WHERE exercise_name = "Dragon Dog"));

INSERT INTO Student_Exercises
VALUES (null, (SELECT id FROM Student
WHERE first_name = 'Draco'), 
(SELECT id FROM Exercise
WHERE exercise_name = "Dragon Dog"));

INSERT INTO Student_Exercises
VALUES (null, (SELECT id FROM Student
WHERE first_name = 'Harry'), 
(SELECT id FROM Exercise
WHERE exercise_name = "Dragon Dog"));

INSERT INTO Student_Exercises
VALUES (null, (SELECT id FROM Student
WHERE first_name = 'Harry'), 
(SELECT id FROM Exercise
WHERE exercise_name = "Chicken Monkey"));

INSERT INTO Student_Exercises
VALUES (null, (SELECT id FROM Student
WHERE first_name = 'Hermione'), 
(SELECT id FROM Exercise
WHERE exercise_name = "Fish Cake"));

INSERT INTO Student_Exercises
VALUES (null, (SELECT id FROM Student
WHERE first_name = 'Hermione'), 
(SELECT id FROM Exercise
WHERE exercise_name = "Panda Lamda"));

INSERT INTO Student_Exercises
VALUES (null, (SELECT id FROM Student
WHERE first_name = 'Neville'), 
(SELECT id FROM Exercise
WHERE exercise_name = "Dragon Dog"));

INSERT INTO Student_Exercises
VALUES (null, (SELECT id FROM Student
WHERE first_name = 'Neville'), 
(SELECT id FROM Exercise
WHERE exercise_name = "Panda Lamda"));

INSERT INTO Student_Exercises
VALUES (null, (SELECT id FROM Student
WHERE first_name = 'Luna'), 
(SELECT id FROM Exercise
WHERE exercise_name = "Dragon Dog"));

INSERT INTO Student_Exercises
VALUES (null, (SELECT id FROM Student
WHERE first_name = 'Luna'), 
(SELECT id FROM Exercise
WHERE exercise_name = "The Code War"));

INSERT INTO Student_Exercises
VALUES (null, (SELECT id FROM Student
WHERE first_name = 'Angela'), 
(SELECT id FROM Exercise
WHERE exercise_name = "Chicken Monkey"));

INSERT INTO Student_Exercises
VALUES (null, (SELECT id FROM Student
WHERE first_name = 'Angela'), 
(SELECT id FROM Exercise
WHERE exercise_name = "Fish Cake"));

INSERT INTO Student_Exercises
VALUES (null, (SELECT id FROM Student
WHERE first_name = 'Ronald'), 
(SELECT id FROM Exercise
WHERE exercise_name = "Dragon Dog"));

INSERT INTO Student_Exercises
VALUES (null, (SELECT id FROM Student
WHERE first_name = 'Ronald'), 
(SELECT id FROM Exercise
WHERE exercise_name = "Fish Cake"));



SELECT id FROM Exercise
WHERE exercise_name = "Chicken Monkey";

--Sub Query example
-- SELECT * FROM Student
-- WHERE first_name = (
-- 	SELECT first_name
-- 	FROM Student
-- 	WHERE id = 7
-- );

--testing a sub query to see if it works
-- 	SELECT first_name
-- 	FROM Student
-- 	WHERE id = 8;


select s.id,
    s.first_name,
    s.last_name,
    s.slack_handle,
    s.student_cohort,
    c.cohort_name
    from Student s
    join Cohort c on s.student_cohort = c.cohort_id
    order by s.student_cohort;

