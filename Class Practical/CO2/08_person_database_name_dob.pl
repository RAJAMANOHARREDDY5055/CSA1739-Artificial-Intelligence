% Simple database of names and dates of birth.
person(alice, date(12, 5, 2002)).
person(bob, date(3, 11, 2001)).
person(charlie, date(25, 1, 2003)).

% Queries:
% ?- person(alice, DOB).
% ?- person(Name, date(_, _, 2002)).
