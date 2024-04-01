# Tests the functions created in EquationSolver.py

import EquationSolver

print('Equation Solver Test')
equation = input('\nEnter an equation: ')
answer = EquationSolver.solve(equation)
print('\nThe answer is', answer)
