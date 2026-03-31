# Class & Object in Python
'''
# class Car :
#     name = "M5 zxm"
#     brand = "BMW"

# car1 = Car()
# print(car1.name)
# print(car1.brand)
'''

class Students :
    # def __init__(self):
    #     print("default connstructor")

    def __init__(self , name , marks):
        self.name = name
        self.marks = marks
        print("parameterised constructor")

s1 = Students("karan" , 93)
print(s1.name , s1.marks)

