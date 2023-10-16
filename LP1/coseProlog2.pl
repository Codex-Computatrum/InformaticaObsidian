%Predicato per verificare se un numero è positivo.
isPositive(X):- X>0.
%Predicato per calcolare il quadrato di un numero intero.
quadr(X, Y):- Y is X*X.
%Predicato per verificare se una lista contiene un elemento specifico.
contains(X, [X]).
contains(X, [_|T]) :- contains(X,T).
%Predicato per calcolare la somma dei primi N numeri interi.
sumN(0, 0).
sumN(N, Tot) :- N1 is N - 1, sumN(N1, Sub), Tot is Sub + N.

%Fattoriale
fact(0,0).
fact(1,1).
fact(X, Tot):- X1 is X-1, fact(X1, Sub), Tot is Sub*X.


% Minimo e Max in una lista
min([X], X).
min([H|T], Min) :- min(T, Min1), Min1 < H, Min is Min1.
min([H|T], Min) :- min(T, Min1), Min1 >= H, Min is H.

max([X], X).
max([H|T], Max) :- max(T, Max1), Max1 > H, Max is Max1.
max([H|T], Max) :- max(T, Max1), Max1 =< H, Max is H.

minmax([X], X, X).
minmax(L1, Min, Max) :- min(L1, Min), max(L1, Max).



%Predicato che verifichi che una lista inizi con A e termini con B
head([H|T], H).
tail([X], X).
tail([_|T], R) :- tail(T, R1), R is R1.
verifica(L1, A, B) :- head(L1, A), tail(L1, B).

%Scrivi un predicato che concateni due liste
concatenazione([], Ris, Ris).
concatenazione(L1, L2, Ris):- append(L1,L2, Ris).

%Media elementi lista
sumL([H], H).
sumL([H|T], Sum):- sumL(T, Sum1), Sum is Sum1+H.
media(List, Media):- sumL(List, Sum), length(List, Len), Media is Sum/Len.

%Predicato che calcoli l'i-esimo elemento di una lista (il primo elemento è I=1)
iElem([H|_], 1, H).	
iElem([_|T], I, Res):- I>1,  I1 is I-1, iElem(T, I1, Res).

%Predicato che inserisce in coda a una lista
append_to_end(Element, [], [Element]).
append_to_end(Element, [Head|Tail], [Head|Result]) :-
    append_to_end(Element, Tail, Result).
