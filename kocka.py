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
