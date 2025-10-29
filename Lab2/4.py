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
"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)    # built-in append()
"""

"""
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
"""

"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
"""

"""
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
"""

#Python - Unpack Tuples
"""
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
"""

"""
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
"""

"""
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
"""

#Python - Loop Tuples
"""
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
print(x)
"""

"""
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
print(thistuple[i])
"""

"""
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
print(thistuple[i])
i = i + 1
"""

#Python - Join Tuples
"""
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
"""

"""
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
"""

