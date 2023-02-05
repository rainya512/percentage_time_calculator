# import random
# import matplotlib.pyplot as plt


def fac_rec(n):
    if n <= 1:
        return 1
    return n * fac_rec(n - 1)


def fac(n):
    if n <= 1:
        return 1

    value = 1
    for i in range(n, 1, -1):
        value *= i
    return value


def npr(n, r):
    return fac(n) / fac_rec(n - r)


def ncr(n, r):
    return npr(n, r) / fac_rec(r)


def Same_nPr(n):
    p = 0
    q = 1
    for i in n:
        p += i
        q *= fac(i)
    return fac(p) / q


def Pow(n, r):
    return n**r


def nhr(n, r):
    return ncr(n + r - 1, r)


n = int(input())


'''
for i in range(n+1):
    print(ncr(n, i))


for i in range(n):
    a.append(int(input()))

print(Same_nPr(a))
'''


Tri_list = []
sum_list = []

for i in range(n+1):
    for j in range(n, i, -1):
        print(end="   ")

    sub_list = []
    for j in range(i+1):
        sub_list.append(ncr(i, j))
        print("%5d" % ncr(i, j), end="  ")

    Tri_list.append(sub_list)
    print("\n")


for i in range(len(Tri_list)):
    for j in range(len(Tri_list), i, -1):
        print(end="    ")

    for j in range(len(Tri_list[i])):
        if Tri_list[i][j] % 2 == 0:
            Tri_list[i][j] = 0

        print("%5d" % Tri_list[i][j], end="   ")
    print("\n")


'''
for i in range(len(Tri_list)):
    sum = 0
    for j in range(len(Tri_list[i])):
        sum += Tri_list[i][j]
    sum_list.append(sum)
'''


"""
dice_list = []
X_list = [i for i in range(1, 7)]
Y_list = [0 for i in range(6)]

for i in range(a):
    Y_list[random.randint(0, 5)]+=1

plt.bar(X_list, Y_list)
plt.show()
"""
