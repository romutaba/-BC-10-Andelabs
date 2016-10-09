from _ast import Num
prime_numbers = 0 # intitializing to Zero
Num = int(input("Enter Number to check: "))
def is_prime(x):
    if x >= 2: 
        for y in range(2,x):
            if not ( x % y ): 
                return False
    else:
        return False
    return True
for i in range(0, Num):
    if is_prime(i):
        prime_numbers += 1
        print (i)

print ("The Prime Numbers between 0 and "+ str(Num) +" is " + str(prime_numbers))

