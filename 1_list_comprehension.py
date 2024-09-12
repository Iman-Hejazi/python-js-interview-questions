'''
write a list comprehension to make a list the values from 
the (key: value) pairs in the following dictionary
Expected Result: [5, 2, 11, 4]
'''

data = {
    "a": 5,
    "b": 2,
    "c": 11,
    "d": 4
}

# Your answer
result = [value for value in data.values()]
print(result)
