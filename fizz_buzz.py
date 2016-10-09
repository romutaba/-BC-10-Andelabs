def fizz_buzz(num):
    #checks number is divisible by 3 and 5*
    if (num%15 == False):
        msg = 'FizzBuzz'
    #checks number is divisible by 5*   
    elif (num%5 == False):
        msg = 'Buzz'
    #checks number is divisible by 3 
    elif (num%3 == False):
        msg = 'Fizz'
    #number not divisible by either 3 or 5*
    else:
        msg = num
    return msg     
 