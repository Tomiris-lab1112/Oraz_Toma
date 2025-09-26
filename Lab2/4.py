#Python Tuples
"""
mytuple = ("apple", "banana", "cherry")
"""
#Allow Duplicates
"""
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
"""
#Tuple Length
"""
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))    #len()
"""   

#Create Tuple With One Item
"""
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
"""

#Python - Update Tuples
#Change Tuple Values
"""
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
"""

#Remove Items
"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
"""

"""
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists    #tuple completely:del
"""
