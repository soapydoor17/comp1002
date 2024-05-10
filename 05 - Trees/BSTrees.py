# BSTrees.py - file defining binary search trees

import LinkedLists as ll

class DSATreeNode():
    def __init__(self, inKey, inValue):
        self._key = inKey
        self._value = inValue
        self._right = None
        self._left = None

    def getKey(self):
        return self._key
    
    def setKey(self, inKey):
        self._key = inKey

    def getValue(self):
        return self._value
    
    def setValue(self, inValue):
        self._value = inValue

    def getRight(self):
        return self._right
    
    def setRight (self, inRight):
        self._right = inRight

    def getLeft(self):
        return self._left

    def setLeft(self, inLeft):
        self._left = inLeft

    def __str__(self):
        return ("Key: " + str(self.getKey()) + "\tValue: " + str(self.getValue()))
    
class DSABinarySearchTree():
    def __init__(self):
        self._root = None

    def getRoot(self):
        return self._root
    
    def setRoot(self, inRoot):
        self._root = inRoot

    def _findRec(self, key, curr):
        value = None

        if curr == None:
            # Base Case: Not Found
            raise ValueError("Key " + key + " not found")
        
        elif key == curr.getKey():
            # Base case: found
            value = curr.getValue()

        elif key < curr.getKey():
            # Go left if key less than current key
            value = self._findRec(key, curr.getLeft())

        elif key > curr.getKey():
            # Go right if key is greater than current key
            value = self._findRec(key, curr.getRight())

        return value

    def find(self, key):
        return self._findRec(key, self.getRoot())
    
    def _insertRec(self, key, data, curr):
        updateNd = curr

        if curr == None:
            # Base case: found
            newNd = DSATreeNode(key, data)
            updateNd = newNd
            if curr == self.getRoot():
                # If this is the first node in the tree, set it as the root
                self.setRoot(updateNd)

        elif key == curr.getKey():
            # Base case: Key is already in tree
            raise ValueError("Key", key, "is already in tree")
        
        elif key < curr.getKey():
            # Recurse left if key less than current key
            curr.setLeft(self._insertRec(key, data, curr.getLeft()))

        else:
            # Else recurse right
            curr.setRight(self._insertRec(key, data, curr.getRight()))

        return updateNd
    
    def insert(self, key, data):
        self._insertRec(key, data, self.getRoot())

    def _promoteSuccessor(self, curr):
        successor = curr

        if curr.getLeft() != None:
            successor = self._promoteSuccessor(curr.getLeft())
            if successor == curr.getLeft():
                curr.setLeft(successor.getRight())

        return successor
    
    def _deleteNode(self, delNd):
        updateNd = None

        if delNd.getLeft() == None and delNd.getRight() == None:
            # No Children
            updateNd = None

        elif delNd.getLeft() != None and delNd.getRight() == None:
            # One child - left
            updateNd = delNd.getLeft()

        elif delNd.getLeft() == None and delNd.getRight() != None:
            # One child - right
            updateNd = delNd.getRight()

        else:
            # Two children
            updateNd = self._promoteSuccessor(delNd.getRight())
            if updateNd != delNd.getRight():
                updateNd.setRight(delNd.getRight())
            updateNd.setLeft(delNd.getLeft())

        return updateNd
    
    def _deleteRec(self, key, curr):
        updateNd = curr

        if curr == None:
            # Base case: Not in the tree
            raise ValueError("Key", key, "is not in the tree")
        
        elif key == curr.getKey():
            # Base case: Found
            updateNd = self._deleteNode(curr)

        elif key < curr.getKey():
            # Recurse left
            curr.setLeft(self._deleteRec(key, curr.getLeft()))

        else:
            # Recurse right
            curr.setRight(self._deleteRec(key, curr.getRight()))

        return updateNd

    def delete(self, key):
        self._root = self._deleteRec(key, self.getRoot())

    def _heightRec(self, currNd):
        if currNd == None:
            # Base case: no more along branch
            htSoFar = -1

        else:
            leftHt = self._heightRec(currNd.getLeft())
            rightHt = self._heightRec(currNd.getRight())

            if leftHt > rightHt:
                htSoFar = leftHt + 1

            else:
                htSoFar = rightHt + 1

        return htSoFar
    
    def height(self):
        return self._heightRec(self.getRoot())
    
    def min(self):
        currNd = self.getRoot()
        while currNd.getLeft() != None:
            currNd = currNd.getLeft()
        minKey = currNd.getKey()
        return minKey
    
    def max(self):
        currNd = self.getRoot()
        while currNd.getRight() != None:
            currNd = currNd.getRight()
        maxKey = currNd.getKey()
        return maxKey

    def balance(self):
        leftHeight = self._heightRec(self.getRoot().getLeft()) + 1
        rightHeight = self._heightRec(self.getRoot().getRight()) + 1

        if leftHeight > rightHeight:
            balPercent = (rightHeight / leftHeight) * 100
        else:
            balPercent = (leftHeight / rightHeight) * 100
        
        return balPercent

    def _inorderRec(self, curr, inList):
        if curr != None:
            inList = self._inorderRec(curr.getLeft(), inList)
            inList.insertLast(curr)
            inList = self._inorderRec(curr.getRight(), inList)
        return inList

    def inorder(self):
        inList = ll.DSALinkedList()
        return self._inorderRec(self.getRoot(), inList)
    
    def _preorderRec(self, curr, preList):
        if curr != None:
            preList.insertLast(curr)
            preList = self._preorderRec(curr.getLeft(), preList)
            preList = self._preorderRec(curr.getRight(), preList)
        return preList

    def preorder(self):
        preList = ll.DSALinkedList()
        return self._preorderRec(self.getRoot(), preList)

    def _postorderRec(self, curr, postList):
        if curr != None:
            postList = self._postorderRec(curr.getLeft(), postList)
            postList = self._postorderRec(curr.getRight(), postList)
            postList.insertLast(curr)
        return postList
    
    def postorder(self):
        postList = ll.DSALinkedList()
        return self._postorderRec(self.getRoot(), postList)
