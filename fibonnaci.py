
def fibonnaci(n):
	Fib_list = [] #create an empty list
	i = 1
	Fib_list.append(i) #insert 1 to the list
	Fib_list.append(i) #insert 1 to the list again
	while i <= n:  #checks that i is less or equal to the fibonnaci integer to check
		i = Fib_list[-1] + Fib_list[-2] #equates i to the sum of the last two digits in the list
		Fib_list.append(i) #inserts the new sum to the list
	else:
		Fib_list.remove(Fib_list[-1])
		for i in range (0, len(Fib_list)):
			print (Fib_list[i]) #prints result in series

print (fibonnaci(5))