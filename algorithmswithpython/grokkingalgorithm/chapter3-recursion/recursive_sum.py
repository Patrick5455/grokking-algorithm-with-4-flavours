def recursive_sum(arr: [int]) -> int:
    final_sum = recursive_sum_helper(arr, 0, 0)
    return final_sum

def recursive_sum_helper(arr, idx, arr_sum):
    if len(arr) == idx:
        return arr_sum
    arr_sum += arr[idx]
    idx += 1
    return recursive_sum_helper(arr, idx, arr_sum)


if __name__ == '__main__':
    sum = recursive_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"sum = {sum}")