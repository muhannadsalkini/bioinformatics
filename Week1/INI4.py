a = 4296
b = 8463
toplam = 0

for i in range(a, b + 1):
    if i % 2 == 1:
        toplam += i

print(toplam)
