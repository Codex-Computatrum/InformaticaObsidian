finLst = [0, 1, 2, 3] --Lista finita di numeri naturali
natLst = [0..] --Lista infinita di naturali
	take 100 natLst --ritorna i primi 100 numeri naturali
	let a = take 1000 natLst --Associa ad a la lista dei primi 1000 numeri naturali
posLst = [1..] --Lista infinita di positivi
oddLst = [1,3..] --Lista infinita di dispari (non negativi)
evenLst = [0,2..] --Lista infinita di pari (non negativi)
negLst = [-1,-2..] --Lista infinita di negativi
zeros = [0,0..]    --Lista infinita di 0
ones = [1,1..]     --Lista infinita di 1
zeroOneTwo = 0 : 1 : 2 : zeroOneTwo --Lista infinita di 0 1 2 0 1 2 ...
	--Prendi tutti gli elementi uno alla volta e se il modulo è uguale a 0 aggiungilo alla nuova lista
multiple p numlst = [n | n <- numlst, n 'mod' p == 0] --Prende in input due argomenti (un natrale e una lista) e ritorna una sottolista
	--potenzialmente finita o infinita che soddisfi la condizione
nonmultiple p numLst = [n | n <- numlst, n 'mod' p != 0] 
take 20 (multiple 3 natLst) -- ritorna la lista dei primi 20 numeri naturali divisibili per 3
