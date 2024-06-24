---
author: Simone Parente
tags:
  - to-do
  - Java
---

>[!info] 
>Le Exceptions sono un modo standard di segnalare situazioni anomale al chiamante di una funzione.

Per lanciare un'eccezione bisogna seguire i seguenti passaggi:
1. Dichiarare che il metodo lancia il tipo (o il tipo della classe padre) di quell'eccezione
	```Java
	class A{
		public static void main() throws Exception{
		}
	}


2. Lanciare l'eccezione all'interno di un blocco `try`.

	```Java
	class A{
		public static void main() throws Exception{  
			try{  
				new Exception();  
			}  
		}
	}



3.  Creare uno o più blocchi `catch` che possano catturarla
	```Java
	class A{  
		public static void main() throws Exception{  
			try{  
				new Exception();  
			} catch(Exception e){  
				//succede qualcosa  
			}  
		}  }
---


>[!error] Attenzione
>Non dichiarare nessun blocco `catch` (oppure `finally`, che vedremo dopo) dopo un blocco `try` causa un errore di compilazione.
### Il blocco `finally`
>[!tldr] TL;DR
Il blocco `finally` viene eseguito **sempre**, a prescindere da praticamente qualsiasi cosa.

Nel caso in cui l'exception **NON** venisse catturata, verrà comunque eseguito il blocco `finally`, ma non il codice presente all'esterno di esso, il `finally` viene eseguito anche dopo eventuali istruzioni di `return` all'interno dei blocchi `try` o `catch`.
Nel caso in cui l'`Exception` venisse catturata, verrà eseguito anche eventuale codice dopo il blocco `finally`.

## Ciclo di vita di un'exception
Un lancio di un’eccezione interrompe il flusso di esecuzione, se non viene catturata localmente, il metodo corrente **termina** e l’`Exception` viene passata al chiamante, il quale avrà la possibilità di catturarla a sua volta, in caso ciò non avvenisse, l’`Exception` continuerà a risalire lo **stack di attivazione** fino a raggiungere il `main`. Se neanche il `main` la cattura l’`Exception` il programma termina e la JVM stampa il contenuto dell’`Exception` (**stack trace**).
### Catch delle `Exceptions`
>[!tldr] TL;DR
>Il codice che assume la responsabilità di gestire un’exception viene inglobato in una clausola catch, il codice che potrebbe lanciare eccezioni dovrà essere inglobato in un blocco marcato try.

```Java
try{
	//codice che potrebbe lanciare exception
} catch (Eccezione1 e){
	//codice che gestisce un eccezione di tipo Eccezione1 (o suoi sottotipi)
} catch (Eccezione2 e){
	//codice che gestisce un eccezione di tipo Eccezione2 (o suoi sottotipi)
} finally{
	//codice che viene eseguito a prescindere, che ci siano o meno exception
}
//nel caso in cui l'exception NON venisse catturata, verrà comunque eseguito il blocco finally,
//ma non il codice presente all'esterno di esso, il finally viene eseguito anche dopo eventuali
//istruzioni return all'interno dei blocchi try o catch

//nel caso in cui l'exception venisse catturata, verrà eseguito anche il codice dopo finally.
```

^try-catch
## Vincoli sintattici
>[!summary] In breve
Sia `catch` che `finally` sono opzionali, ma **almeno uno dei due deve essere inserito**, l’inserimento del solo `try` causerebbe un errore di compilazione.
Se esiste un blocco `finally`, esso **deve apparire** per ultimo.
## Gerarchie

```plantuml
exception Object
exception Throwable
exception Error 
exception Exception
exception RuntimeException
exception  Error_SubClasses
exception  RuntimeException_SubClasses
exception  Exception_SubClasses

'-----------------------------'

Object <|-- Throwable

Throwable <|-- Error
Throwable <|-- Exception

Exception <|-- RuntimeException
Exception <|-- Exception_SubClasses

RuntimeException <|-- RuntimeException_SubClasses

Error <|-- Error_SubClasses

```

Le sottoclassi di `Error` e `RuntimeException` sono dette <span style="color:#ff0000">eccezioni  unchecked</span> ^52c250
- In particolare, la classe `Error` rappresenta eccezioni lanciate dalla JVM, in genere non vengono catturate perché il programma non sarebbe in grado di riprendersi in queste occasioni.
- La classe `RuntimeException` rappresenta eventi eccezionali ma dovuti al programma, anche queste non vengono generalmente catturate, sarebbe buona norma risolvere i problemi che le causano.
>[!fail] Attenzione
>Le eccezioni <span style="color:#ff0000">unchecked</span> **non devono** essere catturate
## Creazione di nuove `Exceptions`<span style="color:#ff0000"><span style="color:#ff0000"><span style="color:#ff0000"><span style="color:#ff0000"><span style="color:#ff0000"><span style="color:#ff0000"></span></span></span></span></span></span>
È possibile creare nuove eccezioni in questo modo: 
```Java
class MiaEccezione extends Exception { ... } // (o estendendo qualunque altra sottoclasse di Exception)
``` 
Dal momento in cui abbiamo questa dichiarazione, si potrà lanciare una `Exception` del tipo (**checked**) `MiaEccezione`.
## Eccezioni catturate
>[!summary] In breve
Una clausola `catch(E e)` cattura ogni oggetto-eccezione di **tipo** `E` **o suo sottotipo**.

Una `exception E` verrà catturata dal primo `catch` in grado di catturarla.
Un `catch` non utilizzabile (ad esempio un `catch` di una classe padre seguito da un `catch` di una sua classe figlia) darà un errore di compilazione (non sarebbe mai raggiungibile).
- Eventuali eccezioni lanciate da un `catch` non potranno essere catturate da altri blocchi catch dello stesso `try`.
- Se necessario, i `try` - `catch` possono essere annidati.
È preferibile utilizzare <span style="color:#ffbe0a">diverse</span> `catch` che catturano <span style="color:#ffbe0a">diverse</span> `Exception` piuttosto che usarne una sola che le cattura tutte.
### Esempio
La classe `IndexOutOfBoundsException` ha due sottoclassi: `ArrayIndexOutOfBoundsException` e `StringIndexOutOfBoundsException`, è possibile creare un `catch(IndexOutOfBoundsException e)` che potrà catturarle entrambe.
