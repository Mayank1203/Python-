'''
# info = {
#     "name" : "Raja",
#     "subjects" : ["python" , "Java"],
#     "topics" : {"dict", "set"},
#     "age" : 23,
#     "is_Adult" : True
# }

# print(info)
# print(type(info))
'''

'''
# info["name"] = "gghjdfl" # change in name 
# print(info["name"]) # Accessing values ny providing keys
# print(info["subjects"])
# print(info["topics"])
'''
'''
EmptyDict = {
}

print(EmptyDict)
EmptyDict["name"] = "Hello"
print(EmptyDict)

'''

'''
student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97 ,
        "chem" : 98 ,
        "math" : 95
    }
}

# print(student)
# print(student["subjects"])
# print(student["subjects"]["math"])

print(student.keys()) # return keys of dict
print(list(student.keys())) # return keys of dict as list
print(len(student)) # return len of dict
print(student.values()) # return values of dict
print(list(student.values())) # return values of dict as list
print(student.items()) # return pairs of dict 
print(student.get("name")) # this give value according to key 

new_dict = {"name" : "neha kumar" , "age" : 16}
student.update(new_dict) # update existing dictionay

print(student)

'''

'''
# Set in PYTHON 

collections = {1,2,3,4} # Set must be unique & immutable 
sett1 = {1,2,2,2} # repeated elements storedonly once so it resolve to {1,2}

print(collections)
print(sett1)
'''
'''

# Methods in set 


collection = set() # empty set 
print(collection)
collection.add(1)
collection.add("Hello")
collection.add(2)
collection.add(2)#override the existing value
print(collection)

collection.remove(2) # remove the element
print(collection)

collection.pop()#remove a random value
print(collection)

collection_dup = {1,45,"Hello"}
print(collection.union(collection_dup))


print(collection.intersection(collection_dup))

'''
