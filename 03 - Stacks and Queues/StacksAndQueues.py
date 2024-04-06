# Activity 1 and 2 of Prac 3
# Implementation of Stacks and Queues using arrays as the data structure
# Contains code for DSAStack, DSAQueue, ShufflingQueue and CircularQueue
# Also contains custom exceptions for when ADTs are full or empty

import numpy

# EXCEPTION INITIALISATION
class EmptyException(Exception):
    ''' Error attempting to access an element from an empty container
    '''
    pass

class FullException(Exception):
    ''' Error attempting to access an element from a full container
    '''
    pass

# CLASS INITIALISATION
class DSAStack():
    def __init__(self, maxCapacity=100):
        ''' Intialisation

        maxCapacity - initialises number of elements in stack (default 100)
        
        self.stack - object array with LIFO functionality
        self.capacity - how many elements the stack is able to hold
        self.count - the number of elements currently in the stack
        '''
        self.stack = numpy.empty(maxCapacity, dtype=object)
        self.capacity = maxCapacity
        self.count = 0
    
    def getCount(self):
        ''' ACCESSOR: Returns number (int) of elements in the stack
        '''
        return self.count
    
    def isEmpty(self):
        ''' ACCESSOR: Returns boolean that is true if there are currently no elements in the stack
        '''
        empty = (self.count == 0)
        return empty
    
    def isFull(self):
        ''' ACCESSOR: Returns boolean that is true if the stack is at capacity
        '''
        full = (self.count == self.capacity)
        return full

    def top(self):
        ''' ACCESSOR: Looks at top-most item but leaves it in the stack
        '''
        if self.isEmpty():
            raise EmptyException('Stack is empty')
        else:
            topVal = self.stack[self.count-1]
            return topVal
        
    def push(self, inValue):
        ''' MUTATOR: Adds a new element to the top of the stack
        
        inValue - element to be added to stack
        '''
        if self.isFull():
            raise FullException('Stack is full')
        else:
            self.stack[self.count] = inValue
            self.count += 1

    def pop(self):
        ''' MUTATOR: takes off top most element of stack and returns it
        '''
        topVal = self.top()
        self.count -= 1
        return topVal


class DSAQueue():
    def __init__(self, maxCapacity=100):
        ''' Intialisation

        maxCapacity - initialises number of elements in queue (default 100)
        
        self.queue - object array with FIFO functionality
        self.capacity - how many elements the queue is able to hold
        self.count - the number of elements currently in the queue
        '''
        self.queue = numpy.empty(maxCapacity, dtype=object)
        self.capacity = maxCapacity
        self.count = 0

    def getCount(self):
        ''' ACCESSOR: Returns number (int) of elements in the queue
        '''
        return self.count
    
    def isEmpty(self):
        ''' ACCESSOR: Returns boolean that is true if there are currently no elements in the queue
        '''
        empty = (self.count == 0)
        return empty
    
    def isFull(self):
        ''' ACCESSOR: Returns boolean that is true if the queue is at capacity
        '''
        full = (self.count == self.capacity)
        return full
    
    def peek(self):
        ''' ACCESSOR: Looks at last item but leaves it in the stack
        '''
        if self.isEmpty():
            raise EmptyException('Queue is empty')
        else:
            frontVal = self.queue[0]
            return frontVal
        
    def enqueue(self, inValue):
        ''' MUTATOR: adds to the end of the queue
        
        inValue - element to be added to the queue
        '''
        if self.isFull():
            raise FullException('Queue is full')
        else:
            self.queue[self.count] = inValue
            self.count += 1

    def dequeue(self):
        ''' MUTATOR: Returns value from front of queue and removes it, shuffling down all other items
        '''
        frontVal = self.peek()
        for i in range(1, len(self.queue)):
            self.queue[i-1] = self.queue[i]
        self.count -= 1
        return frontVal

class ShufflingQueue(DSAQueue):
    pass

class CircularQueue(DSAQueue):
    def __init__(self, maxCapacity=100):
        ''' INITIALISATION - inherits from DSAQueue

        self.front - index of where the first element is
        '''
        super().__init__(maxCapacity)
        self.front = 0

    def peek(self):
        ''' ACCESSOR: Looks at first item but leaves it in the stack
        '''
        if self.isEmpty():
            raise EmptyException('Queue is empty')
        else:
            frontVal = self.queue[self.front]
            return frontVal
        
    def enqueue(self, inValue):
        ''' MUTATOR: adds to the end of the queue
        
        inValue - element to be added to the queue
        '''
        if self.isFull():
            raise FullException('Queue is full')
        else:
            index = (self.front + self.count) % len(self.queue)  # modulus accounts for overflow
            self.queue[index] = inValue
            self.count += 1

    def dequeue(self):
        ''' MUTATOR: Returns value from front of queue and removes it, changing the location of the front of the queue
        '''
        frontVal = self.peek()
        self.count -= 1
        
        # Return self.front to zero if it is going to overflow
        if self.front == self.capacity - 1:
            self.front = 0
        else:
            self.front += 1

        return frontVal
