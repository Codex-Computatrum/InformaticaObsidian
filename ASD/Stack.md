---
author: Lorenzo Tecchia
tags: [definition, dataStructure, to-do]
---
>[!todo] 
>- [ ] Implementazione in C

Uno ***stack*** è un tipo di dati astratto che viene usato per riferirsi a [[Struttura dati|strutture dati]], le cui modalità di accesso sono di tipo: **LIFO**, ovvero **Last In First Out**. L'ultimo elemento inserito è il primo ad essere eliminato.

## Operazioni sulla struttura
Così come un numero di altre strutture dati, lo stack possiede tutte le [[operazioni elementari]].
Solo che nel caso dello stack, le funzioni di $Insert$ e $Delete$ si chiamano rispettivamente $Push$ e $Pop$.

| Nome           | Descrizione                                                                         |
| ------------------- | ----------------------------------------------------------------------------------- |
| $Stack(D)$          | Nome della classe, in questo caso uno $Stack$(LIFO), $D$ è un generico tipo di dato |
| $Push(D):S$         | Inserisce in testa nello $Stack$ e restituisce il nuovo                             |
| $Pop():S$           | Rimuove dallo $Stack$ e restituisce il nuovo                                        |
| $Top():S$           | Restituisce la testa dello stack                                                    |
| $Top\&Pop(): (S,D)$ | Restituisce la testa e il nuovo $Stack$, ed elimina la testa                        |

## Implementazione in C
```C
// da implementare
```