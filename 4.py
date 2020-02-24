# coding: utf-8
lg = 0
for i in range (1, 1000):
    # print(f"I {i}")
    for j in range (1, 1000):
        # print(f"J {j}")
        product = i * j
        slen = len(str(product))
        s1 = str(product)[:slen//2]
        s2 = str(product)[slen//2:]
        if s1[::-1] == s2:
            if product > lg:
                lg = product
            print(s1, s2)
print(lg)

                
