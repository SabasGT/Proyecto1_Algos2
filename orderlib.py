import numpy as np
from statistics import median
from math import log
from math import floor

def insertionSort(A:list) -> "list":
	# Insertionsort tan solo recibe el arreglo a ser ordenado
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
	# Merge se encarga de recibir 3 listas, 2 listas L y R las cuales combina en la lista A.
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
	# Mergesort tan solo recibe el arreglo a ser ordenado
	# assert(len(A)>0)                # Precondicion
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
	# Quicksort tan solo recibe el arreglo a ser ordenado
	# assert(len(A)>0)                # Precondicion
	# assert(A == sorted(A_original)) # Postcondicion
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


def insertionSortIndex(A:list, p:int, r:int):
	# InsertionsortIndez recibe la lista A a ser ordenada y los enteros mayores o iguales que 0 p y r.
	# Para una correcta inicializacion, p debe ser 0 y r debe ser la longitud de A (len(A)).
	# assert(len(A)>0 and p >= 0 and r >= 0)  # Precondicion
	# assert(A == sorted(A_original))         # Postcondicion
	for j in range(p,r):
		key = A[j]
		i = j-1
		while i>=0 and A[i]>key:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key


def partition(A:list, p:int, r:int) -> int:
	# Partition recibe la lista a ordenar A y los enteros mayores o iguales que 0 p y r.
	x = A[r]
	i = p-1
	for j in range(p,r):
		if A[j]<=x:
			i+=1
			A[i],A[j]=A[j],A[i]
	A[i+1],A[r]=A[r],A[i+1]
	return i+1


def quickSort(A:list, p:int, r:int) -> "void":
	# Quicksort recibe la lista A a ordenar y los enteros p y r mayores o iguales que 0.
	# Para una correcta inicializacion p debe ser 0 y r la longitud de A (len(A)).
	# assert(len(A)>0 and p >= 0 and r >= 0)  # Precondicion
	# assert(A == sorted(A_original))         # Postcondicion
	if p + r + 1 <= 32:
		insertionSortIndex(A, p, r)
	elif p < r:
		q = partition(A,p,r)
		quickSort(A,p,q-1)
		quickSort(A,q,r)


def right(i:int) -> int:
	# Right solo se encarga de recibir un entero i y obtener un valor k = 2i + 1.
	# assert(i >= 0)
	# assert(k = 2*i + 1)
	return 2*i + 1


def left(i:int) -> int:
	# Left solo se encarga de recibir un entero i y obtener un valor k = 2i.
	# assert(i >= 0)
	# assert(k = 2*i)
	return 2*i


def max_heapify(A:list, i:int, n:int) -> "void":
	# Max_Heapify recibe la lista A y los enteros mayores o iguales que 0 i e n.
	if i == 0:
		l,r=1,2
	else:
		l,r = left(i),right(i)
	if l<n and A[l]>A[i]:
		mayor = l
	else:
		mayor = i
	if r<n and A[r]>A[mayor]:
		mayor = r
	if mayor != i:
		A[i],A[mayor]=A[mayor],A[i]
		max_heapify(A,mayor,n)


