def HeapSort(A, n):
    BuildHeap(A,n)
    for i = n-1 in range(0):
        Swap(A, 0, i)
        Heapify(A, i, 0)

def BuildHeap(A, n):
    for i = (n/2) - 1 in range(0):
        Heapify(A, n, i)

def Heapify(A, n, i):
    max = i
    l = L(i) # indice del figlio sx dove L(i) = 2i + 1 se l'indice di partenza è 1
    r = R(i) # indice del figlio dx dove R(i) = 2i + 2 se l'indice di partenza è 1
    if l < n and A[max] < A[l]:
        max = l # Aggiorno il valore di max con l'indice destro
    if r < n and A[max] < A[l]:
        max = r # Aggiorno il valore di max con l'indice sinistro
    if max != i:
        Swap(A, max, i)
        Heapify(A, n, max)
