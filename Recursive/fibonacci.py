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
print('Fibonacci Number')
n = input('\nEnter a number: ')
n = int(n) # catch not integer
option = input('[I]terative or [R]ecursive?: ')
startTime = timeit.default_timer()

if any(option == i for i in ['I', 'i']):
    fibNum = fibIterative(n)
elif any(option == i for i in ['R', 'r']):
    fibNum = fibRecursive(n)
else:
    print('That is not a valid entry. Re run the program') # add this to exception

endTime = timeit.default_timer()
runTime = endTime - startTime

print('\nThe Fibonacci Number of', n, 'is', fibNum)
print('METHOD:', option, '\tTIME:', runTime)
