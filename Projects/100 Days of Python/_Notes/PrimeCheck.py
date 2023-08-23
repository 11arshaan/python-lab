import math

n=int(input("Check this number: "))

def prime_check(number):
    isPrime = True
    for x in range (2, number):
        if (number%x) == 0:
            isPrime = False
    if isPrime:
        print("Is Prime")
    else:
        print("Not Prime")


prime_check(number=n)