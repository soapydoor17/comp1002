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
print('Factorial Number')
n = input('\nEnter a number: ')
n = int(n) # catch not integer
option = input('[I]terative or [R]ecursive?: ')
startTime = timeit.default_timer()

if any(option == i for i in ['I', 'i']):
    factorial = calcNFactorialIterative(n)
elif any(option == i for i in ['R', 'r']):
    factorial = calcNFactorialRecursive(n)
else:
    print('That is not a valid entry. Re run the program') # add this to exception

endTime = timeit.default_timer()
runTime = endTime - startTime

print('\nThe factorial of', n, 'is', factorial)
print('METHOD:', option, '\tTIME:', runTime)
