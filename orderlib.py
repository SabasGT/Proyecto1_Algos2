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



def merge_Insertion(L:list, R:list, A:list) -> "void":
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


def mergeSort_Insertion(A:list) -> "void":
	# assert(len(A)>0) # Precondicion
	# assert(A == sorted(A_original)) # Postcondicion
	if len(A) <= 32:
		insertionSort(A)
	else:
		U = A[0:(len(A)//2)]
		V = A[(len(A)//2):len(A)]
		mergeSort_Insertion(U)
		mergeSort_Insertion(V)
		merge_Insertion(U, V, A)