% Backward chaining: Prolog proves a goal by matching facts and rules.
parent(alice, bob).
parent(bob, carol).
parent(carol, david).

ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% Queries:
% ?- ancestor(alice, carol).
% ?- ancestor(alice, Who).
