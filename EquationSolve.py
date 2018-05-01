class EquationSolver:
	"""This class solves a linear equation with a single unknown variable and prints the value.

        Args:
            data(object): The JSON object.
            
	"""
	def __init__(self, data):
		self.data = data
	def convertToInfix(self,prefix):
		"""This function converts a prefix expression to an infix expression

        Args:
            prefix(list): The Prefix expression as a list.
        
        Returns:
        	list: The resultant infix expression.
		"""
		prefix.reverse()
		stack = []
		result = ""
		for i in prefix:
			if(type(i) is int):
				stack.append(i)
			elif(i == "x"):
				stack.append(i)
			else:
				one = stack[-1]
				stack.pop()
				two = stack[-1]
				stack.pop()
				if(type(one) is int and type(two) is int):
					temp = str(one) + i + str(two)
					stack.append(int(eval(temp)))
				else:
					result = "( " + str(two) + " " + str(i) + " " + str(one) + " )"
					stack.append(result)
		result = stack[-1]
		return map(str,result.split())


	def getEquationInRight(self,infix,rhs):
		"""This function shifts all operators and operands excluding x to the right hand side (rhs)

        Args:
            infix(list): The infix expression as a list.
            rhs(int): The initial value of the rhs provided in the JSON File
        Variables:
        	dictionary(dict): Stores the complement of the operators when shifted.
        
        Returns:
        	str: The required solution in the form x = ____
        	
		"""
		stack = []
		infix.reverse()
		stack.append(rhs)
		
		dictionary = {
		 "/" : "*" , "*" : "/",
		 "-" : "+" , "=" : "=", 
		 "+" : "-"
		 }
		result = ""
		for i in infix:
			if (type(i) is str):
				if (i == "(" or i == ")"):
					continue
				if (i == "x"):
					break
				if (i=="*" or i=="/" or i=="+" or i=="-"):
					result = "( " + str(stack[-2]) + " " + dictionary[str(i)] + " " + str(stack[-1]) + " )"
					stack.pop()
					stack.pop()
					stack.append(result)
				else:
					stack.append(int(i))
		infix.reverse()
		for i in infix:
			if (type(i) is str):
				if (i == "(" or i == ")"):
					continue
				if (i == "x"):
					break
				if (i == "*" or i == "/" or i == "+" or i == "-"):
					result = "( " + str(stack[-2]) + " " + dictionary[ str(i) ] + " " + str(stack[-1]) + " )"
					stack.pop()
					stack.pop()
					stack.append(result)
				else:
					stack.append(int(i))
		return stack[0]



	def convertToPrefix(self,data):
		"""This function recursively converts the given JSON object into an expression tree with pre-prder traversal resulting in a prefix expression.

        Args:
            data(object): The JSON Object.
        Variables:
        	dictionary(dict): Stores the equivalent unicode of the operators.
        
        Returns:
        	list: The prefix form of the expression.
        	
		"""
		prefix = []
		dictionary = {
			"multiply"  : "*"  ,   "divide" : "/", 
			"add"       : "+"  ,   "equal"  : "=",
			 "subtract" : "-"  ,   "x"      : "x" 
		}
		for i in data.items():
			if (type(i[1]) is dict):
				prefix.extend(self.convertToPrefix(i[1]))
			if type(i[1]) is int:
				prefix.append( i[1] )
			elif type(i[1]) is unicode:
				prefix.append(dictionary[i[1]])
		return prefix
		

	def solve(self, data):
		"""This function calls the required functions sequentially to solve the problem.
			
			First the prefix expression is extracted. 
			Then the '=' operand is removed and the initial rhs value is saved and removed from the prefix expression.
			Then the prefix is converted into infix and then shifted to the right and finally evaluated.
			Total Time Complexity: O(n) (Linear)
        Args:
            data(object): The JSON Object
        	
		"""
		prefixExp = self.convertToPrefix(self.data)
		prefixExp.pop() 									#Pop the operand =
		rhs = int(prefixExp[0])
		prefixExp.reverse()
		prefixExp.pop()										#Pop the initial value of RHS
		infix = self.convertToInfix(prefixExp)
		rhsValue = self.getEquationInRight(infix,rhs)
		print "x =", rhsValue
		print "x =", eval(rhsValue)
