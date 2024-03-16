# gcd.py - recursive algorithm that finds the greatest common denominator
# Taken from: https://www.geeksforgeeks.org/program-to-find-gcd-or-hcf-of-two-numbers/

import timeit

''' Euclidean Algorithm by Subtraction
The GCD doesn't change if the smaller number is subtracted by the larger number
Optimised by checking if one number is a factor of another
TIME COMPLEXITY - O(min(a,b))

a - first number
b - second number
'''
def gcdSub(a,b):
    # Everything divides by 0
    if a == 0:
        return b
    elif b == 0:
        return a
    
    # Base Case
    elif a == b:
        return a
    
    # Recursive calls
    elif a > b:
        if a % b == 0:      # checking if b is a factor of a
            return b
        else:
            return gcdSub(a-b, a)
    elif b % a == 0:        # b > a, cheacking if a is a factor of b
        return a
    else:
        return gcdSub(a, b-a)


''' Euclidean Algorithm - Optimised using Division
Continuously divide the bigger number by the smaller one
TIME COMPLEXITY - O(log(min(a,b)))

a - first number
b - second number
'''
def gcdDiv(a,b):
    # Everything divides by 0
    if (b==0):
        return a
    else:
        return gcdDiv(b, a%b)

# Main Program
def main():
    print('Greatest Common Denominator')
    num1Success = False
    num2Success = False
    optionSuccess = False
    validOptions = ['S', 'D']

    while not num1Success:
        try:
            num1 = input('\nEnter a number: ')
            num1 = int(num1)
            if num1 < 0:
                raise ValueError
            num1Success = True
        except ValueError:
            print("\nThat is not a valid number, please try again")

    while not num2Success:
        try:
            num2 = input('Enter a second number: ')
            num2 = int(num2)
            if num2 < 0:
                raise ValueError
            num2Success = True
        except ValueError:
            print("\nThat is not a valid number, please try again")

    while not optionSuccess:
        try:
            option = input('Euclidean Algorithm by [S]ubtraction or [D]ivision: ')
            option = option.upper()
            if not any(option == o for o in validOptions):
                raise ValueError
            optionSuccess = True
        except ValueError:
            print("\nThat is not a valid input, please try again")

    startTime = timeit.default_timer()

    if any(option == i for i in ['S', 's']):
        gcd = gcdSub(num1, num2)
    elif any(option == i for i in ['D', 'd']):
        gcd = gcdDiv(num1, num2)

    endTime = timeit.default_timer()
    runTime = endTime - startTime

    print('\nThe Greatest Common Denominator of', num1, 'and', num2, 'is', gcd)
    print('METHOD:', option, '\tTIME:', runTime)

if __name__ == "__main__":
    main()
