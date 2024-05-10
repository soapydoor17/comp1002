# Taken from Prac 4 code
# Updated to have a __str__ function
# LinkedLists.py contains class information for linked lists

# EXCEPTION INITIALISATION
class EmptyException(Exception):
    ''' Error attempting to access an element from an empty container
    This is taken from Prac 3 StacksAndQueues.py
    '''
    pass

class DSAListNode():
    def __init__(self, inValue):
        self._value = inValue
        self._next = None
        self._prev = None

    def getValue(self):
        return self._value
    
    def setValue(self, inValue):
        self._value = inValue

    def getNext(self):
        return self._next
    
    def setNext(self, newNext):
        self._next = newNext

    def getPrev(self):
        return self._prev
    
    def setPrev(self, newPrev):
        self._prev = newPrev

class DSALinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        empty = (self.head == None)
        return empty
    
    def insertFirst(self, newValue):
        newNd = DSAListNode(newValue)
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
        else:
            self.head.setPrev(newNd)
            newNd.setNext(self.head)
            self.head = newNd

    def insertLast(self, newValue):
        newNd = DSAListNode(newValue)
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
        else:
            self.tail.setNext(newNd)
            newNd.setPrev(self.tail)
            self.tail = newNd

    def removeFirst(self):
        if self.isEmpty():
            raise EmptyException('Linked List is empty')
        elif self.head.getNext() == None:
            nodeValue = self.head.getValue()
            self.head = None
            self.tail = None
        else:
            nodeValue = self.head.getValue()
            self.head = self.head.getNext()
            self.head.setPrev(None)
        return nodeValue
    
    def removeLast(self):
        if self.isEmpty():
            raise EmptyException('Linked List is empty')
        elif self.head.getNext() == None:
            nodeValue = self.head.getValue()
            self.head = None
            self.tail = None
        else:
            nodeValue = self.tail.getValue()
            self.tail = self.tail.getPrev()
            self.tail.setNext(None)
        return nodeValue
    
    def peekFirst(self):
        if self.isEmpty():
            raise EmptyException('Linked List is empty')
        else:
            nodeValue = self.head.getValue()
        return nodeValue
    
    def peekLast(self):
        if self.isEmpty():
            raise EmptyException('Linked List is empty')
        else:
            nodeValue = self.tail.getValue()
        return nodeValue
    
    def __str__(self):
        curr = self.head
        listString = ''
        while curr != None:
            currString = str(curr.getValue()) + ' '
            listString = listString + currString
            curr = curr.getNext()
        return listString

