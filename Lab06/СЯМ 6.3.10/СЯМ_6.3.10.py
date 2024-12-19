a = input("vvedite stroky: ")
c = a[0]
s = c.upper()
for i in range(1, len(a)):
    if a[i-1] == " ":
        s = s + a[i-1]
        v = a[i]
        n = v.upper()
        s = s + n
    else:
        s = s + a[i]
print(s)
