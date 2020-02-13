import time
import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.25


def fib1(number):
    if number <= 1:
        return number
    else:
        return(fib1(number-1) + fib1(number-2))


def fib2(number):
    a, b = 0, 1
    for i in range(number):
        a, b = b, a+b
    return a


def fib3(number):
    v1, v2, v3 = 1, 1, 0
    for rec in bin(number)[3:]:
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec == '1':
            v1, v2, v3 = v1+v2, v1, v2
    return v2


number = []
runTime = []
output = []
runTimeTwo = []
runTimeThree = []

num = int(input("Number of element: "))
for i in range(0, num):
    nterms = int(input("How many sequence: "))
    number.append(nterms)
    starTime = time.time()
    for i in range(nterms):
        print(fib1(i))
    starTimeTwo = time.time()
    for i in range(nterms):
        print(fib2(i))

    starTimeThree = time.time()
    for i in range(nterms):
        print(fib3(i))

    runTime.append(time.time() - starTime)
    runTimeTwo.append(time.time() - starTimeTwo)
    runTimeThree.append(time.time() - starTimeThree)
print(number)
print(runTime)
print(runTimeTwo)
print(runTimeThree)

bars1 = runTime
bars2 = runTimeTwo
bars3 = runTimeThree

r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1, bars1, color='#7f6d5f', width=barWidth,
        edgecolor='white', label='recursive')
plt.bar(r2, bars2, color='#557f2d', width=barWidth,
        edgecolor='white', label='iteration')
plt.bar(r3, bars3, color='#2d7f5e', width=barWidth,
        edgecolor='white', label='fast')

plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], number)

plt.legend()
plt.show()
