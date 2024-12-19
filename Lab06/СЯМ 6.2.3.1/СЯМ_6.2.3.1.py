A = int(input("vvedite A: "))
B = int(input("vvedite B: "))
if A >= B:
    print("false: A < B.")
else:
    sum = 0
    for number in range(A, B + 1):
        sum += number
    print("summa", A, "do", B, sum)
