---
author: Simone Parente
tags:
  - Java
  - Java/memoryLayout
---

>[!summary] 
>In Java è possibile definire nuove classi (o interfacce) all'interno di altre classi (le esterne sono dette  *top-level*), queste classi sono chiamate **interne**. Questo meccanismo introduce nuove regole di visibilità.

## Classi interne non statiche
>[!summary] 
>Godono delle seguenti proprietà:
>1. Privilegi di visibilità rispetto alla classe che le contiene e alle altre classi contenute in essa
>2. Restrizioni di visibilità rispetto alle classi esterne a quella contenitrice (possono essere [[Private]])
>3. Riferimento implicito ad un oggetto nella classe contenitrice.

- Possono avere qualsiasi tipo di visibilità.
- Ogni oggetto di una classe interna (non statica) possiede un riferimento implicito ad un oggetto della classe contenitrice, tale riferimento **non può essere modificato** e viene inizializzato automaticamente al momento della creazione dell'oggetto.
## Classi interne statiche
>[!info] 
>Godono, a differenza delle non statiche, di una proprietà in meno:
>1. Privilegi di visibilità rispetto alla classe contenitrice e alle altre classi in essa contenute.
>2. Restrizioni di visibilità rispetto alle altre classi esterne a quella contenitrice.

## Esempio
![[memLayoutClassiInterne.jpg]]