import math
def calculate_mean(x, y):
    if (x > 0 and y > 0) or (x < 0 and y < 0):
        return math.sqrt(x * y)
    else:
        return (x + y) / 2
x = float(input("vvedite x: "))
y = float(input("vvedite y: "))
result = calculate_mean(x, y)
print("resultat:", result)

