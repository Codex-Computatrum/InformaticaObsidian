>[!summary] 
>Sono oggetti immutabili, come i [[Classi Wrapper|tipi wrapper]].
È possibile creare stringhe in questi modi:
```Java
String s1 = new String("abcdef");
String s2 = "abcdef";
```

## String Pool
>[!info] 
>I letterali `String` occupano molto spazio, quindi la JVM riserva un'area specifica per la memorizzazione di questi ultimi.
>Quando il compilatore incontra un letterale `String`, controlla se esso è presente nel pool:
>- Se è presente, viene interpretato come un riferimento all'oggetto `String` esistente.
>- Altrimenti viene creato un nuovo oggetto `String` e aggiunto al pool.

Questo meccanismo funziona perché i letterali `String` sono immutabili.
La classe  `String` sovrascrive il metodo `equals` in modo da controllare l'uguaglianza del valore dei due oggetti, a differenza di `StringBuffer` e `StringBuilder` che lo ereditano da `Object` ed è equivalente a `==`.
## StringBuffer e StringBuilder
>[!info] 
>Sono classi simili a `String`, con la differenza che queste ultime sono mutabili, in particolare `StringBuffer` è **thread-safe**.

