
>[!info] 
> Siano `A` e `B` classi, e sia `B` sottoclasse di `A`:

```java
B beta = new B();  
A alfa = beta;  
System.out.println(beta.getClass() == alfa.getClass()); //Stampa true
```

```java
B beta = new B();  
A alfa = new A();  
System.out.println(beta.getClass() == alfa.getClass()); //Stampa false
```
