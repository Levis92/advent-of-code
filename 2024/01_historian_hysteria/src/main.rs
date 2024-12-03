use std::{fs::File, io::Read};

use itertools::izip;

fn read_file() -> String {
    let mut file = File::open("./data.txt").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    return contents;
}

fn parse_number(str: &String) -> i32 {
    return str.parse::<i32>().unwrap();
}

fn main() {
    let contents = read_file();
    let mut left_column = Vec::<String>::new();
    let mut right_column = Vec::<String>::new();
    for line in contents.lines() {
        let mut line = line.split_whitespace();
        if let Some(left_val) = line.next() {
            left_column.push(left_val.to_string());
        }
        if let Some(right_val) = line.next() {
            right_column.push(right_val.to_string());
        }
    }
    left_column.sort();
    right_column.sort();

    // Part 1
    let mut sum = 0;
    for (left, right) in izip!(&left_column, &right_column) {
        let diff = (parse_number(left) - parse_number(right)).abs();
        sum += diff;
    }
    println!("Sum: {}", sum);
    assert_eq!(sum, 3714264);

    // Part 2
    let mut score = 0;
    for left in &left_column {
        let val = parse_number(left);
        score += val * right_column.iter().filter(|x| *x == left).count() as i32;
    }
    println!("Score: {}", score);
    assert_eq!(score, 18805872);
}
