% Student-Teacher-Subject-Code database.
teaches('T01', 'Dr Rao', 'Artificial Intelligence', 'AI401').
teaches('T02', 'Ms Devi', 'Database Systems', 'CS302').
enrolled('S01', 'Anu', 'AI401').
enrolled('S02', 'Bala', 'CS302').

student_subject(StudentName, Subject, Teacher) :-
    enrolled(_, StudentName, Code),
    teaches(_, Teacher, Subject, Code).

% Queries:
% ?- student_subject('Anu', Subject, Teacher).
% ?- teaches(TeacherCode, Teacher, Subject, Code).
