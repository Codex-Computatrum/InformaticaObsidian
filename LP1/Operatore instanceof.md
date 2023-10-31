---
author: Simone Parente
tags:
  - Java
---
# Operatore `instanceof`
>[!important]
L'operatore `instanceof` in Java viene utilizzato per verificare se un oggetto è un'istanza di una determinata classe.
L'espressione `rif instanceof Class`
Restituisce true se:
> - `rif` è  sottotipo di `Class`. 
> - `rif` non è `null`.
- 
^instanceof

>[!info] 
> Siano `A` e `B` classi, e sia `B` sottoclasse di `A`:

```java
B beta = new B();  
A alfa = beta;  
System.out.println(beta.getClass() == alfa.getClass()); //Stampa true
```

```java
B beta = new B();  
A alfa = new A();  
System.out.println(beta.getClass() == alfa.getClass()); //Stampa false
```
