def recursive_max_num(arr: [int]) -> int:
    max_num = arr[0]
    return max_num_helper(arr, 0, max_num)


def max_num_helper(arr: [int], idx: int, curr_max_num: int) -> int:
    if len(arr) == idx:
        return curr_max_num
    next_num = arr[idx]
    if next_num > curr_max_num:
        curr_max_num = next_num
    idx += 1
    return max_num_helper(arr, idx, curr_max_num)


if __name__ == '__main__':
    arr = [45, 89, 19988, 980980, 0000, 45567, 100_000_000]
    max_num = recursive_max_num(arr)
    print(f'max number in {arr} is {max_num}')
