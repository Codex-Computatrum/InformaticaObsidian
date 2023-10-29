---
author: Simone Parente
tags:
  - Java/modifiers
---
>[!info] 
>Un metodo `abstract` non possiede corpo.
>Si applica *solo a* classi e metodi.

>[!danger] 
>Una classe **deve** essere marcata abstract se:
>- essa contiene almeno un metodo `abstract`
>- essa eredita almeno un metodo `abstract` per cui non fornisce realizzazione
>- essa dichiara di implementare [[Interfaccia|interfacce]] ma non fornisce una realizzazione di tutti i metodi dell'[[Interfaccia|interfaccia]].

È in un certo senso *opposto* a [[final]], una classe `abstract` esiste solo per essere specializzata, mentre un metodo [[final]] non può essere specializzato.