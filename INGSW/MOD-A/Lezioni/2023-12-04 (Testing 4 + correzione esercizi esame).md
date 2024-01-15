## Testing black box
#### SECT
$\text{Strong Equivalence Class Testing}$
Es. prendo il mese luglio e lo testo con il prodotto cartesiano di tutte le classi di equivalenza
Nell'esempio di [[2023-12-01 (Testing 3)#^b1fc47]] abbiamo $5\times 7 \times 2=70$ possibili casi di test.

## Esercizio 3A Giugno 2023
![[giugno2023.pdf]]La signature sarà del tipo `float computeCost(int tokens, boolean isPremium)`
Classi di equivalenza:
- tokens:
	- <span style="color:#00ff00">CE1</span>: $\{1<tokens \leq 256\}$ 
	- <span style="color:#00ff00">CE2</span>: $\{256<tokens<512\}$
	- <span style="color:#ff0000">CE3</span>:$\{tokens \leq 1\}$
	- <span style="color:#ff0000">CE4</span>: $\{tokens \geq 512\}$
- isPremium:
- <span style="color:#00ff00">CE1</span>: $\{true\}$
- <span style="color:#00ff00">CE2</span>:$\{false\}$

\# Casi di test R-WECT: 4
	- 2 per più lungo partizionamento
	- 2 per casi non validi

```java
public class BillingTest{
	@Test
	public void testComputeCostTokenMin256Premium{
		Billing b = new Billing();
		assertEquals(6.4, b.computeCost(128, true)) //128*0.5
	}
}
```



## Esercizio 3A Ottobre 2023
![[ottobre2023.pdf]]
`int calcolaPuntiBonus (float media, int nfc, String ordinamento, boolean erasmus)`

Classi equivalenza:
- media
	- <span style="color:#00ff00">CE1</span>: $\{18\leq media < 24\}$
	- <span style="color:#00ff00">CE2</span>: $\{24 \leq media \leq 28\}$
	- <span style="color:#00ff00">CE3</span>: $\{28<media \leq 30\}$
	- <span style="color:#ff0000">CE4</span>: $\{media<18\}$
	- <span style="color:#ff0000">CE5</span>:$\{media>30\}$
- nfc
	- <span style="color:#00ff00">CE1</span>: $nfc \neq 0$
	- <span style="color:#00ff00">CE2</span>: $nfc = 1$
	- <span style="color:#00ff00">CE3</span>: $2 \leq nfc \leq 20$
	- <span style="color:#ff0000">CE4</span>: $nfc < 0$
	- <span style="color:#ff0000">CE5</span>: $nfc > 20$
- ordinamento
	- <span style="color:#00ff00">CE1</span>: $\text{nuovo}$
	- <span style="color:#00ff00">CE2</span>: $\text{vecchio}$
	- <span style="color:#ff0000">CE3</span>: $\text{ciao}$
	- <span style="color:#ff0000">CE4</span>: $\text{null}$
- erasmus
	- <span style="color:#00ff00">CE1</span>: $\text{true}$
	- <span style="color:#00ff00">CE2</span>: $\text{false}$

Casi validi: 3
Casi non validi: 6

R-WECT  cases = 9



## Esercizio 3A 