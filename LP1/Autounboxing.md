>[!summary]
> L'autounboxing è la conversione automatica che il compilatore Java effettua tra le rispettive [[Classi Wrapper|classi wrapper]] degli oggetti e i rispettivi tipi primitivi.

>[!example] Esempio
>```Java
Integer n = 7;
Integer i = n + 7;
//vengono convertite in
Integer n = Integer.valueOf(7);
Integer i = Integer.valueOf(n.intValue() + 7);
