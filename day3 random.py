import math
x = int(input("Enter a random number: "))
factors = []
for i in range(1,11):
    if x % i == 0:
        factors.append(i)
print("The factors of {} are: {}".format(x, factors))