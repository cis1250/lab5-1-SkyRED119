#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions

def validate_user_input() -> int:
    while (True):
        inpt = input('How many terms of the sequence should be printed? ')
        if (not inpt.isnumeric()):
            print("Please enter a positive integer.")
            continue
        if (int(inpt) <= 0):
            print("Please enter a positive integer.")
            continue
        return int(inpt)

def fib(lst: []) -> int:
    if len(lst) < 1:
        return 0
    elif len(lst) < 2:
        return 1
    else:
        return lst[-2] + lst[-1]

def print_sequence(num: int) -> None:
    myList = []
    for i in range(num):
        myList.append(fib(myList))
        print(myList[i])

    
def main():
    num = validate_user_input()
    print_sequence(num)

main()
