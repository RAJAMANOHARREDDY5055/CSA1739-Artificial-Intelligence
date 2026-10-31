disease(man,diabetes).
disease(sita,fever).
disease(kin,hypertension).

diet(diabetes,low_sugar).
diet(fever,plenty_of_fluids).
diet(hypertension,low_salt).


suggest_diet(Person, Diet):-
disease(Person,Disease),
diet(Disease,Diet).