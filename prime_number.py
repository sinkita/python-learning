import math

def check_prime(n):
    if n == 2:
        print("Prime")
    elif n % 2 != 0: #checking it should not an even no.
        prime_flag = True
        for i in range(2, math.sqrt(n) + 1):
            if n % i == 0:
                prime_flag = False
                break
        if prime_flag == True:
            print("Prime")
        else:
            print("Not Prime")
    else:
        print("Not Prime")

check_prime(9)

    