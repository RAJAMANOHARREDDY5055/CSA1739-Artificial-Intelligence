monkey(at_door).
box(at_window).
banana(at_ceiling).

can_get_banana:-
monkey(at_door),
box(at_window),
banana(at_ceiling),
write('Monkey reaches banana ').
