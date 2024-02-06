---
author: Simone Parente
tags:
  - Java/modifiers
---
>[!info] 
>Si applica *solo a* classi e metodi.
>Un metodo `abstract` non possiede corpo.

>[!danger] 
>Una classe **deve** essere marcata abstract se:
>- essa contiene almeno un metodo `abstract`
>- essa eredita almeno un metodo `abstract` per cui non fornisce realizzazione
>- essa dichiara di implementare [[Interfaces|interfacce]] ma non fornisce una realizzazione di tutti i metodi dell'[[Interfaces|interfaccia]].

È in un certo senso *opposto* a [[Final]], una classe `abstract` esiste solo per essere specializzata, mentre una classe [[Final]] non può essere specializzato.