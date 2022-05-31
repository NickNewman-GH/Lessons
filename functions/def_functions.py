"""Function syntax
def function_name(parameters):
    ""docstring""
    statement(s)
    return expression
"""

"""Function
def myFun():
    print('myFun text')

myFun()
"""

"""Function with arguments
def isZero(number):
    if number == 0:
        print('Yes')
    else:
        print('No')

isZero(0)
isZero(50)
"""

"""Function with default arguments
def printCoords(x, y = 0):
    print(f'x = {x}, y = {y}')

printCoords(5)
printCoords(5, 3)
"""

"""Keyword arguments
def printCoords(x, y):
    print(f'x = {x}, y = {y}')

printCoords(x = 2, y = 12)
printCoords(y = -5, x = 3)
"""

"""*args - non-keyword arguments
def sumOfNumbers(*numbers):
    sum_of_numbers = 0
    for num in numbers:
        sum_of_numbers += num
    print(sum_of_numbers)
    
sumOfNumbers(1,2,3,4,5,6,7,8)
"""

"""**kwargs - keyword arguments
def printKwargs(**keywordArgs):
    for key, value in keywordArgs.items():
        print(f'{key} = {value}')

printKwargs(left = 2, center = 3, right = 2)
"""

"""Args pos
def printArgs(text10, text11, *args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f'{key} = {value}')
    
printArgs('text1', 'text2', 'text3', 'text4', text1='text', text2='text', text3='text')

def printArgs(*args, text10, text11, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f'{key} = {value}')
    
printArgs('text1', 'text2', 'text3', 'text4', text10 = 'text', text11 = 'text', text1='text', text2='text', text3='text')
"""

"""Docstring
print('\n\n###########################\n\n'.join([print.__doc__, sum.__doc__, zip.__doc__]))

def isEven(number):
    '''Function to check if the number is even'''
    return True if number % 2 == 0 else False

print(f'\n###########################\n\n{isEven.__doc__}')
"""

"""Return
def pow(num, degree):
    return num**degree
 
print(pow(2, 5))
print(pow(-4, 3))
"""

"""Objects visibility in the function
def firstElementTo20(x):
    x[0] = 20

arr = [10, 11, 12, 13, 14, 15]
firstElementTo20(arr)
print(arr)

#############################

def arrOverride(x):
    x = [20, 30, 40]

arr = [10, 11, 12, 13, 14, 15]
arrOverride(arr)
print(arr)

#############################

def swap(x, y):
    x, y = y, x

x = 2
y = 3
swap(x, y)
print(x)
print(y)
"""

"""Function in function
def fun1():
    s = 'sometext'

    def fun2():
        print(s)
         
    fun2()
 
fun1()
"""

"""Yield - when we don't want to store the sequence in memory
def generator():
    for value in (5,6,7,8,9,10,11,12,13):
        yield value

for num in generator():
    print(num)
"""

"""Closures
def multiplier(n):
    '''multiplier(n) возвращает функцию, умножающую на n'''
    def mul(k):
        return n*k
    return mul
# того же эффекта можно добиться выражением
# multiplier = lambda n: lambda k: n*k
mul2 = multiplier(5)
print(mul2(4))
"""