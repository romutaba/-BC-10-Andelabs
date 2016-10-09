# A Function that identifies Data Types

def data_type(n):
	#data type String check
	if (type(n) == type("")):	
		msg = len(n)			#returns the string's length
	#data type Boolean check	
	elif (type(n) == type(True)):
		msg = n    				#returns the boolean value
	#data type integer check
	elif (type(n) == type(3)):
		#checks if integer input is less than 100	
		if (n < 100):
			msg = "less than 100"
		#checks if integer input is equal to 100	
		elif (n == 100):
			msg = "equal to 100"
		#checks if integer input is more than 100	
		else:
			msg = "more than 100"
	#data type list check		
	elif (type(n) == type([])):
		#checks if list length is more than or equal to 3
		if (len(n) >= 3):
			msg = n[2]
		#checks if list length is less than 3	
		else:
			msg = None
	#no data type check		
	else:
		msg = "no value"
		
	return msg

print (data_type(''))
