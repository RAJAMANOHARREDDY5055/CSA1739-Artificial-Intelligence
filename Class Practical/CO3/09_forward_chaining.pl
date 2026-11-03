% Forward chaining: repeatedly apply rules whose premises are known.
fact(parent(alice, bob)).
fact(parent(bob, carol)).
rule(grandparent(X, Z), [parent(X, Y), parent(Y, Z)]).

known(F) :- fact(F).
known(F) :- derived(F).
derived(grandparent(X, Z)) :-
    known(parent(X, Y)),
    known(parent(Y, Z)).

% Query: ?- derived(grandparent(alice, carol)).
