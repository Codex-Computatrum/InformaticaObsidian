---
author: Simone Parente
Lezione:
---
## Network programming
Per *network programming* si intende la creazione di applicazioni che funzionano su dispositivi diversi, potenzialmente in simultanea, tramite una rete. L'infrastruttura su cui si basano queste applicazioni è standardizzata e la maggior parte dei processi non devono essere gestiti, se ne occupano i socket (black box).
### Come funziona un socket TCP (Java - C)
![[socketCJava.pdf]]
In questo esempio vediamo due programmi scambiarsi delle stringhe, ma in generale delle applicazioni si scambiano delle strutture dati, in generale, i formati più comuni per lo scambio di informazioni sono [[2023-10-20 12.30-14.30 XML|XML]], YAML e JSON.
### XML
![[2023-10-20 12.30-14.30 XML]]
### YAML
>YAML (Yaml Ain't Markup Language (sì, si chiama davvero così)), è un linguaggio creato appositamente per essere minimale e facilmente leggibile dagli esseri umani.
 
A differenza di XML, i contenuti YAML sono definiti tramite indentazione (NB: non si usa un'indentazione TAB-based, ma solo tramite *whitespaces*).
In YAML i nomi e i valori sono separati da i due punti (colon) (`:`).
#### Liste
Una lista può essere definita in due modi:
- Una struttura i cui elementi sono separati da trattini (`-`).
- Una sequenza di elementi separati da virgole all'interno di parentesi quadre: `(\[E1,E2,...\])`, come in SML.
#### Dizionari
Un dizionario è rappresentato da coppie di elementi - valori separati da virgole all'interno di parentesi graffe: 
`(\{Nome1:Val1, Nome2:Val2, ...})`
#### Esempi
```YAML
person:
  personid: 77
  firstName: John
  lastName: Doe
```
Abbiamo così definito una persona di nome `John Doe`, con ID `77`.
```YAML
people:
  -person:
    personID: 77
    firstName: John
    lastName: Doe
  -person:
    personID: 78
    firstName: Alice
    lastName: Doe
```
Questa invece è una lista di persone

È anche possibile definire campi di una struttura come un dizionario, per esempio:
```
person: {personid: 77, firstName: John, lastName: Doe}
```
### JSON
> Formato utilizzato per lo scambio di dati, facilmente leggibile dagli umani, facilmente computabile e basato sulle convenzioni del linguaggio C. È considerato il linguaggio per lo scambio di dati ideale (ed è uno dei più usati).
#### Sintassi
I nomi dei campi sono definiti tra virgolette (perché sono delle stringhe), seguiti da due punti (:) e il valore.
NB: l'indentazione non è necessaria, ma utile per visualizzare meglio i dati.
È possibile creare dei *JSON objects* come segue:
`{"Name1": Value1, "Name2": Value2, ...}`
Oppure degli array:
`["Name1": Value1, "Name2": Value2, ...]`
I valori sono definiti con una sintassi simile a quella del C:
- Stringhe: `"name": "Bob"` (all'interno di virgolette)
- Numeri (int, float, double): `"age: 27"`, `"weight":60.5"`
- Array: `"pets": ["cat", "dog"]`, `"siblings": []`
- Valori booleani: `"isAlive": true`
- Valori nulli o non disponibili: `"phoneNumber": null`
#### Esempi
- Definizione di una persona come visto precedentemente per `YAML`.
```JSON
{
	"person": {
		"personID": 77,
		"firstName": "John",
		"lastName": "Doe"
	}
}
```
- Definizione di una lista di persone utilizzando un array
```JSON
{
	"people":[
		"person":{
			"personID": 77,
			"firstName": "John",
			"lastName": "Doe"
		},
		"person":{
			"personID": 78,
			"firstName": "Alice",
			"lastName": "Doe"
		}
	]
}
```
È possibile semplificare la sintassi rimuovendo il field `person`:
```JSON
{ 
	"people": [ 
		{ 
			"personID": 77,
			"firstName": "John",
			"lastName": "Doe" 
		}, 
		{ 
			"personID": 78,
			"firstName": "Alice", 
			"lastName": "Doe" 
		} 
	] 
}
```