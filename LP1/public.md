---
author: Simone Parente
tags:
  - Java/modifiers
---
È il più generoso, l'accesso è consentito *quasi* ovunque.
>[!error] 
><ul><u>Il fatto che un metodo sia public non implica il fatto che possa essere accessibile da qualsiasi package.</u></ul>
>In caso ci trovassimo davanti a una classe private `B`(dichiarata all’interno di una classe public, chiamiamola `A`), i metodi di `B` non sarebbero accessibili esternamente alla classe `A`.