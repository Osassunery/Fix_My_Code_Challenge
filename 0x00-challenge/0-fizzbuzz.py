#!/usr/bin/python3

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:  # Check for FizzBuzz first
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:  # Check for Fizz
            print("Fizz", end=" ")
        elif i % 5 == 0:  # Check for Buzz
            print("Buzz", end=" ")
        else:  # Print the number itself if not divisible by 3 or 5
            print(i, end=" ")

if __name__ == "__main__":
    fizzbuzz(50)
