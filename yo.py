# print from 1 to 100
# if number is divisble by 3 -- fizz
# if number is divisble by 5 -- buzz
# if divisible by both -- fizzbuzz

# 2
# fizz
# 3


def fizzbuzz(start_num, stop_num):
	print('_________________')
	for number in range(start_num, stop_num + 1):
		if number % 3 == 0 and number % 5 == 0:
			print("fizzbuzz")
		elif number % 3 == 0:
			print("fizz")
		elif number % 5 == 0:
			print("buzz")
		else:
			print(number) 


fizzbuzz(1,300)