# Python program to convert infix expression to postfix

# Class to convert the expression

def infixToPostfix(infix):
    class Conversion:
            
            # Constructor to initialize the class variables
            def __init__(self, capacity):
                    self.top = -1
                    self.capacity = capacity
                    # This array is used a stack
                    self.array = []
                    # Precedence setting
                    self.output = []
                    self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
            
            # check if the stack is empty
            def isEmpty(self):
                    return True if self.top == -1 else False
            
            # Return the value of the top of the stack
            def peek(self):
                    return self.array[-1]
            
            # Pop the element from the stack
            def pop(self):
                    if not self.isEmpty():
                            self.top -= 1
                            return self.array.pop()
                    else:
                            return "$"
            
            # Push the element to the stack
            def push(self, op):
                    self.top += 1
                    self.array.append(op)

            # A utility function to check is the given character
            # is operand
            def isOperand(self, ch):
                    return ch.isalpha()

            # Check if the precedence of operator is strictly
            # less than top of stack or not
            def notGreater(self, i):
                    try:
                            a = self.precedence[i]
                            b = self.precedence[self.peek()]
                            return True if a <= b else False
                    except KeyError:
                            return False
                            
            # The main function that
            # converts given infix expression
            # to postfix expression
            def InfixToPostfix(self, exp):
                    
                    # Iterate over the expression for conversion
                    for i in exp:
                            # If the character is an operand,
                            # add it to output
                            if self.isOperand(i):
                                    self.output.append(i)
                            
                            # If the character is an '(', push it to stack
                            elif i == '(':
                                    self.push(i)

                            # If the scanned character is an ')', pop and
                            # output from the stack until and '(' is found
                            elif i == ')':
                                    while( (not self.isEmpty()) and
                                                                    self.peek() != '('):
                                            a = self.pop()
                                            self.output.append(a)
                                    if (not self.isEmpty() and self.peek() != '('):
                                            return -1
                                    else:
                                            self.pop()

                            # An operator is encountered
                            else:
                                    while(not self.isEmpty() and self.notGreater(i)):
                                            self.output.append(self.pop())
                                    self.push(i)

                    # pop all the operator from the stack
                    while not self.isEmpty():
                            self.output.append(self.pop())

                    return ("".join(self.output))

    # Driver program to test above function
    obj = Conversion(len(infix))
    return obj.InfixToPostfix(infix)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)



























#infixToPrefix
def infixToPrefix(expr):
    class infix_to_prefix:
        precedence={'^':5,'*':4,'/':4,'+':3,'-':3,'(':2,')':1}
        def __init__(self):
            self.items=[]
            self.size=-1
        def push(self,value):
            self.items.append(value)
            self.size+=1
        def pop(self):
            if self.isempty():
                return 0
            else:
                self.size-=1
                return self.items.pop()
        def isempty(self):
            if(self.size==-1):
                return True
            else:
                return False
        def seek(self):
            if self.isempty():
                return False
            else:
                return self.items[self.size]
        def is0perand(self,i):
            if i.isalpha() or i in '1234567890':
                return True
            else:
                return False
        def reverse(self,expr):
            rev=""
            for i in expr:
                if i == '(':
                    i=')'
                elif i == ')':
                    i='('
                rev=i+rev
            return rev
        def InfixToPrefix (self,expr):
            prefix=""
            #print('prefix expression after every iteration is:')
            for i in expr:
                if(len(expr)%2==0):
                    print("Incorrect infix expr")
                    return False
                elif(self.is0perand(i)):
                    prefix +=i
                elif(i in '+-*/^'):
                    while(len(self.items)and self.precedence[i] < self.precedence[self.seek()]):
                        prefix+=self.pop()
                    self.push(i)
                elif i == '(':
                    self.push(i)
                elif i == ')':
                    o=self.pop()
                    while o!='(':
                        prefix +=o
                        o=self.pop()
                #print(prefix)
                    #end of for
            while len(self.items):
                if(self.seek()=='('):
                    self.pop()
                else:
                    prefix+=self.pop()
                    #print(prefix)
            return prefix
    s=infix_to_prefix()
    rev=""
    rev=s.reverse(expr)
    #print(rev)
    result=s.InfixToPrefix(rev)
    if (result!=False):
        
        prefix=s.reverse(result)
        return prefix
































# Python Program to convert prefix to Infix
def prefixToInfix(prefix):
	stack = []
	
	# read prefix in reverse order
	i = len(prefix) - 1
	while i >= 0:
		if not isOperator(prefix[i]):
			
			# symbol is operand
			stack.append(prefix[i])
			i -= 1
		else:
		
			# symbol is operator
			str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
			stack.append(str)
			i -= 1
	
	return stack.pop()

def isOperator(c):
	if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
		return True
	else:
		return False

# This code is contributed by avishekarora

































# Prefix to Postfix: 
# -*- coding: utf-8 -*-
def prefixToPostfix(s):
    # Example Input

    # Stack for storing operands
    stack = []

    operators = set(['+', '-', '*', '/', '^'])

    # Reversing the order
    s = s[::-1]

    # iterating through individual tokens
    for i in s:

            # if token is operator
            if i in operators:

                    # pop 2 elements from stack
                    a = stack.pop()
                    b = stack.pop()

                    # concatenate them as operand1 +
                    # operand2 + operator
                    temp = a+b+i
                    stack.append(temp)

            # else if operand
            else:
                    stack.append(i)

    # printing final output
    return stack










































# Python3 program to find infix for
# a given postfix.
def isOperand(x):
    return ((x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z'))

# Get Infix for a given postfix
# expression
def postfixToInfix(exp) :
    exp = exp.strip()
    s = []
    for i in exp:	
            
            # Push operands
            if (isOperand(i)) :		
                    s.insert(0, i)
                    
            # We assume that input is a
            # valid postfix and expect
            # an operator.
            else:
            
                    op1 = s[0]
                    s.pop(0)
                    op2 = s[0]
                    s.pop(0)
                    s.insert(0, "(" + op2 + i +
                                                    op1 + ")")
                    
    # There must be a single element in
    # stack now which is the required
    # infix.
    return s[0]


# This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)



































# Python3 Program to convert postfix to prefix

# function to check if
# character is operator or not


def isOperator2(x):

	if x == "+":
		return True

	if x == "-":
		return True

	if x == "/":
		return True

	if x == "*":
		return True

	return False

# Convert postfix to Prefix expression


def postfixToPrefix(post_exp):

	s = []

	# length of expression
	length = len(post_exp)

	# reading from right to left
	for i in range(length):

		# check if symbol is operator
		if (isOperator2(post_exp[i])):

			# pop two operands from stack
			op1 = s[-1]
			s.pop()
			op2 = s[-1]
			s.pop()

			# concat the operands and operator
			temp = post_exp[i] + op2 + op1

			# Push string temp back to stack
			s.append(temp)

		# if symbol is an operand
		else:

			# push the operand to the stack
			s.append(post_exp[i])

	
	ans = ""
	for i in s:
		ans += i
	return ans

# This code is contributed by AnkitRai01

