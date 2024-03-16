# Convert a decimal number to any base
# Inspired by the following links:
# https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/ 
# https://www.geeksforgeeks.org/python-program-to-convert-decimal-to-hexadecimal/ 

import timeit

conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 
                    4: '4', 5: '5', 6: '6', 7: '7', 
                    8: '8', 9: '9', 10: 'A', 11: 'B', 
                    12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def decToAny(num, base):
    if num == 0:
        return 0
    else:
        remainder = num % base
        conversion = conversion_table[remainder]
        newNum = str(decToAny((num // base), base))
        return newNum + conversion

# Main Program
def main():
    print('Number Conversion - decimal to any base (2-16)')
    numSuccess = False
    baseSuccess = False

    while not numSuccess:
        try:
            num = input('\nEnter a number: ')
            num = int(num) # catch not integer
            if num < 0:
                raise ValueError
            numSuccess = True
        except ValueError:
            print("\nThat is not a valid input, please try again")

    while not baseSuccess:
        try:
            base = input('Enter a base: ')
            base = int(base)
            if base < 2 or base > 16:
                raise ValueError
            baseSuccess = True
        except ValueError:
            print("\nThat is not a valid input, please try again")

    startTime = timeit.default_timer()

    answer = decToAny(num, base)

    endTime = timeit.default_timer()
    runTime = endTime - startTime

    print(num, 'converted to base', base, 'is', answer)
    print('TIME:', runTime)

if __name__ == "__main__":
    main()
