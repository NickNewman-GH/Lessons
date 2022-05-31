"""Lambda
a = lambda x, y, z: x+y**2+z**3
b = [(a,b,c) for a, b, c in zip(range(15), range(15, 0, -1), range(15))]
for t in b:
    print(a(*t))
"""

"""Lambda vs def
from time import perf_counter

def cube(y):
    return y*y*y
 
lambda_cube = lambda y: y*y*y

start = perf_counter()
for i in range(int(10e5)): cube(999)
end = perf_counter()
print(f'{end - start:f}')

start = perf_counter()
for i in range(int(10e5)): lambda_cube(999)
end = perf_counter()
print(f'{end - start:f}')

start = perf_counter()
for i in range(int(10e5)): 999**3
end = perf_counter()
print(f'{end - start:f}')
"""

"""List of lambdas
tables = [lambda x=x: x*10 for x in range(1, 11)]
 
for table in tables:
    print(table())
"""

"""Writing our own max func with lambda
Max = lambda a, b : a if(a > b) else b
 
print(Max(10, 20))
"""

"""Find second largest element in every list
List = [[2,3,4,5],[1, 4, 16, 64],[3, 6, 9, 12]]

sortLists = lambda x: (sorted(i) for i in x)
print(list(sortLists(List)))
secondLargestElement = lambda x, fun : [y[-2] for y in fun(x)]
res = secondLargestElement(List, sortLists)

print(res)
"""

"""Filter
ages = [13, 90, 17, 59, 21, 60, 5]
 
adults = list(filter(lambda age: age>18, ages))
 
print(adults)

arr = [5, 7, 22, 97, None, 62, 77, "23", 73, 61]
 
final_list = list(filter(lambda x: isinstance(x, int), arr))
print(final_list)
"""

"""Lambda with map
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(map(lambda x: x*2, li))
print(final_list)
"""