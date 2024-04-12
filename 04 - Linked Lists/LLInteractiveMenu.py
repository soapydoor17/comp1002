# Prac 4 Activity 3
# Interative Menu to explore the functionality of Linked Lists

import LinkedLists as ll

print('\nWelcome to the Linked List Interactive Menu\n')

linkedList = ll.DSALinkedList()
validOptions = ['I', 'R', 'D', 'X', 'P']
exit = False

while not exit:
    optionSuccess = False
    while not optionSuccess:
        try:
            print('Selection an action')
            print('[I]nsert, [R]emove, [D]isplay, [P]eek, e[X]it')
            option = input('Enter option: ')
            option = option.upper()
            if not any(option == o for o in validOptions):
                raise ValueError
            optionSuccess = True
        except ValueError:
            print('\nThat is not a valid option, please try again\n')

    if option == 'I':
        BESuccess = False

        while not BESuccess:
            try:
                print('\nInsert at the [B]eginning or [E]nd')
                begend = input('Enter option: ')
                begend = begend.upper()
                if not any(begend == o for o in ['B', 'E']):
                    raise ValueError
                BESuccess = True
            except ValueError:
                print('\nThat is not a valid option, please try again')

        value = input('Enter value to insert: ')

        print()

        if begend == 'B':
            linkedList.insertFirst(value)
            print('Inserted', value, 'at the beginning of the linked list\n')
        else:
            linkedList.insertLast(value)
            print('Inserted', value, 'at the end of the linked list\n')

    elif option == 'R':
        BESuccess = False

        if linkedList.isEmpty():
            print('\nCannot remove any items as the linked list is empty\n')
        else:
            while not BESuccess:
                try:
                    print('\nRemove at the [B]eginning or [E]nd')
                    begend = input('Enter option: ')
                    begend = begend.upper()
                    if not any(begend == o for o in ['B', 'E']):
                        raise ValueError
                    BESuccess = True
                except ValueError:
                    print('\nThat is not a valid option, please try again')

            if begend == 'B':
                removedVal = linkedList.removeFirst()
                print('\nRemoved', removedVal, 'from the beginning of the linked list\n')
            else:
                removedVal = linkedList.removeLast()
                print('\nRemoved', removedVal, 'from the end of the linked list\n')

    elif option == 'D':
        if linkedList.isEmpty():
            print('\nThe list is currently empty')
        else:
            print()
            currNd = linkedList.head
            while currNd != None:
                print(currNd.getValue())
                currNd = currNd.getNext()
        print()

    elif option == 'P':
        FLsuccess = False

        if linkedList.isEmpty():
            print('\nCannot peek any items as the linked list is empty\n')
        else:
            while not FLsuccess:
                try:
                    print('\nPeek the [F]irst or [L]ast value?')
                    firstLast = input("Enter option: ")
                    firstLast = firstLast.upper()
                    if not any(firstLast == o for o in ['F', 'L']):
                        raise ValueError
                    FLsuccess = True
                except ValueError:
                    print('\nThat is not a valid option, please try again')

            if firstLast == 'F':
                print('\nFirst Value:', linkedList.peekFirst(), '\n')
            else:
                print('\nLast Value:', linkedList.peekLast(), '\n')

    else:
        exit = True

print('\n\nGoodbye!')
