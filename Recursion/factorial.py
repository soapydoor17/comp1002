import timeit

# Iterative
def calcNFactorialIterative(n):
    nFactorial = 1
    for ii in range(n, 1, -1):
        nFactorial = nFactorial * ii
    return nFactorial

# Recursive
def calcNFactorialRecursive(n):
    factorial = 1
    if (n<0):
        # Error Condition
        raise ValueError("Must not be negative")
    elif (n==0):
        # Base Case
        factorial = 1
    else:
        factorial = n * calcNFactorialRecursive(n-1)
    return factorial


# Main Program
def main():
    print('Factorial Number\n')
    numSuccess = False
    optionSuccess = False
    validOptions = ['I', 'R']

    while not numSuccess:
        try:
            n = input('Enter a number: ')
            n = int(n) # catch not integer
            if n < 0:
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
        factorial = calcNFactorialIterative(n)
    elif option == 'R':
        factorial = calcNFactorialRecursive(n)

    endTime = timeit.default_timer()
    runTime = endTime - startTime

    print('\nThe factorial of', n, 'is', factorial)
    print('METHOD:', option, '\tTIME:', runTime)

if __name__ == "__main__":
    main()
