---
author: Mario Penna
tags:
  - definition/property
---
## Differenze tra strutture algebriche

$$
(S,*)
$$

| Semigruppo | Monoide | Gruppo | Gruppo Abeliano |
| --- | --- | --- | --- |
| Associativo | Associativo | Associativo | Associativo |
|  | Elemento Neutro | Elemento Neutro | Elemento Neutro |
|  |  | $\forall A \in S$, A è invertibile | $\forall A \in S$, A è invertibile |
|  |  |  | Commutativo |

## Anello e Campo

$$
(A, +, \cdot)
$$

| Anello | Anello Commutativo | Anello Unitario | Anello Unitario Commutativo | Dominio d’Integrità (Anello) | Campo |
| --- | --- | --- | --- | --- | --- |
| (A, +) Gruppo Abeliano | (A, +) Gruppo Abeliano | (A, +) Gruppo Abeliano | (A, +) Gruppo Abeliano | (A, +) Gruppo Abeliano | (A, +) Gruppo Abeliano |
| (A, •) Semigruppo | (A, •) Semigruppo | (A, •) Monoide | (A, •) Monoide | (A, •) Monoide | (A, •) Gruppo Abeliano |
| • distributiva rispetto a + | • distributiva rispetto a + | • distributiva rispetto a + | • distributiva rispetto a + | • distributiva rispetto a + | • distributiva rispetto a + |
|  | $(A,\cdot)$ commutativa |  | $(A,\cdot)$ commutativa | $(A,\cdot)$ commutativa | $(A, \cdot)$ è commutativa perché è un gruppo abeliano |
|  |  |  |  | Non ha divisori dello zero | Non ha divisori dello zero |

## Anello Booleano

- Anello Commutativo Unitario
- $(\forall x \in A)(x^2=x)$
- $(\forall x \in A)$$(x=-x)$

## Proprietà strutture algebriche

### Commutatività

$\forall a, b \in S (a*b = b*a)$

### Associatività

$\forall a, b, c \in S ((a*b) *c = (a*b)*c)$

### Distributività rispetto a +

$\forall a,b,c \in S (a*(b+c) = a*b+a*c)$

### Elemento Neutro a Dx e Sx

$\forall a \in S (\epsilon * a = a = a * \epsilon)$

### Elementi Simmetrizzabili a Dx e Sx

$\exists b \in S (a*b = b*a = \epsilon)$

### Elementi Cancellabili

N.B. deve esserlo sia a dx che a sx

$\forall x,y \in S ((xa = ya \rightarrow x=y) \land (ax = ay \rightarrow x=y))$