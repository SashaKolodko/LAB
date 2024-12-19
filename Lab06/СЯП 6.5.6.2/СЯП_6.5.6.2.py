import math
def power(a, n):
    if n == 0:
        return 1
    
    else:
        return a * power(a, n - 1)
a = int(input("vvedite a: "))
n = int(input("vvedite n: "))
r = math.pow(a, n)
print(a,"v stepeni",n,"ravno",r)
