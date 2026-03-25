'''
str1 = 'hello'
str2 = "world"

print(str1 ,str2)

str3 = "hello world!. \n good"
print(str3)

str4 = "hello world!. \t good"
print(str4)

'''

'''
str1 = "Apna"
print(len(str1) , str1)

str2 = "College"
print(len(str2) , str2)

finalStr = str1 + " " + str2 # concatenation 
print(len(finalStr) , finalStr)
'''

'''
str = "asdf ghjkl"
print(str[5]) # Indexing
print(str[2])
print(str[9])
'''

'''
str = "Apna College"
print(str[2:7]) # Slicing (ending not included)
print(str[2:]) # 2-11
print(str[:7]) # 0-7

str1 = "apple"
print(str1[-3:-1]) # Negative Slicing 
'''

'''
str = "i am a coder."
print(str.endswith("er.")) # return true if string ends with sub-string
print(str.capitalize())# capitalize 1st char
print(str.replace("a" , "the"))# replace all occurances of old to new 
print(str.find("c")) # return 1st index of 1st occurrer
print(str.count('i'))# counts the occurrence of sub string

'''

age = 34 

if(age>=18):
    print("can vote")
else:
    print("can't vote")

signal = "red"

if(signal == "green"):
    print("you can go")
elif(signal == "yellow"):
    print("you have to wait")
else:
    print("stop")

