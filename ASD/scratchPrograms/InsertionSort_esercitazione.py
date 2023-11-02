def InsertionSortRecursive(A, n):
    if n > 1:
        InsertionSortRecursive(A, n - 1)
        Insert(A, n - 1)

def InsertionSortIterative(A, n - 1):
    for i in range(n):
        Insert(A, i) 

def Insert(A, i):
    x = A[i]
    j = i - 1
    while(j >= 0 && A[j] > x):
        A[j + 1] = A[j]
        j--
    A[j + 1] = x
