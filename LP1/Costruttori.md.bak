>[!info]
>Un costruttore è un metodo avente il nome della classe e nessun tipo di ritorno, possono esisterne di diversi per la stessa classe, ma con parametri diversi.
>```Java
>class Prova{
>	Prova(){
>		System.out.println("Sono un costruttore");
>		}
>}
>```

## Invocazioni di un altro costruttore
>[!tip] 
>Il meccanismo secondo il quale i costruttori possono invocarsi a vicenda si chiama **constructor chaining**.
### Invocazioni esplicite
>[!summary] 
Un costruttore può chiamare un altro costruttore della stessa classe utilizzando la parola chiave `this`, oppure un costruttore della sua superclasse diretta utilizzando `super`.

Queste parole chiavi <span style="color:#ff0000">devono comparire alla prima riga del costruttore</span>, altrimenti avremo un errore di compilazione.
### Invocazioni implicite
>[!summary] 
>Se un costruttore non inizia con una chiamata a un altro costruttore (`this` o `super`, il compilatore inserisce automaticamente una chiamata al costruttore senza argomenti della superclasse.
>Vale a dire, viene inserita l'istruzione `super()` alla prima riga del costruttore.

Nel caso in cui la superclasse non dovesse avere un costruttore senza argomenti, avremo un errore di compilazione.
## Sequenza di inizializzazione di un oggetto
1. Se il costruttore inizia con `super(...)`, passare al costruttore della superclasse.
1. Se il costruttore inizia con `this(...)`, passare al costruttore indicato.
1. Se il costruttore non inizia né con `super` né con `this`, passare al costruttore senza argomenti della superclasse diretta.
2. Eseguire i *blocchi di inizializzazione* e gli *inizializzatori* degli attributi, nell'ordine in cui compaiono nel codice.
>[!attention] Attenzione
>I blocchi di codice marcati `static` vengono eseguiti appena la classe viene caricata in memoria.
