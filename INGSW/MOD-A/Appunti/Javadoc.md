---
author: Simone Parente
tags:
  - Java/docs
---

# JavaDoc
>[!summary] In breve
>Strumento che permette di documentare i file sorgente di un programma all'interno dei sorgenti stessi, utilizzando un particolare formato.

>Commenti che descrivono packages, interfaces, metodi, attributi.
## Struttura
>Sono commenti posti sempre prima della dichiarazione dell'elemento e devono descriverlo in modo sintetico.

>[!example] Esempio
>```Java
/** 
>* Prints a String and then terminates the line.  This method behaves as   * though it invokes \{@link \#print(String)} and then  
 >* {@link \#println()}.  
 >* 
 >* @param x  The {@code String} to be printed.  
 >*/
> public void println(String x)

Questo commento è composto da:
- Un paragrafo che riassume lo scopo del metodo
- Una riga vuota che separa la descrizione dai parametri
- I tag Javadoc (ad esempio `@param`), che indicano le componenti dell'oggetto che sta venendo commentato
### Tags
>Un tag è una stringa del tipo: `@nome commento`, dove `nome` è il tipo di informazione che si sta dando, mentre `commento` è l'informazione.

>[!important] Ordine dei tag
>1. `@author Nome Cognome`: autore dell'elemento (se gli autori sono più di uno, si scrivono su diverse righe).
>2. `@param <nome parametro>`: breve descrizione del parametro, se ci sono più parametri, rispettare l'ordine in cui sono dichiarati
>3. `@return <descrizione>`: breve descrizione di ciò che viene ritornato dal metodo
>4. `@exception <nome eccezione> <descrizione>`: descrizione delle circostanze che determinano il lancio dell'eccezione.

