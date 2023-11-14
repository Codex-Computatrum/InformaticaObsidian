---
author: Simone Parente
tags:
  - UML/statecharts
---

# UML Statecharts
>[!tip] Tips
>1. Ogni stato dovrebbe avere almeno una transizione entrante ed una uscente.
>2. Se diversi stati hanno la stessa condizione di entrata o uscita, considera l'uso di stati composti.
>3. Assicurati di non modellare situazioni non-deterministiche (se non è il tuo obbiettivo).
>4. Al massimo può esserci **uno stato** attivo per ogni regione.

Uno statechart è composto da [[Stati|stati]] e [[Transizioni|transizioni]]
![[Transizioni]]
![[Stati]]
### Esempi
>[!example] Lampada con un unico bottone
>```plantuml
!theme crt-amber
[*] -> Off
Off --> On : click()
On --> Off : click()

>[!example] Contatore in Java
>>```plantuml
!theme crt-amber
state Incrementa
state Decrementa
[*] --> Incrementa
Incrementa --> Incrementa : flick() [count<10] count++
Incrementa --> Decrementa : flick() [count==10] count--
Decrementa --> Decrementa : flick() [count>0], count--
Decrementa --> Incrementa : flick() [count==0], count++

```Java
public class Counter { 
	private int count = 0;
	private String mode = "incrementa";
	public void flick() {
		if(mode.equals("incrementa")) 
			count++;
		else 
			count--; 	
		if(count==10) 
			mode = "decrementa"; 
		else if (count==0) 
			mode = "incrementa"; 
	}
 }
```

>[!example] Finestra in un sistema operativo
>```plantuml
'!theme superhero-outline
'!theme blueprint
'!theme crt-amber
!theme toy
state Visible{
Windowed --> Maximized: max()
Maximized --> Windowed: min()
}
>
state Minimized{
>
}
>
Visible --> Minimized: minimize()
Minimized --> Visible[H]: taskbarClick()
