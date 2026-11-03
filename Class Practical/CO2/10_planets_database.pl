% Planet facts (distance is approximate mean distance from Sun in million km).
planet(mercury, 57.9, terrestrial).
planet(venus, 108.2, terrestrial).
planet(earth, 149.6, terrestrial).
planet(mars, 227.9, terrestrial).
planet(jupiter, 778.6, gas_giant).
planet(saturn, 1433.5, gas_giant).
planet(uranus, 2872.5, ice_giant).
planet(neptune, 4495.1, ice_giant).

% Queries:
% ?- planet(Name, Distance, Type).
% ?- planet(Name, _, gas_giant).
