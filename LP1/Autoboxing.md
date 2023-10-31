---
author: Simone Parente
tags:
  - Java
---
>[!summary]
> L'autoboxing è la conversione automatica che il compilatore Java effettua tra i tipi primitivi e le rispettive [[Classi Wrapper|classi wrapper]] degli oggetti.

>[!example] Esempio
>```Java
Integer n = 7;
//viene convertito in
Integer n = Integer.valueOf(7);
