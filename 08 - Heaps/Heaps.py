# Prac 8 - Heaps 

import numpy as np
import csv

class HeapException(Exception):
    # Used when there is an issue specific to the heap
    pass

## CLASSES FOR HEAPS$
class DSAHeapEntry():
    def __init__(self, inPriority, inValue):
        self._priority = inPriority
        self._value = inValue

    def getPriority(self):
        return self._priority
    
    def setPriority(self, inPriority):
        self._priority = inPriority

    def getValue(self):
        return self._value
    
    def setValue(self, inValue):
        self._value = inValue

class DSAHeap():
    def __init__(self, size):
        self.heap = np.zeros(size, dtype=object)
        self._count = 0

    def getCount(self):
        return self._count

    def add(self, inPriority, inValue):
        if not self.heap.size == self._count:
            newEntry = DSAHeapEntry(inPriority, inValue)
            currIdx = self._count
            self.heap[currIdx] = newEntry
            self._trickleUp(currIdx)
            self._count += 1
        else:
            raise HeapException("Heap is full. Entry could not be added")

    def remove(self):
        if self.heap.size != 0:
            root = self.heap[0]
            self.heap[0] = self.heap[self._count-1]
            self.heap[self._count-1] = 0
            self._count -= 1
            self._trickleDown(0, self._count)
            return root
        else:
            raise HeapException("Heap is empty. No items to be removed")
    
    def display(self):
        if self._count != 0:
            for i in range(self._count):
                entry = self.heap[i]
                print("Priority:", entry.getPriority(), "\tValue:", entry.getValue())
        else:
            print("Heap is currently empty. There is nothing to display")
        print()

    def _trickleUp(self, index):
        parentIdx = int((index - 1) / 2)
        if index > 0:
            if self.heap[index].getPriority() > self.heap[parentIdx].getPriority():
                temp = self.heap[parentIdx]
                self.heap[parentIdx] = self.heap[index]
                self.heap[index] = temp
                self._trickleUp(parentIdx)

    def _trickleDown(self, index, numItems):
        lChildIdx = int(index * 2 + 1)
        rChildIdx = lChildIdx + 1

        if lChildIdx < numItems:
            largeIdx = lChildIdx
            if rChildIdx < numItems:
                if self.heap[lChildIdx].getPriority() < self.heap[rChildIdx].getPriority():
                    largeIdx = rChildIdx
            if self.heap[largeIdx].getPriority() > self.heap[index].getPriority():
                self._swap(largeIdx, index)
                self._trickleDown(largeIdx, numItems)

    def _swap(self, idx1, idx2):
        temp = self.heap[idx1]
        self.heap[idx1] = self.heap[idx2]
        self.heap[idx2] = temp

    def _heapify(self):
        # Converts array of DSAHeapEntry into a max heap
        maxHeap = self
        for i in range(int(self._count/2)-1, -1, -1):
            maxHeap._trickleDown(i, self._count)
        return maxHeap

    def heapSort(self):
        maxHeap = self._heapify()
        for i in range(self._count-1, 0, -1):
            maxHeap._swap(0, i)
            maxHeap._trickleDown(0, i)
        return maxHeap.heap

    def export(self, filename):
        # Taken from Prac 7 - adapted for heaps
        print('Exporting', filename + '.csv')
        f = open(filename + '.csv', 'w+')
        f.close()
        with open(filename + '.csv', 'w', newline='') as file:
            exporter = csv.writer(file)
            for instance in self.heap:
                exporter.writerow([instance.getPriority(), instance.getValue()])
        
        print('Export successful')

def readFile(inFilename):
    # Taken from Prac 7
    contents = None
    try:
        f = open(inFilename, 'r')
        contents = np.genfromtxt(inFilename, delimiter=',', dtype=str)
        print("Rows:", len(contents), "Columns:", len(contents[0]))
        for i in range(len(contents)):
            for j in range(len(contents[0])):
                pass
        print("Read successful")
    except:
        print("Error opening", inFilename)
    finally:
        f.close()
    return contents

## TEST HARNESS
def main():
    print('\nTesting DSAHeap and DSAEntry Class\n')

    heap = DSAHeap(10)
    print('Heap before items are added:')
    print('Count:', heap.getCount())
    heap.display()

    # Adding to Heap
    heap.add(2, "24")
    heap.add(7, "6")
    heap.add(26, "7")
    heap.add(25, "99")
    heap.add(19, "9")
    print("\nAfter Adding, Before Removal: ")
    print('Count:', heap.getCount()) 
    heap.display()

    heap.remove()
    print("\nAfter Removal: ")
    print('Count:', heap.getCount()) 
    heap.display()

    # Testing Sorting
    print("\nTesting HeapSort\n")
    print("Before Sorting:")
    heap.display()

    sortedArray = heap.heapSort()

    print("After Sorting:")
    for i in range(sortedArray.size):
        entry = sortedArray[i]
        if entry != 0:
            print("Priority:", entry.getPriority(), "\tValue:", entry.getValue())
    print()

    # Sorting RandomNames7000.csv
    print('\nSorting RandomNames7000.csv')

    namesHeap = DSAHeap(7000)

    namesArray = readFile('RandomNames7000.csv')
    for row in namesArray:
        priority = row[0]
        value = row[1]
        namesHeap.add(priority, value)

    sortedNames = namesHeap.heapSort()
    print('\nSucessfully Sorted RandomNames7000.csv\n')
    # Taken from Prac 7 - adapted for heaps
    print('Exporting HeapsOutput.csv')
    f = open('HeapsOutput.csv', 'w+')
    f.close()
    with open('HeapsOutput.csv', 'w', newline='') as file:
        exporter = csv.writer(file)
        for instance in sortedNames:
            if instance != 0:
                exporter.writerow([instance.getPriority(), instance.getValue()])
    
    print('Export successful')

if __name__ == '__main__':
    main()
