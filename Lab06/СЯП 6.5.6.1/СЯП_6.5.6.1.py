def gcd(a, b):
 
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    
    return (a * b) // gcd(a, b)
try:
    A = int(input("vvedite A: "))
    B = int(input("vvedite B: "))

    if A <= 0 or B <= 0:
        raise ValueError("zisla dolgnu > 0).")
    nod = gcd(A, B)
    nok = lcm(A, B)

    print("NOD", A, "i", B,":",nod)
    print("NOK", A, "i", B,":",nok)
except ValueError as e:
    print("oshibka:",e)

