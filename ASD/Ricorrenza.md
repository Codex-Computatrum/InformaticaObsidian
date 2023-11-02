---
author: Lorenzo Tecchia
tags:
  - definition
---
Una ***ricorrenza*** è una equazione o disequazione che descrive una funzione in termini dei suoi valori su input più piccoli.

>[!tip] 
> Per risolvere al pieno equazioni di ricorrenza ricorre in ogni caso, utilizzare un mix dei metodi proposti qui sotto.

>[!important]
> Permette di descrivere i [[Analisi asintotica#Notazione $ Theta$|tempi di esecuzione]] degli algoritmi divide et impera.
## Risoluzioni
### Sostituzione
Nel ***metodo di sostituzione***, ipotizziamo un limite e poi usiamo l'induzione matematica per dimostrare che la nostra ipotesi sia corretta
#### Esempio
### Albero delle ricorrenze
Il ***metodo dell'albero delle ricorrenze o albero di [[ricorsione]]*** converte la ricorrenza in un albero i cui nodi rappresentano i costi ai vari livelli della ricorsione; per risolvere la ricorrenza, adotteremo delle tecniche che limitano le sommatorie.
>[!tip] 
> Di solito, in questo caso, è buona norma andare a disegnare l'albero delle ricorrenze fino ad un livello che ci permetta di interpretare l'andamento

Quando si risolve un'equazione di ricorrenza con albero delle ricorrenza, vanno tenute a mente le seguenti informazioni:
1. Numero del livello
2. Input
3. Contributo ad ogni livello
4. Numero di rami
5. Totale
Ad ogni passo quindi:
- Sostituiamo l'input 
- Verifichiamo il contributo dei nodi
- Calcoliamo il numero di rami ad ogni chiamata ricorsiva
- Calcoliamo il totale moltiplicando il contributo dei nodi per il numero di rami
#### Esempio
| Livello | Input             | Contributo        | Rami                                                   | Totale                                   |
| ------- | ----------------- | ----------------- | ------------------------------------------------------ | ---------------------------------------- |
| 0       | $n$               | $n$               | 1                                                      | n                                        |
| 1       | $n^{\frac{1}{3}}$ | $n^{\frac{1}{3}}$ | $n^{\frac{2}{3}}$                                      | $n^{\frac{1}{3}}\cdot n^{\frac{2}{3}}=n$ |
| 2       | $n^{\frac{1}{9}}$ | $n^{\frac{1}{3}}$ | $n^{\frac{2}{3}}\cdot n^{\frac{2}{9}}=n^{\frac{8}{9}}$ |$n^{\frac{1}{9}}\cdot n^{\frac{8}{9}}=n$                                          |
### Metodo dell'esperto
Il ***metodo dell'esperto*** fornisce i limiti per ricorrenze nella forma $$T(n)=a\;T(n/b)+f(n)$$
dove $a\geq 1, b > 1$ e $f(n)$ è una funzione data.
#### Esempio