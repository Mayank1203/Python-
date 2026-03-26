'''
marks = [1,2,3,4,5]# this is a list
print(marks)
print(len(marks))
print(marks[3]) # Indexing 

mix = ["abcd" , 345 , "ghjk"]# this is a list
print(mix)
mix[0] = "tyuiop"
print(mix)
'''

'''
nums = [1,5,7,9,3,4]
print(nums)
print(len(nums))
print(nums[1:4])#Slicing(ending index excluded)
'''


#List Methods 
list = ['w' , 'd' , 's','f','c','k']
list.append('x') # adds one element at the end
print(list)

list.sort()
print(list)# sort in ascending order

list.sort(reverse=True) #sort in descending order
print(list)

list.reverse() #reverse the list
print(list)

list.insert(3,'a')
print(list)

list.remove('d') #remove first occurence of element 
print(list)

list.pop(5) #remove element of particular index
print(list)



