# Functions in Python 
'''
# Function Definition 

# def calcSum(a,b): # a,b are the parameters 
#     return a+b 

# print(calcSum(2,6)) # Function calling & (2 and 6) both are arguments
# print(calcSum(34782,667814))

# def printHello():
#     print("hello")

# printHello()
# printHello()
'''

'''
# def Average(a,b,c): # User defined Functions 
#     avg = (a+b+c)/3 
#     return avg

# avgNum = Average(1,2,3)
# print(avgNum) 

# Build in functions 
    # len() , print() , type() etc..def

'''


'''
# Default parameters

def cal_prob(b,a=2): # here a is default parameter
    print(a*b)
    return a*b 

cal_prob(9)
'''

# Recursion 

# def show(a):
#     if(a==0): # Base Case 
#         return 
#     print(a)
#     show(a-1)
#     print("END")

# show(5)

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(4))
