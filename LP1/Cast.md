---
author: Simone Parente
---
# Cast

>[!tldr] TL;DR 
>Un cast (o coercizione di tipo) è una conversione esplicita di un tipo in un altro.
La sintassi è `(T) exp` dove `(T)` è il tipo che vogliamo assegnare e `exp` è un riferimento.

Si può utilizzare un **cast** per:
- Effettuare esplicitamente una promozione (nonostante sia superfluo)
- Effettuare una **promozione al contrario**, per esempio da `double` a `int`, in questi casi è facile incorrere in perdite di informazioni.
Nel passaggio da numeri con la virgola a numeri interi, si può perdere sia in precisione che in magnitudine (ordine di grandezza).
Questi casting sono in generale sconsigliati, è opportuno utilizzare gli appositi metodi della classe `Math`.
## Cast consentiti
Siano `A` e `B` dei tipi riferimento (o array):
1. Se `B` è supertipo di `A`:
    1. Si chiama _**upcast**_ ed è superfluo, perché i valori di tipo `A` sono a prescindere assegnabili al tipo `B` ([[Assegnabilità|relazioni di assegnabilità]])
2. Se `B` è sottotipo di `A`:
    - Si chiama _downcast_
    - A run-time la JVM controlla che l’oggetto da convertire appartenga effettivamente a una sottoclasse di `B`
        - In caso contrario avremo una `ClassCastException`

In generale **è preferibile** <span style="color:#ff0000"> <b> <i>evitare i downcast </i> </b> </span>, perché essi **aggirano il type checking svolto dal compilatore**. Se si deve necessariamente usare un _downcast_, esso dovrebbe essere preceduto da un controllo [[Note esercizi binding#^instanceof|instanceof]], così da assicurare la correttezza della conversione.