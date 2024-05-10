# BSTInteractiveMenu.py - Interative Menu to explore the functionality of Binary Seach Trees

import BSTrees as bst

print('\nWelcome to the Binary Search Tree Interactive Menu\n')

bsTree = bst.DSABinarySearchTree()
exit = False

while not exit:
    optionSuccess = False
    while not optionSuccess:
        try:
            print('Selection an action')
            print('[A]dd a node, [R]emove a node, [D]isplay, [O]ther, e[X]it')
            option = input('Enter option: ')
            option = option.upper()
            if not (option == 'A' or option == 'R' or option == 'D' or option == 'X' or option == 'O'):
                raise ValueError
            optionSuccess = True
        except ValueError:
            print('\nThat is not a valid option, please try again\n')

    if option == 'A':
        keySuccess = False

        while not keySuccess:
            try:
                inKey = input('Enter a key: ')
                inKey = int(inKey) 
                inValue = input('Enter value to insert: ')
                bsTree.insert(inKey, inValue)
                keySuccess = True
            except ValueError:
                print('\nThat is not a valid option, please try again')

        print("\nNode has been inserted\n")

    elif option == 'R':

        if bsTree.getRoot() == None:
            print('\nCannot remove any items as the tree is empty\n')
        else:
            try:
                inKey = input('Enter a key to remove: ')
                inKey = int(inKey)
                bsTree.delete(inKey)
                print('\nRemoved key', inKey, 'from the tree\n')
            except ValueError:
                print('\nCould not remove as key', inKey, 'is not in the tree\n')

    elif option == 'D':
        if bsTree.getRoot() == None:
            print('\nThe tree is currently empty')
        else:
            print()
            displaySuccess = False

            while not displaySuccess:
                try:
                    print('\n[I]norder, p[R]eorder or p[O]storder')
                    displayChoice = input('Enter option: ')
                    displayChoice = displayChoice.upper()
                    if not (displayChoice == 'I' or displayChoice == 'R' or displayChoice == 'O'):
                        raise ValueError
                    displaySuccess = True
                except ValueError:
                    print('\nThat is not a valid option, please try again')

            if displayChoice == 'I':
                # INORDER
                treeList = bsTree.inorder()
                print('\nPrinting Inorder\n')
            elif displayChoice == 'R':
                # PREORDER
                treeList = bsTree.preorder()
                print('\nPrinting Preorder\n')
            else:
                # POSTORDER
                treeList = bsTree.postorder()
                print('\nPrinting Postorder\n')

            print(treeList)
        print()

    elif option == 'O':
        otherSuccess = False

        while not otherSuccess:
            try:
                print('\nm[I]nimum, m[A]ximum, [H]eight, or [B]alance, [F]ind')
                otherChoice = input("Enter option: ")
                otherChoice = otherChoice.upper()
                if not (otherChoice == 'I' or otherChoice == 'A' or otherChoice == 'H' or otherChoice == 'B' or otherChoice == 'F'):
                    raise ValueError
                otherSuccess = True
            except ValueError:
                print('\nThat is not a valid option, please try again')

        if otherChoice == 'I':
            print('\nMin Value:', bsTree.min(), '\n')
        elif otherChoice == 'A':
            print('\nMax Value:', bsTree.max(), '\n')
        elif otherChoice == 'H':
            print('\nHeight of Tree:', bsTree.height(), '\n')
        elif otherChoice == 'F':
            findNode = input('What node do you want to find: ')
            findNode = findNode.upper()
            try:
                bsTree.find(findNode)
                print("\n", findNode, "is in the tree\n")
            except ValueError:
                print("\n", findNode, "is NOT in the tree\n")
        else:
            print('\nBalance Percentage:', bsTree.balance(), '%\n')

    else:
        exit = True

print('\n\nGoodbye!')
