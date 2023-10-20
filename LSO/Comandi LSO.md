## Comandi 

- **pwd**: print working directory 
  
- **cd** : cambia la directory di lavoro
  
- **mdkir**: crea una nuova directory (puoi specificare dove viene creata se specifichi il path)
  
- **rmdir**:  rimuovi una directory (devi specificare il path della directory).
##### ls
mostra una lista in ordine alfabetico del contenuto della o delle directory (possibile indicare quale) 
alcune opzioni:
- l (formato esteso) 
- a anche i file nascosti
- r visita ricorsiva delle sottodirectory (possibile loop infinito).
- i mostra i-number (che è?)
- t ordina per ultima modifica 
#### Link
ln \[nome1] \[nome2]   : associa al nuovo nome (link) nome2 al file esistente name1, non può essere una directory.
- tutti i link allo stesso file hanno lo stesso stato e caratteristiche.
	- non puoi distinguere la entry originale dal nuovo link
	- di questo tipo non possono essere fatti con file presenti su file system diversi
	- con **-s** puoi creare 
		- link a directory
		- link tra file o directory che stanno su file system diversi
		- viene creato un file name2 contenente il path di name1 (link simbolico)


- **du** :  disk usage (visita ricorsivamente le directory e mostra il " disk usage")
  
- **chmod \[permesso] \[filename]** : attribuisce permessi di un file
	- u (proprietario) g (gruppo) o (altri utenti) a (tutti)
	- + (aggiungi) - (togli) =(assegna)
	- r (lettura) w (scrittura) x (esecuzione)
#### chown	  
**chown \[opzione]  \[user]  \[:\[group] ] file...** : cambia proprietario o gruppo primario per uno o più file.
-  se dopo il punto non segue il nome del gruppo, viene attribuito il gruppo principale ove appartiene user
- se dopo il :group non viene indicato il nome dell'utente, viene cambiato solo il gruppo primario (chgrp).

- **touch \[nome]** : crea un nuovo file (possibile specificare la directory di creazione)

- **mv \[options] name...target**: muove il file o directory sotto la directory target 
	- se name e target non sono directory, il contenuto di target viene sostituito da quello di name

- **cp \[opzioni] \[name]....target**: funziona come mv, ma questa volta viene copiato 
  
- **cat \[nomefile]**: mostra il contenuto del file.

