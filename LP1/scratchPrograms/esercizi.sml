fun reverse lst = 
  let
    fun aux [] acc = acc
      | aux (x::xs) acc = aux xs (x :: acc)
  in
    aux lst []
  end
;

reverse [1,2, 3, 4, 5];
reverse [];

(*3*)

val L = [1,2,3,4,5];

length L;

(*4*)
fun somma lst = 
  let 
    fun aux [] acc = acc
      | aux (x + xs) acc = aux xs (x + acc)
  in 
      aux lst []
  end
;

somma [1, 2, 3 ]
