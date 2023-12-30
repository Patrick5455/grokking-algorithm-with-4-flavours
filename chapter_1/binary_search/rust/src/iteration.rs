pub fn binary_search_with_iteration(mut arr: Vec<String>, item: &String) -> i32 {
    arr.sort();
    let mut low = 0;
    let mut high = (arr.len()) as i32;

    while low <= high {
        let mid = ((low + high) / 2) as usize;
        println!("guessed position: {mid}");
        if item > &arr[mid] {
            low = (mid + 1) as i32;
        } else if item < &arr[mid] {
            high = (mid - 1) as i32;
        } else {
            return mid as i32;
        }
    }

    return -1;
}
