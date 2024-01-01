use iteration::binary_search_with_iteration;
use recursion::binary_search_with_recursion;

pub mod iteration;
pub mod recursion;

fn main() {

    let mut student_records: Vec<String> = Vec::new();
    student_records.push(String::from("Patrick"));
    student_records.push(String::from("Omolade"));
    student_records.push(String::from("Oyin"));
    student_records.push(String::from("Funke"));
    let item = &String::from("Oyin");

    let position_with_recursion = binary_search_with_recursion(student_records.clone(), item);
    println!("using recursion: position of {item} is {position_with_recursion}");

    let position_with_iteration = binary_search_with_iteration(student_records.clone(), item);
    println!("using iteration: position of {item} is {position_with_iteration}")
}
