// use iteration::binary_search_with_iteration;
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
    let position = binary_search_with_recursion(student_records, item);
    println!("position of {item} is {position}")
}
