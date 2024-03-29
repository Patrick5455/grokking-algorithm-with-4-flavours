# Given two non-empty arrays of integers, write a function that determines whether the second
# array is a subsequence of the first on.
# A subsequence of an array is  a set of numbers that
# aren't necessarily adjacent in the array, but they are in the same order as they appear in the
# array.
# For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4] and so
# do the numbers [2, 4].
# Note that a single number in an array and the array itself are both
# valid subsequences of the array.

def is_valid_subsequence_solution(array, sequence) -> bool:
    seq_idx = 0
    for num in array:
        if num == sequence[seq_idx]:
            seq_idx += 1
        if len(sequence) == seq_idx:
            return True
    return False
