(* Funzioni Lista *)

(* Funzione Lunghezza *)
fun lenght [] = 0
  | lenght (_::xs) = 1 + lenght xs;

(* Funzione Inverti Elementi *)
fun inverti [] = []
  | inverti (x :: xs) = (inverti xs) @ [x];

(* Funzione Max *)
fun max [x] = x 
  | max (x::xs) = let
    val maxNext = max xs
in
  if x > maxNext then x else maxNext
end;

(* Funzione appartiene a lista *)
fun appartiene x [] = false
  | appartiene x (y::ys) = (x = y) orelse appartiene x ys;

(* Funzione Rimuovi Duplicati *)
fun rimuoviDuplicati [] = []
  | rimuoviDuplicati (x::xs) =
    if appartiene x xs then
      rimuoviDuplicati xs
    else
      x :: rimuoviDuplicati xs;

(* Funzione Somma Elementi *)
fun sommaElementi [] = 0
  | sommaElementi (x::xs) = x + sommaElementi xs
;

(* Lista *)
val L = [1, 2, 3, 4, 5, 5];

(* Risultati *)
lenght L;
inverti L;
max L;
rimuoviDuplicati L;
sommaElementi L;