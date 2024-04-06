# Prac 4 Activity 3
# Interative Menu to explore the functionality of Linked Lists

import LinkedLists as ll

print('\nWelcome to the Linked List Interactive Menu\n')

linkedList = ll.DSALinkedList()
validOptions = ['I', 'R', 'D', 'X']
exit = False

while not exit:
    optionSuccess = False
    while not optionSuccess:
        try:
            print('Selection an action')
            print('[I]nsert, [R]emove, [D]isplay, e[X]it')
            option = input('Enter option: ')
            option = option.upper()
            if not any(option == o for o in validOptions):
                raise ValueError
            optionSuccess = True
        except ValueError:
            print('\nThat is not a valid option, please try again\n')

    if option == 'I':
        BESuccess = False
        valueSuccess = False

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

        while not valueSuccess:
            try:
                value = input('Enter value to insert (must be an integer): ')
                value = int(value)
                valueSuccess = True
            except ValueError:
                print('\nThat is not a valid option, please try again\n')

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

    else:
        exit = True

print('\n\nGoodbye!')
