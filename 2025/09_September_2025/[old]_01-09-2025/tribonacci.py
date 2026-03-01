""" 
The Tribonacci sequence is a series of numbers where each number is the sum of the three preceding ones. When starting with 0, 0 and 1, the first 10 numbers in the sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44.

Given an array containing the first three numbers of a Tribonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.

    Your function should handle sequences of any length greater than or equal to zero.
    If the length is zero, return an empty array.
    Note that the starting numbers are part of the sequence.

 """

def tribonacci_sequence(start_sequence: list, length_sequence: int) -> list:
    if length_sequence == 0:
        return []
    elif length_sequence <= len(start_sequence):
        return start_sequence[:length_sequence]
    else:
        new_sequence = start_sequence
        while len(start_sequence) < length_sequence:
            new_sequence.append(sum(new_sequence[-3:]))
        
        return new_sequence


length = 20
input_array = [0, 0, 1]

print(tribonacci_sequence([21, 32, 43], 1))