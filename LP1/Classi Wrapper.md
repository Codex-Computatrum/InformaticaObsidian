---
author: Simone Parente
tags:
  - Java
---

# Classi Wrapper

>[!summary]
> Per ogni tipo base, Java offre una classe che **ingloba** un valore di quel tipo in un oggetto.
Queste classi servono a trattare i valori base come se fossero oggetti.

Le classi wrapper sono:
- `Byte`, `Short`, `Integer`, `Long`, `Float`, `Double`
- `Boolean`
- `Character`
- `Void`
Tutte le classi wrapper sono **immutabili** (non è possibile modificarne il contenuto) e **final** (non possono avere sottoclassi). Ogni classe wrapper ha un metodo statico `valueOf()` che prende in input un valore del tipo base corrispondente e ritorna un oggetto wrapper che lo ingloba.

```java
Integer n = Integer.valueOf(3);
Double x = Double.valueOf(3.1144);
```