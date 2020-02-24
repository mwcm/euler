# coding: utf-8
# solution = 4613732
total = 0
curr = 1
prev = 0
while curr < 4000000:
    curr = curr + prev
    prev = curr - prev
    print(curr)
    if curr % 2 == 0:
        total = total + curr
print(f'total {total}')
