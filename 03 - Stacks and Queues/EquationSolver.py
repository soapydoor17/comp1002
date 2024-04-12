# Activity 3 of Prac 3
# EQUATION SOLVER: Creation of functions that solve equations

import StacksAndQueues as sq

class EquationError(Exception):
    ''' Exception raise when solving equation doesn't work
    '''
    pass

def _precedenceOf(operator):
    ''' Private Function that determines the order of precedence of the operators
    operator - string that is either +, -, * or /
    Function used in _parseInfixToPostfix()

    Returns 1 if operator is + or -
    Returns 2 if operator is * or /
    '''
    if (operator == '+') or (operator == '-'):
        return 1
    elif (operator == '*') or (operator =='/'):
        return 2

def _parseInfixToPostfix(equation):
    ''' Private Function that converts infix input from user to a postfix queue
    equation - string from user input
    Function used in solve()

    Returns a CircularQueue
    '''
    infixList = equation.split()
    postfixQueue = sq.CircularQueue()
    operatorStack = sq.DSAStack()
    operators = ['+', '-', '*', '/']

    for i in range(len(infixList)):
        term = infixList[i]
        if (term == '('):
            # start new sub equation
            operatorStack.push('(')

        elif (term ==')'):
            # end sub equation
            while (operatorStack.top() != '('):
                postfixQueue.enqueue(operatorStack.pop())
            operatorStack.pop()                               # removes '('

        elif any(term == o for o in operators):
            # place operators in postfix queue accordingly
            while ((not operatorStack.isEmpty()) and (operatorStack.top() != '(') and
                   (_precedenceOf(operatorStack.top()) >= _precedenceOf(term))):
                postfixQueue.enqueue(operatorStack.pop())
            operatorStack.push(term)

        else:
            # places numbers into postfixqueue
            postfixQueue.enqueue(float(term))

    while (not operatorStack.isEmpty()):
        # places remaining operators into queue
        postfixQueue.enqueue(operatorStack.pop())

    return postfixQueue

def _executeOperation(op, op1, op2):
    ''' Private Function that solves a binary opertation
    Function used in _evaluatePostfix()

    op - operater (string)
    op1 - operand to the left of operator (float)
    op2 - operand to the right of operator (float)

    Returns solution in the form of a float
    '''
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2

def _evaluatePostfix(postfixQueue):
    ''' Private Function that determines the solution to a postfix equation
    Function used in solve()

    postfixQueue - a CircularQueue of the postfix equation

    Returns the answer to the equation in the form of a float
    '''
    operandStack = sq.DSAStack()

    while not postfixQueue.isEmpty():
        term = postfixQueue.dequeue()

        if isinstance(term, float):
            operandStack.push(term)

        elif isinstance(term, str):
            op2 = operandStack.pop()
            op1 = operandStack.pop()
            binSoln = _executeOperation(term, op1, op2)
            operandStack.push(binSoln)

    if operandStack.getCount() == 1:
        return operandStack.top()
    else:
        raise EquationError('More than one term left over, input may not be formatted properly')

def solve(equation):
    ''' Public Function that solves an equation

    equation - string of equation to be solved

    Returns answer in the form of a float
    '''
    postfixQueue = _parseInfixToPostfix(equation)
    answer = _evaluatePostfix(postfixQueue)

    return answer

def main():
    print('\nEquation Solver Test')
    inputSuccess = False

    while not inputSuccess:
        try:
            equation = input('\nEnter an equation: ')
            answer = solve(equation)
            inputSuccess = True
        except ValueError:
            print("\nThat is not a valid equation. Try again")
            print("Note that operands, operators and brackets must be separated by a space")

    print('\nThe answer is', answer)

if __name__ == "__main__":
    main()