def build_max_heap(A:list, f:int, b:int) -> "void":
	# Build_Max_Heap recibe la lista A y los enteros f y b mayores o iguales que 0.
	for i in range(b//2, f - 1, -1):
		max_heapify(A, i, b)


def heapSort(A:list, f:int, b:int) -> "void":
	# Heapsort recibe la lista A a ser ordenada y los enteros mayores o iguales que 0 f y b.
	# Para una correcta inicializacion, f debe ser 0 y b debe ser la longitud de A menos 1 (len(A) - 1).
	# assert(len(A)>0 and f >= 0 and b >= 0)  # Precondicion
	# assert(A == sorted(A_original))         # Postcondicion
	build_max_heap(A, f, b)
	for i in range(b, f,-1):
		A[0], A[i] = A[i], A[0]
		max_heapify(A,0, i)


def partitionLoop(A:list, p:int, r:int, x:int) -> "int":
	# Partition_Loop recibe la lista A y los enteros mayores o iguales que 0 p, r y x.
	i = p
	j = r-1
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
	# QuicksortLoop recibe la lista A a ser ordenada y los enteros mayores o iguales que 0 f y b.
	while b - f> 32:
		p = partitionLoop(A, f, b, median([A[f], A[f + ((b - f + 1)//2)], A[b]]))
		if (p - f) >= (b - p):
			quicksortLoop(A, p, b)
			b = p
		else:
			quicksortLoop(A, f, p)
			f = p


def quicksortMedian(A:list, f:int, b:int) -> "void":
	# QuicksortMedian recibe la lista A a ser ordenada y los enteros mayores o iguales que 0 f y b.
	# Para una correcta inicializacion, f debe ser 0 y b debe ser la longitud de A menos 1 (len(A) - 1).
	# assert(len(A)>0 and f >= 0 and b >= 0)  # Precondicion
	# assert(A == sorted(A_original))         # Postcondicion
	quicksortLoop(A, f, b)
	insertionSortIndex(A, f, b)


def introsortLoop(A:list, f:int, b:int, depthLim:int) -> "void":
	# QuicksortLoop recibe la lista A a ser ordenada y los enteros mayores o iguales que 0 f, b y depthLim.
	while (b - f) > 32:
		if depthLim == 0:
			heapSort(A, f, b)
			return
		depthLim = depthLim - 1
		p = partitionLoop(A, f, b, median([A[f], A[f + ((b - f + 1)//2)], A[b]]))
		introsortLoop(A, p, b, depthLim)
		b = p


def introSort(A:list, f:int, b:int) -> "void":
	# Introsort recibe la lista A a ser ordenada y los enteros mayores o iguales que 0 f y b.
	# Para una correcta inicializacion, f debe ser 0 y b debe ser la longitud de A menos 1 (len(A) - 1).
	# assert(len(A)>0 and f >= 0 and b >= 0)  # Precondicion
	# assert(A == sorted(A_original))         # Postcondicion
	introsortLoop(A, f, b, 2 * floor(log(b - f + 1, 2)))
	insertionSortIndex(A, f, b)

def threewaypart(A:list,l:int,r:int):
	i,j = l,r-1
	p,q = l-1,r
	v = A[r]
	while True:
		while A[i]<v:
			i+=1
		while v<A[j]:
			j-=1
			if j==l:
				break
		if i>=j:
			break
		A[i],A[j]=A[j],A[i]
		if A[i]==v:
			p+=1
			A[p],A[i]=A[i],A[p]
		if A[j]==v:
			q-=1
			A[j],A[q]=A[q],A[j]
	A[i],A[r]=A[r],A[i]
	j = i-1
	i+=1
	for k in range(l,p):
		A[k],A[j]=A[j],A[k]
		j -=1
	for k in range(r-1,q,-1):
		A[i],A[k]=A[k],A[i]
		i+=1
	return i,j



def quicksortThreeWay(A:list, l:int, r:int):
	# QuicksortThreeWay recibe la lista A a ordenar y los enteros l y r mayores o iguales que 0.
	# Para una correcta inicializacion l debe ser 0 y r la longitud de A menos 1 (len(A) - 1).
	# assert(len(A)>0 and p >= 0 and r >= 0)  # Precondicion
	# assert(A == sorted(A_original))         # Postcondicion
	
	if len(A)<=32:
		insertionSortIndex(A, l, r)
	elif r>l:
		i,j = threewaypart(A,l,r)
		quicksortThreeWay(A, l, j)
		quicksortThreeWay(A, i, r)


def quicksortDual(A:list, left:int, right:int) -> "void":
	# QuicksortDual recibe la lista A a ordenar y los enteros left y right mayores o iguales que 0.
	# Para una correcta inicializacion left debe ser 0 y right la longitud de A menos 1 (len(A) - 1).
	# assert(len(A)>0 and p >= 0 and r >= 0)  # Precondicion
	# assert(A == sorted(A_original))         # Postcondicion
	if (right - left + 1) <= 32:
		insertionSortIndex(A, left, right + 1)
	else:
		if A[left] > A[right]:
			p = A[right]
			q = A[left]
		else:
			p = A[left]
			q = A[right]
		
		l = left + 1
		g, k = right - 1, l
		while k <= g:
			if A[k] < p:
				A[k], A[l] = A[l], A[k]
				l += 1
			else:
				if A[k] >= q:
					while A[g] > q and k < g:
						g -= 1
					if A[g] >= p:
						A[k], A[g] = A[g], A[k]
					else:
						A[k], A[g] = A[g], A[k]
						A[k], A[l] = A[l], A[k]
						l += 1
					g -= 1
			k += 1
		l -= 1
		g += 1
		A[left] = A[l]
		A[l] = p
		A[right] = A[g]
		A[g] = q
		quicksortDual(A, left, l - 1)
		quicksortDual(A, l + 1, g - 1)
		quicksortDual(A, g + 1, right)





# if l + r + 1 >= 32:
# 		if r <= 1:
# 			return

# 		i = l - 1
# 		j = r
# 		p = l - 1
# 		q = r
# 		v = A[r]
		
# 		while True:
# 			foundi = True
# 			foundj = True
# 			i += 1

# 			while A[i] <= v and foundi:
# 				if A[i] <= v:
# 					foundi = False
# 				i += 1

# 			while v <= A[j] and foundj:
# 				if j == 0:
# 					break
# 				if v <= A[j]:
# 					foundj = False
# 				j -= 1

# 			if i >= j:
# 				break

# 			A[i], A[j] = A[j], A[i]

# 			if A[i] == v:
# 				p += 1
# 				A[p], A[i] = A[i], A[p]

# 			if A[j] == v:
# 				q = q - 1
# 				A[j], A[q] = A[q], A[j]
		
# 		A[i], A[r] = A[r], A[i]
# 		j = i - 1
# 		k = l
# 		while k < p:
# 			A[k], A[j] = A[j], A[k] 
# 			k += 1
# 			j -= 1
		
# 		i = i + 1
# 		k = r - 1
# 		while k > q:
# 			A[i], A[k] = A[k], A[i]
# 			k -= 1
# 			i += 1