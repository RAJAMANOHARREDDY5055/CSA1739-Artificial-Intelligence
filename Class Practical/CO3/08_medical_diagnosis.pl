% Toy rule-based diagnosis example; not a substitute for a clinician.
symptom(alex, fever).
symptom(alex, cough).
symptom(sam, sneezing).
symptom(sam, runny_nose).

possible_condition(Person, flu_like_illness) :-
    symptom(Person, fever), symptom(Person, cough).
possible_condition(Person, common_cold) :-
    symptom(Person, sneezing), symptom(Person, runny_nose).

% Queries: ?- possible_condition(alex, Diagnosis).
%           ?- possible_condition(sam, Diagnosis).
