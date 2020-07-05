#!/usr/bin/env python3


def get_input():
    """Prompt user for three numbers to test"""
    print("Input the three numbers you want to test, separated by spaces")
    nums = input()
    return nums


def convert_to_list(nums):
    """Convert the input from a string to a list of ints"""
    num_list = nums.split()
    num_list = map(lambda x: int(x), num_list)
    return num_list


def square_and_sort(num_list):
    """Square the numbers in the list and sort them by size"""
    num_list = list(map(lambda x: x ** 2, num_list))
    num_list.sort()
    return num_list


def compare_list(num_list):
    """See if a^2 + b^2 = c^2"""
    a2_plus_b2 = num_list[0] = num_list[1]
    c2 = num_list[-1]
    if a2_plus_b2 == c2:
        print("The numbers are a Pythagorean triple.")
    else:
        print("The numbers aren't a Pythagorean triple.")


def continue_or_not(keep_going):
    """See if user wants to test another set of numbers"""
    print("Would you like to test another set of numbers? (y or n)")
    keep_going = input().lower()
    return keep_going


def main():
    keep_going = "y"
    while keep_going == "y":
        nums = get_input()
        num_list = convert_to_list(nums)
        try:
            squared_nums = square_and_sort(num_list)
            compare_list(squared_nums)
        except:
            print("Error: invalid input.  Do you want to try again? (y or n)")
            keep_going = input().lower()
            continue
        keep_going = continue_or_not(keep_going)


if __name__ == "__main__":
    main()
