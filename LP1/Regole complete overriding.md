---
author: Simone Parente
tags:
  - Java
---

- I metodi “padre” devono essere <span style="color:#ff0000"><b>non private, non static e non final </b></span>.
- I due metodi devono avere <span style="color:#00ccff"> <b>identica signature</b></span> (nome del metodo e tipo dei parametri formali).
- Il tipo di ritorno può essere **uguale o sottotipo** del **tipo di ritorno originario**.
- Se il metodo della sottoclasse dichiara di lanciare un’`exception` checked, tale tipo deve essere un **sottotipo di una delle eccezioni dichiarate** **dall’originale**, il metodo figlio può lanciarne di più o di meno.
    - Le eventuali eccezioni checked dichiarate dal metodo nella sottoclasse, devono essere tipi posti al di sotto nella gerarchia delle eccezioni dal metodo nella superclasse.