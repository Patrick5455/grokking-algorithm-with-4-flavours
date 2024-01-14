"""
Find the two integers in a non-empty array of distinct integers that sums up to the target_sum
"""


def two_number_sum_1(array, target_sum):
    array = set(array)
    array = list(array)
    for val in array:
        for num in range(len(array)):
            if val == array[num]:
                break
            if val + array[num] == target_sum:
                return [val, array[num]]
    return []


def two_number_sum_2(array, target_sum):
    sets = set(num for num in array)
    for num in sets:
        match_for_num = target_sum - num
        if match_for_num in sets and match_for_num != num:
            return [num, match_for_num]

    return []


if __name__ == '__main__':
    arr = [6, 7, 0, 1, 1, 6, 8, 9]
    result = two_number_sum_2(arr, 13)
    print("result=", result)


