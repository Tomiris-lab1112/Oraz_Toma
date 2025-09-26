#Boolean Values
"""
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False
"""

"""
a = 200
b = 33
if b > a:
  print("b is greater than a")  #if если условие будет True
else:
  print("b is not greater than a")  #else если условие будет False
"""

#Evaluate Values and Variables
"""
print(bool("Hello"))
print(bool(15))
"""

"""
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
"""

#Most Values are True
"""
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])   #Значение True
"""

#Some Values are False
"""
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})   #Значение False
"""

"""
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))    #False_len 0_False
"""

#Functions can Return a Boolean
"""
def myFunction() :
  return True
print(myFunction())    #Функции, возвращающие логическое значение
"""

"""
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")   #Будет yes
"""

"""  #isinstance
x = 200
print(isinstance(x, int))   #Определяет это истенное число или нет (True or False)
"""