import json
import EquationSolve as solve

inputData = json.load(open('inputs/in2.json'))				#Opens the JSON file and reads it. To change the input, add the file in inputs directory and change the name here 
y = solve.EquationSolver(inputData)							#Creates an instance of the Class
y.solve(inputData)											#Solves the equation and prints the solution