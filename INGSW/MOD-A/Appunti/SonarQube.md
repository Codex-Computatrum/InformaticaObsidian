---
author: Simone Parente
tags:
---
### Qualità del software
>Un software di qualità è tale quando soddisfa requisiti specifici e si conforma a determinati standard.

Per valutare la qualità di un software esistono due approcci, l'analisi *statica* e l'analisi *dinamica*.
#### Analisi statica
>È eseguita sul codice sorgente puro, senza necessità di eseguirlo.

L'analisi viene fatta per cercare:
- [[2023-11-03 (code smells)|Code smells]]
- Bugs
- Problemi di sicurezza
- Codice duplicato o troppo codice troppo complesso
- Dipendenze (e analizzarle anche queste ultime)
- ecc.
Ѐ praticamente impossibile andare a analizzare staticamente il codice manualmente, soprattutto se si parla di codebases di migliaia di righe, questo è uno dei motivi per cui si utilizzano software come SonarQube.
#### Analisi dinamica
>Eseguita durante l'esecuzione del software

Gli aspetti su cui si sofferma sono:
- Debugging
- Profiling (misurare la quantità di spazio o di tempo "utilizzato" per determinati metodi)
- Software testing (approfondito in futuro)
- etc.

---
## SonarQube
>[!summary] In breve
>SonarQube è una piattaforma open-source progettata per valutare la qualità del codice. Analizza il codice e fornisce un feedback sulle pratiche di sviluppo e su eventuali errori.
### Issues

^issues

>[!summary] Ne esistono di 3 tipi
>- [[SonarQube#^bugs|Bugs]]
>- [[SonarQube#^vulnerabilita|Vulnerabilità]]
>- [[SonarQube#^codesmells|Code Smells]]
#### Bugs ^bugs
>Errori di programmazione che possono causare errori o comportamenti non previsti a runtime (Affidabilità del codice).

>[!example] Esempio
>![[bugExample.png]]
#### Vulnerabilità ^vulnerabilita
>Parti di codice che possono essere attaccate da utenti malintenzionati (Sicurezza del codice).

>[!example] Esempio
>![[vulnerabilityExample.png]]

#### Code Smells ^codesmells
 >Errori che rendono il codice difficile da capire e manutenere
 
 >[!example] Esempio
 >![[codeSmellExample.png]]
#### Gravità degli issues
In principio erano:
- <span style="color:#ff0000">Blocker</span>
	Perdite di memoria, connessioni JDBC non chiuse,ecc.
- <span style="color:#ff0000">Critical</span>
	In genere causato da errori di sicurezza, ad esempio un blocco [[Exceptions#^try-catch|catch]] vuoto o un pericolo di SQL Injection.
- <span style="color:#ffbe0a">Major</span>
	Può causare **seri problemi di produttività** per gli sviluppatori, alcuni esempi sono: codice duplicato e parametri inutilizzati.
- <span style="color:#fff700">Minor</span>
	Possono causare problemi di produttività allo sviluppatore, possono essere: metodi con troppe linee di codice, costrutti `switch` con meno di due casi.
- <span style="color:#fff700">Info</span>
	Semplici osservazioni.
Dalla versione 10.2 sono stati mappati in:
- <span style="color:#ff0000">High</span>
- <span style="color:#ffbe0a">Medium</span>
- <span style="color:#fff700">Low</span>
#### Ciclo di vita degli issues
Gli issues possono avere diversi *stati*:
- `Open`: settato automaticamente quando SonarQube trova un nuovo problema.
- `Confimed`: l'esistenza dell'problema è stata confermata manualmente da un utente.
- `Resolved`: settato manualmente per indicare che la prossima analisi dovrebbe far passare l'issue allo stato `Closed`
- `Reopened`: settato automaticamente quando SonarQube rileva che i problemi precedentemente trovati non sono stati risolti.
- `Closed`: settato automaticamente quando SonarQube rileva che un issue è stato effettivamente risolto.
### Regole
> SonarQube ha degli insiemi di regole, che sono pratiche e standard di programmazione che dovrebbero essere seguiti. Se il codice sorgente analizzato viola una regola, viene creato un [[SonarQube#^issues|issue]].

### Quality gate
>Insieme di condizioni imposte dall'organizzazione sulla qualità del codice.

>[!example] Esempio
>- Non deve esserci nessun issue di livello <span style="color:#ffbe0a">Medium</span> o superiore, oppure
>- ![[qualityGateCond.png]]

