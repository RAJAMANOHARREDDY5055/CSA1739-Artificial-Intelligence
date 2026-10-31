female(anu).
female(sita).

male(raj).
male(manohar).

parent(sita,anu).
parent(manohar,anu).

parent(sita,raj).
parent(manohar,raj).

mother(X,Y):-
female(X),
parent(X,Y).

father(X,Y):-
male(X),
parent(X,Y).

