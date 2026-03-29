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
'''
# WAP to store some words in dictionary

dict = {
    "table" : { "a piece of furniture" , "list of facts & figure"
    } ,

    "cat" : "a small animal"
}

print(dict)
'''

# print number from 1 to 100 

# i = 1

# while i<=100:
#     print(i)
#     i+=1

# print number from 100 to 1

# j = 100 

# while j>=1 :
#     print(j)
#     j-=1

# print the multiplication table of number n
# n = int(input("Enter number : "))

# i = 1 

# while i<=10 :
#     print(i*n)
#     i+=1


# print the element of list using the loop

# list = [1,4,9,16,25,36,49,64,81,100]
# i = 0

# while(i<len(list)):
#     print(list[i])
#     i+=1

# search for number x in tuple :
# tup = (1,4,9,16,25,36,49,64,81,100)

# x = int(input("Enter your number : "))
# i = 1

# while(i<len(tup)):
#     if(x == tup[i]):
#         print("element obtained at index : " , i)
#     i+=1

# print("end of loop")


#WAP to print the elements of list using for loop

# list = [1,4,9,16,25]

# for i in list :
#     print(i)

# search for number x in tuple using for loop

# 

# WAP to print 1 to 100 with for & range function 

# for i in range(1,101,1):
#     print(i)

# WAP to print 100 to 1 with for & range function 

# for i in range(100,0,-1):    
#     print(i)

# WAP to print multiplication table of number n 

# n = int(input("enter number : "))

# for i in range(1,11,1):
#     print(n*i)

# WAP to find sum of n number using while loop

# n = int(input("enter the number n : "))
# sum = 0
# i = 1
# while(i<=n):
#     sum += i 
#     i+=1
# print(sum)

# WAP to find the factorial of first n numbers 

# n = int(input("enter the number n : "))
# factorial = 1 
# for i in range(1 , n+1):
#     factorial *= i
# else:
#     print(factorial)



