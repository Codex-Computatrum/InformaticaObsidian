---
author: Simone Parente
tags:
  - prolog/exercises
  - todo
---
```PROLOG
 
%Data una lista come quella sotto, scrivere una query che restituisce gli studenti maschi
[stud(mario,m), stud(maria,f), stud(paolo,m)].
%stud(X,m)

%Usando member, scrivere la regola per una select (algebra relazionale)>
%sulla relazione r che seleziona i record il cui secondo elemento
%appartiene a una lista data. Se r ha n colonne, la select ha ha n+1
%argomenti:
   %select_r_2(Z,Y, L) :- member(Y,L).
%Non ho capito come creare una regola a n argomenti

%Scrivere un predicato reverse che inverte una lista. Prendere esempio
%dalla soluzione per ML che fa uso di un accumulatore per costruire
%progressivamente la lista invertita
%CHATGPT
reverse(List, Reversed) :- reverse_acc(List, [], Reversed).

reverse_acc([], Acc, Acc).
%reverse_acc([H|T], Acc, Reversed) :- reverse_acc(T, [H|Acc], Reversed).
%----------------------------------------------

%Scrivere un predicato append che concatena due liste

%append1(Lista1, Lista2, Risultato) :- append1([Lista1|Lista2]).

%Somma degli elementi in una lista
sum([], 0).
sum([X|Xs], Total) :- sum(Xs, Subtotal), Total is X + Subtotal.

%Lunghezza di una lista
lung([],0).
lung([H|T], Tot) :- lung(T, Sub), Tot is Sub+1.

%Conta occorrenze sbagliata
%conta(X, [], 0).
%conta(X, [X|T], 1).
%conta(X, [H|T], Tot) :- conta(X, T, Sub), Tot is Sub+1.
%Conta occorrenze giusta
conta(X, [], 0).
conta(X, [H|T], Tot) :- X = H, conta(X, T, Sub), Tot is Sub+1.
conta(X, [H|T], Tot) :- X \= H, conta(X, T, Tot).

```
