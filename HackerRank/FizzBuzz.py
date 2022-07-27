
# Complete the 'fizzBuzz' function below.
# The function accepts INTEGER n as parameter.

def fizzBuzz(n):
    # Write your code here
    for number in range(1, n+1):
        if (number % 3 == 0) and (number % 5 == 0):
            print("FizzBuzz")
        elif (number % 3 == 0):
            print("Fizz")
        elif (number % 5 ==0):
            print("Buzz")
        else:
            print(number)

fizzBuzz(15)