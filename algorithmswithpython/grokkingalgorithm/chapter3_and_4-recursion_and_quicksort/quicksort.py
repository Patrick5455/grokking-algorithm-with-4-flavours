def quicksort(arr: [int]) -> [int]:
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    larger = [ele for ele in arr if ele > pivot]
    smaller = [ele for ele in arr if ele < pivot]
    return quicksort(smaller) + [pivot] + quicksort(larger)


if __name__ == '__main__':
    arr_to_sort = [7, 89, 90, 35, 57, 12, 13, 32, 23, 34, 43, 42, 78, 45, 28, 9, 8]
    sorted_arr = quicksort(arr_to_sort)
    print(f'arr to sort = {arr_to_sort}')
    print(f'sorted arr = {sorted_arr}')
