# Prac 6 - Activity 1 - Graph Implementation
# Undirected Graph

import LinkedLists as ll
import StacksAndQueues as sq

class DSAGraphVertex():
    def __init__(self, inLabel, inValue):
        self._label = inLabel
        self._value = inValue
        self._links = ll.DSALinkedList()
        self._visited = False

    def getLabel(self):
        return self._label
    
    def getValue(self):
        return self._value
    
    def getAdjacent(self):
        return self._links
    
    def setVisited(self):
        self._visited = True

    def clearVisited(self):
        self._visited = False

    def getVisited(self):
        return self._visited
    
    def addEdge(self, vertex):
        self._links.insertLast(vertex)

    def deleteEdge(self, label):
        edges = self.getAdjacent()
        currE = edges.head
        success = False
        if currE != None and currE.getNext() == None:
            self._links.head = None
            self._links.tail = None
            success = True
        else:
            while currE != None and not success:
                if currE.getValue().getLabel() == label:
                    prevE = currE.getPrev()
                    nextE = currE.getNext()
                    if prevE == None:
                        edges.head = nextE
                    else:
                        prevE.setNext(nextE)
                    if nextE == None:
                        edges.tail = prevE
                    else:
                        nextE.setPrev(prevE)
                    success = True
                currE = currE.getNext()

        if success == False:
            raise ValueError

    def __str__(self):
        return str(self.getLabel())
    
class DSAGraph():
    def __init__(self):
        self.vertices = ll.DSALinkedList()

    def addVertex(self, label, value):
        # Checking label isn't already in graph
        currV = self.vertices.head
        while currV != None:
            if currV.getValue().getLabel() == label:
                raise ValueError
            currV = currV.getNext()

        # Adding graph to tree
        newVertex = DSAGraphVertex(label, value)
        self.vertices.insertLast(newVertex)

    def hasVertex(self, label):
        currV = self.vertices.head
        success = False
        while currV != None and not success:
            if currV.getValue().getLabel() == label:
                success = True
            currV = currV.getNext()
        return success
    
    def getVertexCount(self):
        count = 0
        currV = self.vertices.head
        while currV != None:
            count += 1
            currV = currV.getNext()
        return count

    def getEdgeCount(self):
        count = 0
        currV = self.vertices.head
        while currV != None:
            edges = currV.getValue().getAdjacent()
            currE = edges.head
            while currE != None:
                count += 1
                currE = currE.getNext()
            currV = currV.getNext()
        count = count / 2
        return count
    
    def getVertex(self, label):
        vertex = None
        currV = self.vertices.head
        while currV != None and vertex == None:
            if currV.getValue().getLabel() == label:
                vertex = currV.getValue()
            currV = currV.getNext()
        if vertex == None:
            raise ValueError
        return vertex
    
    def getAdjacent(self, label):
        vertex = self.getVertex(label)
        vertexList = vertex.getAdjacent()
        return vertexList
    
    def isAdjacent(self, label1, label2):
        v1List = self.getAdjacent(label1)
        currV = v1List.head
        success = False
        while currV != None and not success:
            if currV.getValue().getLabel() == label2:
                success = True
            currV = currV.getNext()
        return success
    
    def addEdge(self, label1, label2):
        v1success = False
        while not v1success:
            try:
               vertex1 = self.getVertex(label1)
               v1success = True
            except ValueError:
                self.addVertex(label1, None)

        v2success = False
        while not v2success:
            try:
               vertex2 = self.getVertex(label2)
               v2success = True
            except ValueError:
                self.addVertex(label2, None)

        vertex1.addEdge(vertex2)
        vertex2.addEdge(vertex1)

    def deleteEdge(self, label1, label2):
        vertex1 = self.getVertex(label1)
        vertex2 = self.getVertex(label2)
        vertex1.deleteEdge(label2)
        vertex2.deleteEdge(label1)

    def deleteVertex(self, label):
        vertexList = self.vertices
        currV = vertexList.head
        success = False

        # Delete Vertex
        if currV.getNext() == None:
            self.vertices.head = None
            self.vertices.tail = None
            success = True
        else:
            while currV != None and not success:
                if currV.getValue().getLabel() == label:
                    prevV = currV.getPrev()
                    nextV = currV.getNext()
                    if prevV == None:
                        vertexList.head = nextV
                    else:
                        prevV.setNext(nextV)
                    if nextV == None:
                        vertexList.tail = prevV
                    else:
                        nextV.setPrev(prevV)
                    success = True
                currV = currV.getNext()

        if success == False:
            raise ValueError("Vertex", label, "does not exist")
        
        # Delete Edges
        currV = self.vertices.head
        while currV != None:
            vertex = currV.getValue()
            try:
                vertex.deleteEdge(label)
            except ValueError:
                pass
            currV = currV.getNext()

    def displayAsList(self):
        print("Printing Graph as an Adjacency List\n")
        currV = self.vertices.head
        while currV != None:
            vertex = currV.getValue()
            rowString = str(vertex.getLabel()) + " | "
            vList = vertex.getAdjacent()
            rowString = rowString + str(vList)
            print(rowString)
            currV = currV.getNext()

    def displayAsMatrix(self):
        print("Printing Graph as an Adjacency Matrix\n")
        rowString = '  '
        currV = self.vertices.head

        # Header Row
        while currV != None:
            label = currV.getValue().getLabel()
            rowString = rowString + str(label) + " "
            currV = currV.getNext()
        print(rowString)

        # Data Rows
        currV = self.vertices.head
        while currV != None:
            adjV = self.vertices.head
            label1 = currV.getValue().getLabel()
            rowString = str(label1) + " "
            while adjV != None:
                label2 = adjV.getValue().getLabel()
                if self.isAdjacent(label1, label2):
                    rowString = rowString + "1 "
                else:
                    rowString = rowString + "0 "
                adjV = adjV.getNext()
            print(rowString)
            currV = currV.getNext()

    def breadthFirstSearch(self):
        # NOTE: Add alphabetical sorting
        t = sq.DSAQueue()
        q = sq.DSAQueue()

        # Iterate through vertices list and clear visit
        currV = self.vertices.head
        while currV != None:
            if currV.getValue().getVisited():
                currV.getValue().clearVisited()
            currV = currV.getNext()

        v = self.vertices.head
        v.getValue().setVisited()
        q.enqueue(v)
        while not q.isEmpty():
            v = q.dequeue()
            w = v.getValue().getAdjacent().head
            while w != None:
                if not w.getValue().getVisited():
                    t.enqueue(v)
                    t.enqueue(w)
                    w.getValue().setVisited()
                    q.enqueue(w)
                w = w.getNext()
        return t
    
    def depthFirstSearch(self):
        # NOTE: Add alphabetical sorting
        t = sq.DSAQueue()
        s = sq.DSAStack()
        # Iterate through vertices list and clear visit
        currV = self.vertices.head
        while currV != None:
            if currV.getValue().getVisited():
                currV.getValue().clearVisited()
            currV = currV.getNext()

        v = self.vertices.head
        v.getValue().setVisited()
        s.push(v)
        while not s.isEmpty():
            w = v.getValue().getAdjacent().head
            while w != None:
                if not w.getValue().getVisited():
                    t.enqueue(v)
                    t.enqueue(w)
                    w.getValue().setVisited()
                    s.push(w)
                    v = w
                    w = v.getValue().getAdjacent().head
                else:
                    w = w.getNext()
            v = s.pop()
        return t
        
