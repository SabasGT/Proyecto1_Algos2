import numpy as np
from statistics import median
from math import log
from math import floor

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
	if p + r + 1 <= 32:
		insertionSortIndex(A, p, r)
	else:
		if p < r:
			q = partition(A, p, r)
			quickSort(A,p,q-1)
			quickSort(A,q,r)


def right(i:int) -> int:
	k = 2*i + 1
	return k


def left(i:int) -> int:
	k = 2*i
	return k


def max_heapify(A:list, i:int, n:int) -> "void":
	l = left(i)
	r = right(i)
	if l < n and A[l] > A[i]:
		largest = l
	else:
		largest = i

	if r < n and A[r]> A[largest]:
		largest = r

	if largest != i:
		A[i], A[largest] = A[largest], A[i]
		max_heapify(A, largest, n)


def build_max_heap(A:list, f:int, b:int) -> "void":

	for i in range(b//2, f - 1, -1):
		max_heapify(A, i, b)


def heapSort(A:list, f:int, b:int) -> "void":
	build_max_heap(A, f, b)

	for i in range(b, f,-1):
		A[0], A[i] = A[i], A[0]
		max_heapify(A,0, i)


def partitionLoop(A:list, p:int, r:int, x:int) -> "int":
	i = p - 1
	j = r
	while True:
		while A[j] > x:
			j = j - 1

		while A[i] < x:
			i = i + 1

		if i < j:
			A[i], A[j] = A[j], A[i]
		else:
			return j


def quicksortLoop(A:list, f:int, b:int) -> "void":
	while b - f  + 1> 32:
		p = partitionLoop(A, f, b, median([A[f], A[f + ((b - f + 1)//2)], A[b]]))
		if (p - f) >= (b - p):
			quicksortLoop(A, p, b)
			b = p
		else:
			quicksortLoop(A, f, p)
			f = p


def quicksortMedian(A:list, f:int, b:int) -> "void":
	quicksortLoop(A, f, b)
	insertionSortIndex(A, f, b + 1)


def introsortLoop(A:list, f:int, b:int, depthLim:int) -> "void":
	while (b + 1 - f) > 32:
		if depthLim == 0:
			heapSort(A, f, b)
			return
		
		depthLim = depthLim - 1
		p = partitionLoop(A, f, b, median([A[f], A[f + ((b - f + 1)//2)], A[b]]))
		introsortLoop(A, p, b, depthLim)
		b = p


def introSort(A:list, f:int, b:int) -> "void":
	introsortLoop(A, f, b, 2 * floor(log(b - f + 1, 2)))
	insertionSortIndex(A, f, b + 1)


def quicksortThreeWay(A:list, l:int, r:int) -> "void":
	if l + r + 1 >= 32:
		if r <= 1:
			return

		i = l - 1
		j = r
		p = l - 1
		q = r
		v = A[r]
		
		while True:
			foundi = True
			foundj = True
			i += 1

			while A[i] <= v and foundi:
				if A[i] <= v:
					foundi = False
				i += 1

			while v <= A[j] and foundj:
				if j == 0:
					break
				if v <= A[j]:
					foundj = False
				j -= 1

			if i >= j:
				break

			A[i], A[j] = A[j], A[i]

			if A[i] == v:
				p += 1
				A[p], A[i] = A[i], A[p]

			if A[j] == v:
				q = q - 1
				A[j], A[q] = A[q], A[j]
		
		A[i], A[r] = A[r], A[i]
		j = i - 1
		k = l
		while k < p:
			A[k], A[j] = A[j], A[k] 
			k += 1
			j -= 1
		
		i = i + 1
		k = r - 1
		while k > q:
			A[i], A[k] = A[k], A[i]
			k -= 1
			i += 1

		quicksortThreeWay(A, l, j)
		quicksortThreeWay(A, i, r)
	else:
		insertionSortIndex(A, l, r)