- **rm \[r] nome**: rimuove i file indicati
	- se il file è una directory, da messaggio di errore a meno che non si specifichi con -r, che rimuove ricorsivamente tutta la direttrice (elimina tutti i file all' interno)
#### mount
- **mount**: controlla le partizioni montate sulla linux box
	- **-t (argomento)**: tipo di fs
		- ext2 (linux)
		- reiserfs (linux)
		- ext3 (linux)
		- vfat per FAT (win 9x)
		- msdos (DOS)
		- ntfs (win NT)
		- iso9660 (CDROM)
		- hpfs (OS/2)
		- hps (Macintosh)
	- **-o (argomento) opzione**: altra opzione di file system mountpoint
		- rw: lettura e scrittura
		- exec: esecuzione
		- noexec: non esecuzione
		- remount: rimonta un fs
col comando mount è possibile montare diversi tipi di filesystem, basta specificare il file system da montare e il tipo di file system.

per smontare il file system si usa il comando "unmount" specificando il filesystem da smontare
- **fstab** :  imposta il file system che dovrà montare all' avvio del sistema 
	- **noauto** : non montare
	- **users**: ogni utente può montare o smontare un dispositivo 
	- **user**: ogni utente può solo montare un dispositivo , può smontare solo se ha montato il fs


- **echo \[argomenti]**: visualizza gli argomenti in ordine 
- 
- se si lavora su un file non esistente, di solito viene creato automaticamente, è possibile riscriverlo con (>) o accodarlo (>>) , usando il simbolo (<) reindirizzi l' input 

- **cat \[file1] \[file2]** : concatena i file e li scrive sullo standard output 


- il pattern ($) viene sostituito con l' output del comando 
	- con ls equivale al *
	- con echo scrive la riga in input
	- cat prende l' intero contenuto del file 
	- a = S(ls) assegna ad a l' elenco dei file nella directory 
	- touch "$(date)" il file viene chiamato come la data attuale 

#### grep 

- **grep \[opzioni] pattern \[nomefile]**
stampa le righe del file che corrispondono al pattern (è un espressione regolare)
  - caso base: senza caratteri speciali 
	- se il nome non è specificato, legge da standard input, consente la concatenazione di file 
	- con -v stampo le righe che non corrispondono al pattern 
	- con -c visualizzo solo il numero di occorrenze della stringa
	- con -i case sensitive
	- -n numero riga 
	- l' espressione regolare è un pattern che descrive un insieme di stringhe 
		- "." (qualunque)
		- "exp*" zero o piu occorrenze di exp
		- "^exp" exp all' inizio del rigo
		- "exp\$" exp alla fine del rigo
		- "\[a-z]" un carattere in un intervallo 
		- "\[^a-z]" non presente in questo intervallo 
		- "\\<exp" all'inizio della parola 
		- "exp\\>" alla fine di una prola
		- "exp{N}" compare n volte
		-  "exp{N,}" compare almeno n volte 
		-  "exp{N,M}" compare almeno N volte e al piu di M
		- "\[\[:CLASS:]]" carattere in CLASS
			- alpha: alfabetici
			- alnum: alfanumerici
			- digit: cifre
			- upper: maiuscoli 
			- lower: minuscoli 
	- exdended regular expression:
		- exp +: una o piu occorrenze 
		- exp?: zero o una occorrenza
		- exp1 | exp2 : 1 o l' altra
		- (exp): equivalenza, serve a stabilire l' ordine di valutazione
	- in grep vanno usati con \\ che precede
		  in egrep no.

- **wc (word count) \[opzione]\[file]** : fornisce il numero delle righe, parole o caratteri in un file. senza opzioni fornisce in ordine queste 33 
	- -c caratteri
	- -w parole
	- -l righe 
### Processi

- **ps** : fornisce i processi presenti 
	- \# al terminale corrente 
		- pid= pid , tty= terminale (virtuale) , Time= tempo di CPU usato, CMD= comando generante del processo 
	## selezione 
	 - senza nulla sono quelli lanciati dalla shell corrente
	 - -u (nome): processi di quell'utente
	 - -a (All) tutti i processi 
	## formato
	- senza nulla: PID, terminale, ora di esecuzione, comando
	- -f (full) anche UID, PPID, argomenti
	- -F (Full) anche altro 
	- -o elenco_campi:  visualizza i campi specificati 

## Sort \[options] \[file]

- riordina e fonde insieme il cntenuto dei file, o riordina le linee in input 
	senza opzioni avviene in base al primo campo e in ordine alfabetico
	- **-f** : ignora maiuscole e minuscole 
	- **-n** : chiave di ordinamento numerica e non testuale 
	- **-r** : senso decrescente 
	-  **-o fileout** : output inviato a fileout invece che output standard 
	-  **-t s** : s come separatore di campo 
	- **- k s1,s2** : usa i campi da s1 a s2-1 come chiavi di ordinamento 

### head \\ tail 
- **head \[numero] file** : visualizza le prime n righe di un file , 10 se vuoto  
- **tail \[numero] file** : visualizza le ultime n righe di un file , 10 se vuoto  
## pipe ( | ) 

- concatena l'output di una funzione nell' input di un altra ( quello di sinistra come input per quello di destra )
#### Comandi concatenabili 
- inizio pipe:
	echo, ls, (e tutti quelli che scrivono su stdout)
	- anche al centro: 
	  wc,sort, uniq, grep, cat, head, tail 
	- senza argomenti leggono  su stdin e scrivono su stdout 
	- solo a fine pipe : less (paginatore interattivo)


## script 

uno script shell bash inizia con: #!/bin/bash nel file 
	 ha permesso d' esecuzione 
	 il resto del file contiene comandi di shell 
	  si possono scrivere le stesse cose che nel prompt 
si esegue conn ./nome_file

è possibile creare degli script interattivi con il comando read \$variabile 
sintassi:
#! : sto indicando che il file è uno script 
il resto dice  qual' è l'interprete dello script. 
come risultato viene invocato l' interprete passandogli come argomento il nome dello script 
- variabili definite:  precedute da "$"
	-  0 : nome  dello script 
	- 1...9 : parametri da riga di comando 
	- \# : numero di parametri ricevuto 
	- * : tutti i parametri di una stringa singola  (su un rigo)
	- @ : tutti i parametri in stringhe separate (va a capo) 
	- ! : process ID (PID) processo corrente
	- ? : exit status dell' ultimo comando eseguito 
	- USER : username dell' utente che avvia lo script 
	- HOSTNAME : l' hostname della macchina da dove è partito lo script 
	- SECONDS : numero di secondi da quando è partito lo script
	- RANDOM : ogni volta che è referenziato , ritorna un numero diverso 
	- LINENO : linea corrente del bash script 

##### operatore condizionale 
if\[condizione] {} : è un if

### cicli 
##### While 
 finchè la condizione è vera 
while comando 
	do 
		cose 
	done

#### until
 finchè la condizione è falsa

until condizione 
do 
	cose 
done 
#### For

for var in lista_valori 
	do 
		cose 
	done

#### case
 case stringa in 
		stringa_caso_1) cose ;;
		stringa_caso_2) cose ;;
	
esac




