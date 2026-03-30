# I/O file in Python

'''
# f = open("demo.txt","r")

# data = f.read()
# print(data)
'''

'''
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()
'''
'''
# f = open("demo.txt","w") # w means overriding the existing once

# f.write("I have to complete this in 2 days only")

# f.close()
'''


'''
f = open("demo.txt","a") # a means add the existing once

f.write("\n Tomorrow is the last day")

f.close()
'''

'''

# with syntax in file 

# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("new data")
'''

import os

os.remove("demo.txt")

