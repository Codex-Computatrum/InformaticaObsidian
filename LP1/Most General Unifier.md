Il Most General Unifier (MGU) nella programmazione logica è la [[Sostituzione|sostituzione]] più generale che rende due termini identici. In altre parole, è il modo più generale di istanziare le variabili nei termini in modo che diventino uguali.
La ricerca dell'MGU può essere effettuata in modo algoritmico utilizzando l'algoritmo di unificazione.
### Esempio
``` Prolog
genitore(john, jim).
genitore(john, ann).
genitore(jane, ann).
```
Supponiamo di voler unificare le query
`genitore(john, jim)` e `genitore(X, ann)`.
L'unificazione cercata è quella che ci permette di trovare un'unica sostituzione che rende i due termini uguali. In questo caso, l'unificazione avviene quando `X` viene istanziato a `john`. Quindi, l'MGU in questo caso  è `X/john`.
Un'altra unificazione possibile sarebbe `X/jane`, ma questo non renderebbe i due termini uguali, quindi non è valida.