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