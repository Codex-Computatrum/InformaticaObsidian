---
author: Simone Parente
tags:
  - UML/statecharts
---
## Transizioni
>[!tldr] Cos'è una transizione?
>Una transizione è un arco orientato che va da uno [[Stati|stato]] all'altro.

Rappresentano possibili cambiamenti di stato, possono essere decorate con dei labels (opzionali):

>[!info] Labels
>- <span style="color:#ffbe0a"><b>triggers</b></span>: lista di eventi che possono indurre un cambiamento di stato
>- <span style="color:#00ccff"><b>[guard]</b></span>: condizione booleana
> - <span style="color:#c800ff"><b>\actions</b></span>: elenco di operazioni da eseguire quando si verifica la transizione

```plantuml
!theme crt-amber
state Stato_A
state Stato_B

Stato_A --> Stato_B : triggers [guard] /actions 
```

Le transizioni che non possiedono <span style="color:#ffbe0a"><b>triggers</b></span> né <span style="color:#00ccff"><b>guards</b></span> sono dette **transizioni spontanee**. ^transizionispontanee