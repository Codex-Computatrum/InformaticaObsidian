Sia $A$ un insieme e sia $F \subseteq P(A)$, $F$ si dice <span style="color:#ffbe0a">partizione</span> di $A$ se e solo se:
1. $(\forall x \in F)(x \neq \emptyset)$
2. $(\forall x,y \in F) (x \neq y \implies x \cap y = \emptyset)$
3. $x \in F: \bigcup x = A$
#### Esempio 1.
Siano $A$ un insieme e $F \subseteq P(A)$ così definiti:
$$A=\{1,2,3,4,5\}$$
$$F=\{\{1\}, \{2\}, \{3,4\} \}$$
$F$ è partizione di $A$? %%No%%
1. $(\forall x \in F)(x \neq \emptyset)$ ? Si, perché $(\{1\} \neq \emptyset) \land (\{ 2 \} \neq \emptyset) \land (\{ 3,4\} \neq \emptyset)$
2. $(\forall x,y \in F) (x \neq y \implies x \cap y = \emptyset)$ ? Si, perché $\{1\} \cap \{2\} \cap \{3,3\} = \emptyset$
3.  $x \in F: \bigcup x = A$ ? No, $\cup x = \{ 1,2,3,4 \} \neq \{1,2,3,4,5\} = A$
Quindi $F$ non è partizione di $A$, sarebbe stato partizione se fosse stato, per esempio $F=\{\{1\},\{2\}, \{3,4,5\} \}$.