a = input("vvedite szislo: ")
numbers = list(map(int, a.split()))
r = [num for num in numbers if num % 2 == 0 and num < 10 and num != 0]

if r:
    s = sorted(r)
    print("chetnue zisla bolshe 10:", s)
else:
    print("nety")
