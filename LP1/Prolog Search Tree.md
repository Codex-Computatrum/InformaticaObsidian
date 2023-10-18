>[!summary]  L'idea generale
>1. Scrivere la query iniziale in un box al centro della pagina, questo box sarà una sorta di to-do list.
>2. Disegnare le branch basandosi sul numero di clausole definite dal predicato.
>3. Procedere con le branch da sinistra verso destra, se una branch corrisponde a un **fatto**, andare a **4**, se la branch corrisponde a una *regola*, vai allo step *5*.
>4. Se la query non unifica con il fatto, disegnare una $X$. Altrimenti disegnare una un quadrato vuoto (questo quadrato vuoto segnala che non ci sono altre cose da fare).
>5. Se la query non unifica con la testa della regola, disegnare una croce, altrimenti disegnare un nuovo box con il corpo della regola come nuova query.

## Esempio
Supponiamo di avere i seguenti fatti e la relativa regola:
```Prolog
loves(vincent, mia).
loves(marsellus,mia).

jealous(A,B) :- loves(A,C), loves(B,C).
```
>[!todo] Esercizio
>Disegnare il search tree per la query `jealous(X,Y)`.

Andiamo ora ad eseguire i passaggi definiti prima:
1. Scrivere la query iniziale in un box all'inizio della pagina.
![[st prolog P52.png]]
2. Disegnare le branch basandosi sul numero di clausole definite dal predicato.
	-  In questo caso il predicato è `jealous(A,B) :- loves(A,C), loves(B,C)`, dobbiamo quindi verificare solo questa regola, avremo di conseguenza un'unica branch che conterrà una nuova query, che sarà `loves(A,C), loves(B,C)`. Le sostituzioni saranno `X=A, Y=B`.
![[st prolog P53.png]]
    - A questo punto avremo una nuova query, dovremmo quindi ripetere il punto 2. Andiamo a cercare se esistono fatti o regole che permettano sostituzioni, in questo caso i due fatti iniziali unificano con la regola, avremo quindi due diverse branch uscenti da `loves(A,C), loves(B,C)`.
![[st prolog P54.png]]
3. Procedere con le branch da sinistra verso destra, se una branch corrisponde a un **fatto**, andare a **4**, se la branch corrisponde a una *regola*, vai allo step *5*.
Avremo il primo fatto (`loves(vincent, mia)`) che unifica con la prima query (`loves(A,C)`), avremo quindi le sostituzioni `A=vincent, B=mia`.
>[!danger] Attenzione
>Questo non vuol dire che abbiamo trovato una risposta, ci troviamo davanti a una query composta, avremo una risposta nel momento in cui sia `loves(A,C)` che  `loves(B,C)` avranno delle sostituzioni adeguate.

![[st prolog P55.png]]
A questo punto vediamo se nel database esiste un fatto (diverso da `loves(vincent,mia)`) che unifichi con `loves(B,mia)`.
Abbiamo entrambi i fatti che unificano con questa query, disegniamo quindi due branch.
Le sostituzioni saranno `B=vincent` e `B=marsellus`
![[st prolog P56.png]]
4. Non ci sono altre cose da fare, disegniamo due quadrati vuoti.
![[st prolog P57.png]]
>[!danger] Attenzione
>L'esercizio non è ancora finito, dobbiamo tornare indietro e ricominciare con la branch di destra di `loves(A,C), loves(B,C)`.

Adesso la sostituzione sarà `A=marsellus, B=mia`. Ci troviamo davanti a una situazione simile alla precedente, andiamo ad eseguire i passaggi precedenti.
![[st prolog P58.png]]

4. Vediamo se esistono fatti che unificano con `loves(B,mia)`, come prima, avremo due branch (una per `loves(marcellus, mia)` e una per `loves(vincent,mia`), non c'è altro da fare, disegnamo disegniamo due quadrati vuoti sotto le ultime due unificazioni.
![[st prolog P59.png]]

Search tree completato.