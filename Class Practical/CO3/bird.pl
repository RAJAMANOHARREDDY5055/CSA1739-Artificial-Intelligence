bird(parrot).
bird(eagle).
bird(ostrich).
bird(penguin).

can_fly(parrot).
can_fly(eagle).

files(X):-
bird(X),
can_fly(X).