

è presente nella gran parte dei sistemi operativi UNIX like.

#### /dev 

tutti i file al suo interno rappresentano dispositivi 
- Character device : dispositivi di trasmissione e trasferimento 
	- dsp\[0]: dispositivo audio. 
	- lp\[0]: porta parallela. 
- Block device : Dispositivi di memorizzazione e conservazione 
	- hd\[a]: hdd ide. 
	- sd\[a]: hdd scsi, memory stick, memory card, etc...




partiamo con un disco di destinazione:
![[Pasted image 20231207114448.png]]

il comando è il seguente:

$$\text{dd if=/dev/sda of=/mnt/dest/dd\_image/sda.dd bs=2048 conv=noerror, sync}$$
Dove:
- **IF** = input file \[sorgente /sda].
- **OF** = output file \[file immagine sda.dd].
- **BS**= block size in byte, di default 512 \[in questo caso 2048 byte].

- **CONV**= in  base ai parametri 
	- noerror= continua ad elaborare in caso di errore.
	- sync= sostituisce i blocchi non letti con NULS (sincronizza la dimensione della destinazione con la sorgente).


- Comandi avanzati 
	- **SKIP**= \[n] salta la lettura del n blocchi di memoria partendo dall' inizio.
	- **COUNT**= \[n] l' elaborazione termina dopo aver letto n blocchi di memoria. 
	- Di solito servono per acquisire una singola partizione o evitare  


esempio di acquisizione di una sola partizione 

$$\text{dd if=/dev/sda of=/mnt/dest/dd\_image/sda\_{p2.dd} skip=2099199 count=6289408}$$

$$\text{dd if=/dev/sda of=/mnt/dest/dd\_image/sda\_{p2.dd} bs=1024 skip=3000000 count=1000000}$$



#### Calcolare l'hash 

- calcoliamo l' hash della sorgente sda e lo salviamo in un file sda\_orig.hash.
$$\text{md5sum /dev/sda > /mnt/dest/dd\_image/sda\_orig.hash}$$
$$\text{cat /mnt/dest/dd\_image/sda\_origin.dd}$$

- con lo stesso hash sda lo salviamo in un file sda_dd.hash. 

$$\text{md5sum /mnt/dest/dd\_image/sda\_{orig.hash} > /mnt/dest/dd\_image/sda\_dd.hash}$$
$$\text{cat /mnt/dest/dd\_image/sda\_dd.hash}$$

- Durante l' elaborazione di una copia. 
$$\text{dd if=/dev/sda bs2048 | tee /mnt/dest/dd\_{image/}sda.dd |}$$
$$ md5sum > /mnt/dest/dd\_{image/} sda.hash$$

-  **TEE** = biforca/duplica lo stream (una si usa per il file immagine, l' altra vien trasmesso al comando successivo md5sum).
