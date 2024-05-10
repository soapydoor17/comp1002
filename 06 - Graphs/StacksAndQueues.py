# Using code from Prac 4 to 

# Prac 4 Activity 2 - Using LinkedLists in Stacks and Queue
# Adapting Code from StacksAndQueues.py from Prac 3

# Activity 1 and 2 of Prac 3
# Implementation of Stacks and Queues using LINKED LISTS as the data structure
# Contains code for DSAStack, DSAQueue, ShufflingQueue and CircularQueue

import LinkedLists as ll

# CLASS INITIALISATION
class DSAStack():
    def __init__(self):
        ''' Intialisation
         
        self.stack - object linked list with LIFO functionality
        self.count - the number of elements currently in the stack
        '''
        self.stack = ll.DSALinkedList()
        self.count = 0
    
    def getCount(self):
        ''' ACCESSOR: Returns number (int) of elements in the stack
        '''
        return self.count
    
    def isEmpty(self):
        ''' ACCESSOR: Returns boolean that is true if there are currently no elements in the stack
        '''
        empty = self.stack.isEmpty()
        return empty

    def top(self):
        ''' ACCESSOR: Looks at top-most item but leaves it in the stack
        '''
        if self.isEmpty():
            raise ll.EmptyException('Stack is empty')
        else:
            topVal = self.stack.peekFirst()
            return topVal
        
    def push(self, inValue):
        ''' MUTATOR: Adds a new element to the top of the stack
        
        inValue - element to be added to stack
        '''
        self.stack.insertFirst(inValue)
        self.count += 1

    def pop(self):
        ''' MUTATOR: takes off top most element of stack and returns it
        '''
        topVal = self.stack.removeFirst()
        self.count -= 1
        return topVal


class DSAQueue():
    def __init__(self):
        ''' Intialisation

        self.queue - object LinkedList with FIFO functionality
        self.count - the number of elements currently in the queue
        '''
        self.queue = ll.DSALinkedList()
        self.count = 0

    def getCount(self):
        ''' ACCESSOR: Returns number (int) of elements in the queue
        '''
        return self.count
    
    def isEmpty(self):
        ''' ACCESSOR: Returns boolean that is true if there are currently no elements in the queue
        '''
        empty = self.queue.isEmpty()
        return empty
    
    def peek(self):
        ''' ACCESSOR: Looks at first item but leaves it in the stack
        '''
        if self.isEmpty():
            raise ll.EmptyException('Queue is empty')
        else:
            frontVal = self.queue.peekFirst()
            return frontVal
        
    def enqueue(self, inValue):
        ''' MUTATOR: adds to the end of the queue
        
        inValue - element to be added to the queue
        '''
        self.queue.insertLast(inValue)
        self.count += 1

    def dequeue(self):
        ''' MUTATOR: Returns value from front of queue and removes it, shuffling down all other items
        '''
        frontVal = self.queue.removeFirst()
        self.count -= 1
        return frontVal
