function fizzBuzz(num){
	/**var num = prompt('Please enter a number: ');*/
	/** checks number is divisible by 3 and 5*/
	if (num%15 == false){

		msg = 'FizzBuzz';
	/** checks number is divisible by 5*/
	}else if (num%5 == false){

		msg = 'Buzz';
	/** checks number is divisible by 3*/
	}else if (num%3 == false){

		msg = 'Fizz';
	/**number not divisible by either 3 or 5*/
	}else{

		msg = num;
	}

	return msg;
}