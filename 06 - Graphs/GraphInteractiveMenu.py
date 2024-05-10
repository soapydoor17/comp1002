# BSTInteractiveMenu.py - Interative Menu to explore the functionality of Binary Seach Trees

import Graphs as g
import StacksAndQueues as sq
import LinkedLists as ll

print('\nWelcome to the Binary Search Tree Interactive Menu\n')

graph = g.DSAGraph()
exit = False

while not exit:
    optionSuccess = False
    while not optionSuccess:
        try:
            print('Selection an action')
            print('[A]dd a vertex/edge, [R]emove a vertex/edge, [D]isplay, [S]earch, [O]ther, e[X]it')
            option = input('Enter option: ')
            option = option.upper()
            if not (option == 'A' or option == 'R' or option == 'D' or option == 'X' or option == 'S' or option == 'O'):
                raise ValueError
            optionSuccess = True
        except ValueError:
            print('\nThat is not a valid option, please try again\n')

    if option == 'A':
        veSuccess = False
        while not veSuccess:
            try:
                print("\nAdd a [V]ertex or an [E]dge?")
                veOption = input('Enter option: ')
                veOption = veOption.upper()
                if not (veOption == 'V' or veOption == 'E'):
                    raise ValueError
                veSuccess = True
            except ValueError:
                print('\nThat is not a valid option, please try again')

        if veOption == 'V':
            # Add vertex
            try:
                inKey = input('Enter a key: ')
                inKey = inKey.upper()
                inValue = input('Enter value to insert: ')
                graph.addVertex(inKey, inValue)
                print('\nVertex', inKey, 'has been added\n')
            except ValueError:
                print('\nThat is not a valid option, please try again\n')

        else:
            # Add edge
            keySuccess = False
            while not keySuccess:
                try:
                    inKey1 = input('Enter the first key: ')
                    inKey1 = inKey1.upper()
                    inKey2 = input('Enter the second key: ')
                    inKey2 = inKey2.upper()
                    keySuccess = True
                    graph.addEdge(inKey1, inKey2)
                    print('\nEdge', inKey1, inKey2, 'has been added\n')
                except ValueError:
                    print('That is not a valid entry, please try again\n')

    elif option == 'R':
        veSuccess = False
        while not veSuccess:
            try:
                print("\nAdd a [V]ertex or an [E]dge?")
                veOption = input('Enter option: ')
                veOption = veOption.upper()
                if not (veOption == 'V' or veOption == 'E'):
                    raise ValueError
                veSuccess = True
            except ValueError:
                print('\nThat is not a valid option, please try again\n')

        if veOption == 'V':
            # Remove vertex
            try:
                inKey = input('Enter a key: ')
                inKey = inKey.upper()
                graph.deleteVertex(inKey)
                keySuccess = True
                print("\nVertex", inKey, "has been deleted\n")
            except ValueError:
                print('\nVertex deletion was not successful\n')

        else:
            # Remove edge
            keySuccess = False
            while not keySuccess:
                try:
                    inKey1 = input('Enter the first key: ')
                    inKey1 = inKey1.upper()
                    inKey2 = input('Enter the second key: ')
                    inKey2 = inKey2.upper()
                    graph.deleteEdge(inKey1, inKey2)
                    keySuccess = True
                    print('\nEdge', inKey1, inKey2, 'has been deleted\n')
                except ValueError:
                    print('\nEdge deletion was not successful\n')

    elif option == 'D':
        if graph.vertices.head == None:
            print('\nThe graph is currently empty')
        else:
            print()
            displaySuccess = False

            while not displaySuccess:
                try:
                    print('\nDisplay as a [L]ist or a [M]atrix')
                    displayChoice = input('Enter option: ')
                    displayChoice = displayChoice.upper()
                    if not (displayChoice == 'L' or displayChoice == 'M'):
                        raise ValueError
                    displaySuccess = True
                except ValueError:
                    print('\nThat is not a valid option, please try again')

            if displayChoice == 'L':
                graph.displayAsList()
            else:
                graph.displayAsMatrix()
        
        print()

    elif option == 'S':
        bdSuccess = False

        if graph.vertices.isEmpty():
            print('\n Graph is currently empty')

        else:
            while not bdSuccess:
                try:
                    print('\n[B]readth-first or [D]epth-first search')
                    searchChoice = input('Enter choice: ')
                    searchChoice = searchChoice.upper()
                    if not (searchChoice == 'B' or searchChoice == 'D'):
                        raise ValueError
                    bdSuccess = True
                except ValueError:
                    print('\nThat is not a valid option please try again')

            if searchChoice == 'B':
                # Breadth first
                searchQueue = graph.breadthFirstSearch()
                print('\nPrinting Breadth First Seach:\n')
            elif searchChoice == 'D':
                # Depth first
                searchQueue = graph.depthFirstSearch()
                print('\nPrinting Depth First Seach:\n')

            while not searchQueue.isEmpty():
                v1 = searchQueue.dequeue().getValue()
                v2 = searchQueue.dequeue().getValue()
                print(v1.getLabel(), v2.getLabel())

        print()



    elif option == 'O':
        otherSuccess = False

        while not otherSuccess:
            try:
                print('\n[H]as vertex, [V]ertex count, [E]dge count, [G]et vertex, get [A]djacent, [I]s adjacent')
                otherChoice = input("Enter option: ")
                otherChoice = otherChoice.upper()
                if not (otherChoice == 'H' or otherChoice == 'V' or otherChoice == 'E' or otherChoice == 'G' or otherChoice == 'A' or otherChoice == 'I'):
                    raise ValueError
                otherSuccess = True
            except ValueError:
                print('\nThat is not a valid option, please try again')

        if otherChoice == 'H':
            label = input('Enter the label to find: ')
            label = label.upper()
            success = graph.hasVertex(label)
            print()
            if success:
                print(label, 'is in the graph')
            else:
                print(label, 'is NOT in the graph')
            print()
        
        elif otherChoice == 'V':
            count = graph.getVertexCount()
            print('\nVertex Count:', count, '\n')
        
        elif otherChoice == 'E':
            count = graph.getEdgeCount()
            print('\nEdge Count:', count, '\n')
        
        elif otherChoice == 'G':
            label = input('Enter the label to find: ')
            label = label.upper()
            try:
                graph.getVertex(label)
                print()
                print(label, 'has been found and is in the graph\n')
            except ValueError:
                print()
                print(label, 'is NOT in the graph as an error was brought up whilst running this command\n')

        elif otherChoice == 'A':
            label = input('Enter a label: ')
            label = label.upper()
            try:
                adjList = graph.getAdjacent(label)
                print('\nPrinting adjacent vertices of ', label)
                print(adjList)
                print()
            except ValueError:
                print('\nAdjacent vertices not found as this label isn\'t in the tree\n')
                
        elif otherChoice == 'I':
            label1 = input('Enter first label: ')
            label1 = label1.upper()
            label2 = input('Enter second label: ')
            label2 = label2.upper()
            if graph.hasVertex(label2):
                try:
                    success = graph.isAdjacent(label1, label2)
                    if success:
                        print()
                        print(label1, 'is adjacent to', label2)
                    else:
                        print()
                        print(label1, 'is not adjacent to', label2)
                except ValueError:
                    print('\nError was raised as', label1, 'doesn\'t exist')
                print()
            else:
                print('\n', label2, 'does not exist in this graph')

    else:
        exit = True

print('\n\nGoodbye!')
