for i in range(40,65,5):
    print(i)

print("  ")

for i in range(200,-5,-5):
    print(i,end=" ")

print(" ")

import random

k=[]

for i in range(30):
    k.append(random.randint(-10,10))

print("A lista elemei:")
print(k)

db=int(input("Hányasával írjam ki a számokat? "))

for i in range(0,len(k),db):
    print(k[i:i+db])

    # 4. feladat
print("\n4. feladat")
negativ = 0
nulla = 0

for szam in k:
    if szam < 0:
        negativ += 1
    elif szam == 0:
        nulla += 1

print("Negatív számok darabszáma:", negativ)
print("Nullák darabszáma:", nulla)

import random

d = []

for i in range(50):
    kocka1 = random.randint(1, 6)
    kocka2 = random.randint(1, 6)
    d.append((kocka1, kocka2))

for i in range(0, 50, 10):
    print(d[i:i+10])