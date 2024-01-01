pub fn binary_search_with_recursion(mut sorted_arr: Vec<String>, item: &String) -> i32 {
    sorted_arr.sort();
    println!("sorted arr: {:?}", sorted_arr);
    let low: i32 = 0;
    let high: i32 = (sorted_arr.len() - 1) as i32;
    return binary_search_with_recursion_helper(sorted_arr, item, low, high);
}

fn binary_search_with_recursion_helper(
    sorted_arr: Vec<String>,
    item: &String,
    mut low: i32,
    mut high: i32,
) -> i32 {
    let mid: usize = ((low + high) / 2) as usize;
    println!("guessed position = {mid}");

    if item == &sorted_arr[mid] {
        return mid as i32;
    }

    if item > &sorted_arr[mid] {
        low = (mid) as i32 + 1;
        return binary_search_with_recursion_helper(sorted_arr, item, low, high);
    }

    if item < &sorted_arr[mid] {
        high = (mid) as i32 - 1;
        return binary_search_with_recursion_helper(sorted_arr, item, low, high);
    }

    return -1;
}
