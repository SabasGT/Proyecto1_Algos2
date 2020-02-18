import numpy as np

def insertionSort(A:list) -> "list":
	# assert(len(A)>0)                # Precondicion
	# assert(A == sorted(A_original)) # Postcondicion
	for i in range(1, len(A)):
		key = A[i]
		j = i - 1
		while j >= 0 and A[j] > key:
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = key
	return A


def merge(L:list, R:list, A:list) -> "void":
	infinito = float("inf")
	i, j = 0,0

	L = np.concatenate((L, [infinito]))
	R = np.concatenate((R, [infinito]))

	for k in range(0, (len(L) + len(R)) - 2):
		if L[i] < R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1


def mergeSort(A:list) -> "void":
	# assert(len(A)>0) # Precondicion
	# assert(A == sorted(A_original)) # Postcondicion
	if len(A) <= 32:
		insertionSort(A)
	else:
		U = A[0:(len(A)//2)]
		V = A[(len(A)//2):len(A)]
		mergeSort(U)
		mergeSort(V)
		merge(U, V, A)


def quicksortIter(A:list) -> "void":
	n, m = 0, 1
	tam = len(A)

	while m < tam:
		n, m = n + 1, m * 2
	k, p, q = 0, 0, tam

	x = [0] * n
	y = [0] * n

	while (k != 0) or (q - p >= 2):
		if (q - p <= 1):
			k = k - 1
			p = x[k]
			q = y[k]
		elif (q - p >= 2):
			z = A[(p + q) // 2]
			r, w, b = p, p , q
			while w != b:
				if A[w] < z:
					A[r], A[w] = A[w], A[r]
					r, w = r + 1, w + 1
				elif A[w] == z:
					w = w + 1
				elif A[w] > z:
					b = b - 1
					A[b], A[w] = A[w], A[b]
			
			if r - p <= q - w:
				x[k] = w
				y[k] = q
				q = r
			elif q - w <= r - p:
				x[k] = p
				y[k] = r
				p = w
			k += 1


def insertionSortIndex(A:list, p:int, r:int) -> "void":
	for j in range(p, r):
		key = A[j]
		i = j - 1
		while i >= 0 and A[i] > key:
			A[i + 1] = A[i]
			i -= 1
		A[i + 1] = key


def partition(A:list, p:int, r:int) -> int:
	x = A[r]
	i = p - 1
	for j in range(p,r):
		if A[j] <= x:
			i = i + 1
			A[i], A[j] = A[j], A[i]
	A[i + 1], A[r] = A[r], A[i + 1]
	return (i + 1)


def quickSort(A:list, p:int, r:int) -> "void":
	# Correcta inicializacion con p = 0 y r = len(A) - 1
	if p + r + 1 <= 100:
		insertionSortIndex(A, p, r)
	else:
		if p < r:
			q = partition(A, p, r)
			quickSort(A,p,q-1)
			quickSort(A,q,r)