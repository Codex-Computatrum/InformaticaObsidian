>[!warning] Importante
I metodi vanno cercati nelle classi dei tipi *dichiarati* degli oggetti e nella superclasse (oltre che in `Object`).
Se esiste un override in una sottoclasse e il tipo effettivo dell'object è quello della sottoclasse, la firma scelta sarà quella dell'override

---
## Visibilità dei metodi
>[!info] 
>Siano `A` e B delle classi precedentemente dichiarate, e sia `B` sottoclasse di `A`.
```java
public class Main {  
	public static void main(String[] args) {  
		B beta = new B();  
		A alfa = beta;  
	}
```
L'object `alfa` potrà accedere a tutti i metodi di `A` e tutti quelli di `B`.

---
## getClass()
Questo metodo restituisce l'oggetto di tipo Class del riferimento dell'oggetto su cui viene applicato.
>[!info] 
>Siano `A` e B delle classi precedentemente dichiarate, e sia `B` sottoclasse di `A`.
```Java
public class Main {  
	public static void main(String[] args) {  
		B beta = new B();  
		A alfa = beta;  
		System.out.println(alfa.getClass()); //ritornerà B perché il riferimento 'beta' è di tipo 'B'
	}
}
```
---
## Operatore `instanceof`
