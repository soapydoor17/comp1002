import timeit

# Iterative
def fibIterative(n):
    fibVal = 0
    currVal = 1
    lastVal = 0

    if (n==0):
        fibVal = 0
    elif (n==1):
        fibVal = 1
    else:
        for ii in range(2, n+1):
            fibVal = currVal + lastVal
            lastVal = currVal
            currVal = fibVal
    return fibVal

# Recursive
def fibRecursive(n):
    fibVal = 0

    if (n==0):
        fibVal = 0
    elif (n==1):
        fibVal = 1
    else:
        fibVal = fibRecursive(n-1) + fibRecursive(n-2)
    return fibVal


# Main Program
def main():
    print('Fibonacci Number')
    numSuccess = False
    optionSuccess = False
    validOptions = ['I', 'R']

    while not numSuccess:
        try:
            n = input('Enter a number: ')
            n = int(n) # catch not integer
            if n < 0 or n > 50:
                raise ValueError
            numSuccess = True
        except ValueError:
            print("\nThat is not a valid number, please try again")

    while not optionSuccess:
        try:
            option = input('[I]terative or [R]ecursive?: ')
            option = option.upper()
            if not any(option == o for o in validOptions):
                raise ValueError
            optionSuccess = True
        except ValueError:
            print("\nThat is not a valid input, please try again")

    startTime = timeit.default_timer()

    if option == 'I':
        fibNum = fibIterative(n)
    elif option == 'R':
        fibNum = fibRecursive(n)

    endTime = timeit.default_timer()
    runTime = endTime - startTime

    print('\nThe Fibonacci Number of', n, 'is', fibNum)
    print('METHOD:', option, '\tTIME:', runTime)

if __name__ == "__main__":
    main()
