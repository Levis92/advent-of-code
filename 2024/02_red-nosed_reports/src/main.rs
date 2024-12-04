use std::{fs::File, io::Read};

fn read_file() -> String {
    let mut file = File::open("./data.txt").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    return contents;
}

fn parse_number(str: &str) -> i32 {
    return str.parse::<i32>().unwrap();
}

fn is_same_direction(diff: &[i32]) -> bool {
    return diff.iter().all(|&i| i.is_negative()) || diff.iter().all(|&i| i.is_positive());
}

fn is_in_range(diff: &[i32]) -> bool {
    return diff.iter().all(|&i| (1..=3).contains(&i.abs()));
}

fn is_safe(diff: &[i32]) -> bool {
    return is_same_direction(diff) && is_in_range(diff);
}

fn calculate_differences(levels: &Vec<i32>) -> Vec<i32> {
    return levels.windows(2).map(|pair| pair[1] - pair[0]).collect();
}

fn main() {
    let contents = read_file();
    let mut safe_count = 0;
    let mut dampened_safe_count = 0;
    for report in contents.lines() {
        let levels: Vec<i32> = report.split_whitespace().map(parse_number).collect();
        let diff: Vec<i32> = calculate_differences(&levels);
        if is_safe(&diff) {
            safe_count += 1;
        } else {
            for index in 0..levels.len() {
                let mut dampened_levels = levels.clone();
                dampened_levels.remove(index);
                let dampened_diff = calculate_differences(&dampened_levels);
                if is_safe(&dampened_diff) {
                    dampened_safe_count += 1;
                    break;
                }
            }
        }

        
    }
    // Part 1
    println!("Safe count: {}", safe_count);
    assert_eq!(safe_count, 218);

    // Part 2
    println!("Dampened safe count: {}", safe_count + dampened_safe_count);
    assert_eq!(safe_count + dampened_safe_count, 290);
}
