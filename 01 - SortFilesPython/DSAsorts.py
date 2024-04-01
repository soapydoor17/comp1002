#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

def bubbleSort(A):
    for p in range(len(A)-1):
        # Passing through and sorting
        swapped = False
        for i in range(len(A)-p-1):
            if (A[i] > A[i+1]):
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
                swapped = True
        print(A)
        
        # Checking if complete
        if not swapped:
            print("FINISHED", p)
            print("Final Array:", A)
            return
    print("Final Array:", A)

def insertionSort(A):
    for n in range(1, len(A)):
        i = n
        while (i > 0) and (A[i-1] > A[i]):
            temp = A[i]
            A[i] = A[i-1]
            A[i-1] = temp
            i -= 1
        print(A)
    print("Final Array:", A)

def selectionSort(A):
    for n in range(len(A)-1):
        minIdx = n
        for j in range(n+1, len(A)):
            if (A[j] < A[minIdx]):
                minIdx = j  
        temp = A[minIdx]
        A[minIdx] = A[n]
        A[n] = temp
        print(A)
    print("Final Array:", A)

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...


