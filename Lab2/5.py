#Python Sets
"""
thisset = {"apple", "banana", "cherry"}
print(thisset)
"""

"""
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)    #True
"""

"""
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)    #False
"""

"""
thisset = {"apple", "banana", "cherry"}
print(len(thisset))   #len
"""

"""
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}    #set
"""

"""
set1 = {"abc", 34, True, 40, "male"}
"""

"""
myset = {"apple", "banana", "cherry"}
print(type(myset))
"""

"""
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
"""

#Python - Access Tuple Items
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
"""

"""
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
"""

"""
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
"""

"""
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
"""

"""
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
"""

"""
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
print("Yes, 'apple' is in the fruits tuple")
"""

#Add Any Iterable

"""
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
"""

"""
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
"""

"""
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
"""

#Python - Remove Set Items
"""
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)    #using the remove()
"""

"""
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)   #discard()
"""

"""
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)   #pop()
"""

"""
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
"""

"""
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
"""

#Python - Loop Sets
"""
thisset = {"apple", "banana", "cherry"}
for x in thisset:
print(x)
"""

#Python - Join Sets
"""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
"""

"""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)
"""

"""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
"""

"""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)
"""

"""
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
"""

"""
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
"""

"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
"""

"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)
"""

#Python frozenset
"""
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
"""
