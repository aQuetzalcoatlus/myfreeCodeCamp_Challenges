""" 
Given an array of integers from 1 to `n`, inclusive, return an array of all the missing integers between 1 and `n` (where `n` is the largest number in the given array).
    - The given array may be unsorted and may contain duplicates.
    - The returned array should be in ascending order.
    - If no integers are missing, return an empty array.
"""

def fill_numbers(number1, number2):
    if number2 > number1:
        start_number = number1
        end_number = number2
    else:
        start_number = number2
        end_number = number1

    return list(range(start_number+1, end_number))

def find_missing_numbers(given_list: list):
    unique_list = list(set(given_list))
    sorted_list = sorted(unique_list)

    missing_numbers: list = []

    for i, val in enumerate(sorted_list[:-1]):
        num1 = sorted_list[i]
        num2 = sorted_list[i+1]

        if num2 != (num1 + 1):
            missing_numbers.append(fill_numbers(num1, num2))

    missing_numbers_list = [item for row in missing_numbers for item in row]

    return missing_numbers_list

if __name__ == "__main__":
    test_arr = [1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4]

    print(find_missing_numbers(test_arr))