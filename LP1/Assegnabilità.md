La **relazione di assegnabilità** (o _**compatibilità**_) tra tipi stabilisce quando è possibile **assegnare un valore** di un certo tipo `T` ad una variabile di tipo `U`.

Si dice che `T` è **assegnabile** ad `U` se: ^641102
- `T` è _sottotipo_ di `U`, oppure  `T` e `U` sono tipi base e c’è una conversione implicita da `T` a `U`. ^b1919b

Questa relazione si applica nei contesti di:

- Assegnazione `a = exp`
- Chiamata a metodo `x.f(exp)`
- Chiamata da metodo `return exp`