# Class & Object in Python
'''
# class Car :
#     name = "M5 zxm"
#     brand = "BMW"

# car1 = Car()
# print(car1.name)
# print(car1.brand)
'''
'''
# class Students :
#     # def __init__(self):
#     #     print("default connstructor")

#     college_name = "BSDK College" # Class Attribute

#     @staticmethod #decorator => makes static
#     def hello():
#         print("Hello")



#     def __init__(self , name , marks):
#         self.name = name # object Attribute 
#         self.marks = marks
#         print("parameterised constructor")

#     def welcome(self): # Method
#         print("welcome" , self.name)

#     def getMarks(self): # Method
#         return self.marks 

# s1 = Students("karan" , 93)
# print(s1.name , s1.marks)
# print(s1.college_name)

# Object Attribute have higher presidence as compare to Class Attribute

# s2 = Students("maya",89)
# s2.welcome()
# print(s2.getMarks())

# s2.hello()

'''

# Abstraction 
class Car:

    def __init__(self):
        self.acc=False
        self.clutch = False
        self.breake = False

    def start(self):
        self.clutch = True
        self.acc = True 
        print("Car Started")

car = Car()
car.start() # calling fuction but don't know what done inside



