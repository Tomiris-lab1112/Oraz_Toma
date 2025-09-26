<<<<<<< HEAD
if 5 > 2:
  print("Five is greater than two!")
=======
#Python Lists
"""
thislist = ["apple", "banana", "cherry"]
print(thislist)
""" 

#Allow Duplicates  #разрешений дубликата 
"""
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
"""

#List Length     #the function:len()
"""
thislist = ["apple", "banana", "cherry"]
print(len(thislist))    #количество элементов в списке - 3 
"""

#List Items - Data Types
"""
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]    #Типы данных string, int и boolean:
"""

#type()
"""
mylist = ["apple", "banana", "cherry"]
print(type(mylist))   #объекты с типом данных 'list'
"""

#The list() Constructor
"""
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)    #использовать конструктор list() при создании Новый список
"""

#Python - Access List Items  #Доступ к элементам
"""
Элементы списка индексируются, и вы можете получить к ним доступ, обратившись к порядковому номеру:
Вернет 3,4,5 пункт

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])    
"""

#Range of Negative Indexes
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])  #ответь будет апельсин киви дыная
"""

#Python - Change List Items
"""
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
"""
#Change a Range of Item Values
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) 
"""
#Insert Items
"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
"""
#Python - Add List Items
"""
hislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)     #append()
""" 

#Insert Items
"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)   #insert()
"""

#Extend List
"""
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)     #extend()  и используется tropical thislist
"""
#Add Any Iterable
"""
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)     #extend()
"""
#Range of Indexes
"""
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
"""
#Check if Item Exists
"""
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
"""
>>>>>>> e40abd0 (lab2)
