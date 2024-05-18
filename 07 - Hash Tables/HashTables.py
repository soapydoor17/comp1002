# Prac 07 - Hash Tables Classes

import numpy as np
import csv

class HashException(Exception):
    pass

class DSAHashEntry():
    def __init__(self, inKey='', inValue=None):
        self._key = inKey
        self._value = inValue
        self._state = 0

        if inValue != None:
            self._state = 1

    def getKey(self):
        return self._key
    
    def getValue(self):
        return self._value
    
    def getState(self):
        return self._state
    
    def setState(self, newState):
        if newState != 1 and newState != 0 and newState != -1:
            raise ValueError("State must be 0, 1, or -1")
        self._state = newState

class DSAHashTable():
    def __init__(self, tableSize):
        actualSize = self._nextPrime(tableSize)
        self.hashArray = np.zeros(actualSize, dtype=object)
        for i in range(actualSize):
            self.hashArray[i] = DSAHashEntry()
        self.count = 0

    def _nextPrime(self, inNum):
        if inNum % 2 == 0:
            primeVal = inNum - 1
        else:
            primeVal = inNum
        
        isPrime = False
        while not isPrime:
            primeVal += 2
            firstPass = True
            ii = 3
            isPrime = True
            rootVal = np.sqrt(primeVal)
            while firstPass or (ii <= rootVal and isPrime):
                firstPass = False
                if primeVal % ii == 0:
                    isPrime = False
                else:
                    ii += 2

        return int(primeVal)

    def _hash(self, inKey):
        hashIdx = 0
        for i in range (len(inKey)):
            hashIdx = (31 * hashIdx) + ord(inKey[i])
        return hashIdx % self.hashArray.size
    
    def _stepHash(self, inKey):
        hashStep = 5 - (ord(inKey[0]) % 5)
        return hashStep
    
    def put(self, inKey, inValue):
        newEntry = DSAHashEntry(inKey, inValue)
        hashIdx = self._hash(inKey)
        success = False
        origIdx = hashIdx
        giveUp = False
        probeStep = self._stepHash(inKey)

        while not success and not giveUp:
            arrayElement = self.hashArray[hashIdx]
            if arrayElement.getState() != 1:
                self.hashArray[hashIdx] = newEntry
                success = True
            else:
                hashIdx = (hashIdx + probeStep) % self.hashArray.size
                if hashIdx == origIdx:
                    giveUp = True

        if giveUp:
            raise HashException("Key", inKey, "was not able to be put into the hash table")
        
        self.count += 1

        if self.getLoadFactor() > 0.7:
            self._resize(2 * self.hashArray.size)

    def get(self, inKey):
        hashIdx = self._hash(inKey)
        origIdx = hashIdx
        found = False
        giveUp = False
        probeStep = self._stepHash(inKey)

        while not found and not giveUp:
            if self.hashArray[hashIdx].state == 0:
                giveUp = True
            elif self.hashArray[hashIdx].key == inKey:
                found = True
            else:
                hashIdx = (hashIdx + probeStep) % self.hashArray.size
                if hashIdx == origIdx:
                    giveUp = True

        if not found:
            raise HashException("Key", inKey, "was not found in the hash table. Value could not be retrieved")
        
        retValue = self.hashArray[hashIdx].value
        return retValue
    
    def remove(self, inKey):
        hashIdx = self._hash(inKey)
        origIdx = hashIdx
        found = False
        giveUp = False
        probeStep = self._stepHash(inKey)

        while not found and not giveUp:
            if self.hashArray[hashIdx].getState() == 0:
                giveUp = True
            elif self.hashArray[hashIdx].getKey() == inKey:
                found = True
            else:
                hashIdx = (hashIdx + probeStep) % self.hashArray.size
                if hashIdx == origIdx:
                    giveUp = True

        if not found:
            raise HashException("Key", inKey, "was not found in the hash table. Entry could not be deleted")
        
        delEntry = DSAHashEntry()
        delEntry.setState(-1)
        self.hashArray[hashIdx] = delEntry
        self.count -= 1

        if self.getLoadFactor() < 0.3:
            self._resize(self.hashArray.size // 2)

        print('Removed', inKey)

    def hasKey(self, inKey):
        hashIdx = self._hash(inKey)
        origIdx = hashIdx
        found = False
        giveUp = False
        probeStep = self._stepHash(inKey)

        while not found and not giveUp:
            if self.hashArray[hashIdx].getState() == 0:
                giveUp = True
            elif self.hashArray[hashIdx].getKey() == inKey:
                found = True
            else:
                hashIdx = (hashIdx + probeStep) % self.hashArray.size
                if hashIdx == origIdx:
                    giveUp = True

        return found
    
    def getLoadFactor(self):
        return self.count / self.hashArray.size
    
    def _resize(self, size):
        count = 0
        entries = np.zeros(self.count, dtype=object)
        for element in self.hashArray:
            if element.getState() == 1:
                entries[count] = element
                count += 1

        if count != self.count:
            raise HashException("Error when resizing: Count of entries does not equal to self.count")
        
        size = self._nextPrime(size)
        self.hashArray = np.zeros(size, dtype=object)
        self.count = 0

        for i in range(size):
            self.hashArray[i] = DSAHashEntry()

        for i in range(count):
            key = entries[i].getKey()
            value = entries[i].getValue()
            self.put(key, value)

        print('Resizing to', size)

    def export(self, filename):
        print('Exporting', filename + '.csv')
        f = open(filename + '.csv', 'w+')
        f.close()
        with open(filename + '.csv', 'w', newline='') as file:
            exporter = csv.writer(file)
            for instance in self.hashArray:
                if instance.getState() == 1:
                    exporter.writerow([instance.getKey(), instance.getValue()])
        
        print('Export successful')


def readFile(inFilename):
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

def main():
    # Create a hash table
    hashTable = DSAHashTable(3)

    # Add entries to the hash table
    for i in range(1, 20):
        hashTable.put(f"key{i}", f"value{i}")

    print("Load Factor:", hashTable.getLoadFactor())

    # Print the size of the hash table after adding entries
    print(f"Size of hash table after adding entries: {hashTable.hashArray.size}")

    # Remove some entries from the hash table
    for i in range(1, 10):
        hashTable.remove(f"key{i}")

    print("Load Factor:", hashTable.getLoadFactor())

    # Print the size of the hash table after removing entries
    print(f"Size of hash table after removing entries: {hashTable.hashArray.size}")

    hashTable1 = DSAHashTable(10)

    # Read in the RandomNames7000.csv file
    contents = readFile('RandomNames7000.csv')
    for row in contents:
        key = row[0]
        value = row[1]
        # Check if the key already exists in the hash table
        if not hashTable1.hasKey(key):
            # If not, insert the key-value pair into the hash table
            hashTable1.put(key, value)

    # Export the hash table to a .csv file using the export method
    hashTable1.export('HashTableOutput')
    print("Hash Array Size", hashTable1.hashArray.size)
    print("Number of Entries", hashTable1.count)
    print("Load Factor:", hashTable1.getLoadFactor())

if __name__ == "__main__":
    main()
