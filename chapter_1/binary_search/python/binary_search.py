def binary_search_with_recursion(sorted_arr: list[str], item: str):
    low, high = 0, len(sorted_arr) - 1
    position = binary_search_with_recursion_helper(sorted_arr, item, low, high)
    print(f"final position {position}")
    return position


def binary_search_with_recursion_helper(sorted_arr: list[str], item: str,
                                        low: int = 0, high: int = 0):
    if low > high:
        return None
    mid = (low + high) // 2
    print(f'guess position = {mid}')
    guess = sorted_arr[mid]
    if guess > item:
        high = mid - 1
        return binary_search_with_recursion_helper(sorted_arr, item, low, high)
    elif guess < item:
        low = mid + 1
        return binary_search_with_recursion_helper(sorted_arr, item, low, high)
    else:
        return mid


def binary_search_with_iteration(sorted_arr: list[str], item: str):
    low, high = 0, len(sorted_arr) - 1
    while low <= high:
        mid = (low + high) // 2
        print(f'guess position = {mid}')
        guess = sorted_arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    arr = ["apple", "zebra", "monkey", "ball", "execute", "banana", "golang", "kotlin",
           "databricks", "scala", "k8s", "presto", "ffg"]
    search = "zebras"
    arr.sort()
    print(f'sorted array: {arr} with size of {len(arr)}')
    position_using_recursion = binary_search_with_recursion(arr, search)
    print(f"using recursion: position of item {search} is at {position_using_recursion} of array")
    # position_using_iteration = binary_search_with_iteration(arr, search)
    # print(f"using iteration: position of item {search} is at {position_using_iteration} of array")
