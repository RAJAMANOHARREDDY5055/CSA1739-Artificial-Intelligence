% Sum integers from 1 to N.
sum_n(0, 0).
sum_n(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum_n(N1, Previous),
    Sum is N + Previous.

% Query: ?- sum_n(5, S).
