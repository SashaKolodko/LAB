a = input("vvedite szislo: ")
s = list(map(int, a.split()))
r = [num for num in s if num % 2 == 0 and num != 0]
if r:  
    max = max(r)
    print("naubolshie zislo:", max)
else:
    print("nety.")
