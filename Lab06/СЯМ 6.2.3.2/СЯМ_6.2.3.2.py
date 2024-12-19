
n = int(input("vveditekolichestvo elementov: "))
sum = 0
count = 0
d = []
print("vvedite posledovatelnost:")
while count < n:
    number = int(input())
    d.append(number)
    count += 1
i = 0
while i < n and (d[i] % 2 == 0) * 1:  
    sum += d[i]
    i += 1
    
print("summa:", sum)
   


   

    


