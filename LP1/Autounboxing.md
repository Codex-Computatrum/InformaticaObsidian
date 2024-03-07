---
author: Simone Parente
tags:
  - Java
---
>[!summary]
> L'autounboxing è la conversione automatica che il compilatore Java effettua tra le [[Classi Wrapper|classi wrapper]] degli oggetti e i rispettivi tipi primitivi.

> [!example] 
> ```Java
> Integer i = 7; //qui viene utilizzato l'autoboxing
> /*e diventa */ Integer i = Integer.valueOf(7); //mentre
> int r = i+5;
> //viene convertito in
> int r = i.intValue();
> ```
