use binarysearch::iteration::binary_search_with_iteration;
use binarysearch::recursion::binary_search_with_recursion;


mod binarysearch;

fn main() {

    let mut student_records: Vec<String> = Vec::new();
    student_records.push(String::from("Patrick"));
    student_records.push(String::from("oke"));
    student_records.push(String::from("Oyin"));
    student_records.push(String::from("Funke"));
    let item = &String::from("Oyin");

    let position_with_recursion = binary_search_with_recursion(student_records.clone(), item);
    println!("using recursion: position of {item} is {position_with_recursion}");

    let position_with_iteration = binary_search_with_iteration(student_records.clone(), item);
    println!("using iteration: position of {item} is {position_with_iteration}")
}
