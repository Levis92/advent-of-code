use std::{fs::File, io::Read};
use regex::Regex;

fn read_file() -> String {
    let mut file = File::open("./data.txt").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    return contents;
}

fn get_numbers(str: &str) -> Vec<i32> {
    let digit_re = Regex::new(r"\d*").unwrap();
    return digit_re.find_iter(str).filter_map(|d| d.as_str().parse::<i32>().ok()).collect();
}

fn mul(cmd: &str) -> i32 {
    let numbers: Vec<i32> = get_numbers(cmd);
    return numbers[0] * numbers[1];
}

fn get_matches<'a>(re: &Regex, str: &'a str) -> Vec<&'a str> {
    return re.find_iter(str).map(|i| i.as_str()).collect();
}

fn main() {
    let mul_re = Regex::new(r"mul\(\d*,\d*\)").unwrap();
    let do_re = Regex::new(r"do\(\)").unwrap();
    let dont_re = Regex::new(r"don't\(\)").unwrap();
    let cmd_exp = [do_re.as_str(), dont_re.as_str(), mul_re.as_str()].join("|");
    let cmd_re = Regex::new(&cmd_exp).unwrap();

    let mut mul_sum = 0;
    let mut cmd_sum = 0;
    let mut enabled = true;
    let contents = read_file();

    for line in contents.lines() {
        // Part 1
        let commands: Vec<&str> = get_matches(&mul_re, line);
        for cmd in commands {
            mul_sum += mul(&cmd);
        }
        // Part 2
        let commands: Vec<&str> = get_matches(&cmd_re, line);
        for cmd in commands {
            if enabled && mul_re.is_match(cmd) {
                cmd_sum += mul(&cmd);
            } else if do_re.is_match(cmd) {
                enabled = true;
            } else if dont_re.is_match(cmd) {
                enabled = false;
            }
        }
    }
    // Part1
    println!("Mul sum: {}", mul_sum);
    assert_eq!(mul_sum, 170068701);

    // Part2
    println!("Cmd sum: {}", cmd_sum);
    assert_eq!(cmd_sum, 78683433);
}
