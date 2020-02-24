# coding: utf-8
# solution = 233168
aeiou = 0
for i in range(0, 1000):
    if (i % 3 == 0) or (i % 5 == 0):
        print(f'match {i}')
        aeiou += i
print(f'total: {aeiou}')
