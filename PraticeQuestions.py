'''
# write a programm to input 2 numbers & print their sum

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
sum = a+b
print("Sum of numbers : " , sum)
'''
'''
# WAP to input side of square & print its area

side = float(input("Enter side of Square : "))
print("Area of Square : " , side*side)
'''

'''
# WAP to input user's first name & print its length
name = input("Enter your name :")
print("length of name : " , len(name))
print(name.find('e'))
print(name.count('e'))

'''

'''
# WAP to check if a number entered ny the user is odd or even 

num = int(input("enter number to check : "))

if(num % 2 == 0):
    print("number is even")
else:
    print("number is odd")

'''

# WAP to store some words in dictionary

dict = {
    "table" : { "a piece of furniture" , "list of facts & figure"
    } ,

    "cat" : "a small animal"
}

print(dict)
