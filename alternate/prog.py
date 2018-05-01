import json
def convertToInfix(lis):
	"""This function converts a prefix expression to an infix expression

        Args:
            prefix(list): The Prefix expression as a list.
        
        Returns:
        	list: The resultant infix expression.
	"""
	lis.reverse()
	stack = []
	ans = ""
	for i in lis:
		if(type(i) is int):
			stack.append(i)
		elif(i=="x"):
			stack.append(i)
		else:
			one = stack[-1]
			stack.pop()
			two = stack[-1]
			stack.pop()
			if(type(one) is int and type(two) is int):
				temp = str(one)+i+str(two)
				stack.append(int(eval(temp)))
				print temp
			else:
				ans = "( "+str(two) +" "+str(i) +" "+ str(one) + " )"
				stack.append(ans)
	ans = stack[-1]
	return map(str,ans.split())



def getEquationInRight(infix,rhs):
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
	dictionary = {"/" : "*", "*" : "/", "-" : "+", "=" : "=", "+" : "-"}
	ans =""
	for i in infix:
		if(type(i) is str):
			if(i=="(" or i==")"):
				continue
			if(i=="x"):
				break
			if(i=="*" or i=="/" or i=="+" or i=="-"):
				ans = "( "+str(stack[-2]) +" "+dictionary[str(i)] +" "+ str(stack[-1]) + " )"
				stack.pop()
				stack.pop()
				stack.append(ans)
			else:
				stack.append(int(i))
	infix.reverse()
	for i in infix:
		if(type(i) is str):
			if(i=="(" or i==")"):
				continue
			if(i=="x"):
				break
			if(i=="*" or i=="/" or i=="+" or i=="-"):
				ans = "( "+str(stack[-2]) +" "+dictionary[str(i)] +" "+ str(stack[-1]) + " )"
				stack.pop()
				stack.pop()
				stack.append(ans)
			else:
				stack.append(int(i))
	return stack[0]
	
def convertToPrefix(data):
	"""This function recursively converts the given JSON object into an expression tree with pre-prder traversal resulting in a prefix expression.

        Args:
            data(object): The JSON Object.
        Variables:
        	dictionary(dict): Stores the equivalent unicode of the operators.
        
        Returns:
        	list: The prefix form of the expression.
        	
	"""
	prefix = []
	dictionary = {"multiply" : "*", "divide" : "/", "add" : "+", "equal" : "=", "subtract" : "-", "x" : "x" }
	for i in data.items():
   		if (type(i[1]) is dict):
   			prefix.extend( convertToPrefix(i[1]) )
   		if type(i[1]) is int:
   			prefix.append( i[1] )
   		elif type(i[1]) is unicode:
   			prefix.append( dictionary[i[1]] )
   	return prefix
data = json.load(open('in.json'))
prefixExp = convertToPrefix(data)
prefixExp.pop()
rhs = int( prefixExp[0] )
prefixExp.reverse()
prefixExp.pop()
infix = convertToInfix( prefixExp )
rhsValue = getEquationInRight(infix,rhs)
print "x =",rhsValue
print "x =",eval(rhsValue)