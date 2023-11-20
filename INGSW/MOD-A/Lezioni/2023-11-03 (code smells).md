---
author: Simone Parente
tags:
  - todo
---
di nuovo clean code
La consegna di codice al mometo avviene tramite immagini docker ($\implies$ imparare)
Lezione su restAPI in futuro?
## Functions
Come ottenere codice di miglior qualità
### Ridurre il numero di parametri
- Tramite "wrapping"
	- Invece di passare due variabili int, ad esempio, per indicare un punto, è possbile passare un object di tipo Point, che contiene queste due variabili.
- Tramite variabili d'istanza
### Commenti
- Riscrivere codice scritto male $>$ commentare codice scritto male
- Va bene avere commenti, ma un paio di righe, non di più
- Meglio avere codice autoesplicativo che un codice illeggibile commentato
- Non commentare inutilmente il codice (slide perfetta)
>[!quote] 
>Quando vi capiterà di dover scrivere un commento, pensateci bene e cercate di scoprire se non esiste un modo per esprimere la stessa cosa nel codice

I metodi "vicini" si suppone facciano cose "inerenti"
## Gestione degli errori
Come gestire gli errori?
- un botto di if
- un botto di try-catch (o equivalenti) (PREFERIBILE in generale, meglio se vengono utilizzate catch "mirate" e non un unico blocco catch per tutto)
<span style="color:#ff0000">NON CREARE FUNZIONI CHE RITORNANO NULL</span>, potrebbero causare, ad esempio `NullPointerException`, [[Exceptions#^52c250||eccezione unchecked]].
### Classi
>[!summary] 
>Le classi **devono** essere piccole, avere un'unica responsabilità, non usare parole come "Super", "Manager", "Processor" (<u>non da sole</u>, per es. "EmployeeProcessor" andrebbe bene).
>Usare come nome una breve descrizione senza usare parole tipo "and", "but", etc.

----
$$\text{Codice che funziona} \neq \text{Clean code}$$
## Code Smells e Refactoring ^codesmells
Bad smell (anti-pattern): qualcosa su cui approfondire
(da sapere 5-6-7 refactoring principali usati spesso)
[Refactoring](https://www.refactoring.guru)
### Tipi di code smell
#### Bloaters
Metodi o classi che nel corso dell'evoluzione del software sono diventati troppo grandi ed è diventato difficile lavorarci. Esempi: metodi lunghi, classi grandi, metodi con troppi parametri.
#### Object Orientation Abusers
Applicazione sbagliata dei principi della programmazione a oggetti:
- Classi alternative con diverse interfacce (?)
- Switches
- Field temporanei
#### Change preventers
Situazioni presenti nel codice che rallentano le modifiche:
Shotgun surgery: per una singola modifica devo fare infinite piccolissime modifiche in giro per le classi ed i package
#### Dispensables
>[!quote] [Refactoring.guru](https://refactoring.guru/refactoring/smells/dispensables)
>A dispensable is something pointless and unneeded whose absence would make the code cleaner, more efficient and easier to understand.
Qualcosa di cui si può fare a meno
#### Couplers
>[!quote] 
>All the smells in this group contribute to excessive coupling between classes or show what happens if coupling is replaced by excessive delegation.

### Refactoring
Dato un blocco di codice, iteriamo per migliorarlo fino a quando abbiamo risorse e tempo a sufficienza per farlo. Niente cambia da parte dell'utente, vengono fatti solo cambiamenti interni al codice (partendo dal problema più grande).
[Principali refactorings](https://refactoring.guru/refactoring/techniques)