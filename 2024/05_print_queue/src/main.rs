use std::{fs::File, io::Read, cmp::Ordering::{Less, Greater}};

fn read_file() -> String {
    let mut file = File::open("./data.txt").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    return contents;
}

struct Rule {
    x: i32,
    y: i32
}

fn format_data() -> (Vec<Rule>, Vec<Vec<i32>>) {
    let content = read_file().to_owned();
    if let [rules, manuals] = content.split("\n\n").collect::<Vec<&str>>().as_slice() {
        let rules: Vec<Rule> = rules
            .split_whitespace()
            .filter_map(
                |l| match l.split("|").collect::<Vec<&str>>().as_slice() {
                    [x, y] => Some(Rule { x: x.parse::<i32>().unwrap(), y: y.parse::<i32>().unwrap() }),
                    _ => None
                }
            ).collect();
        let manuals: Vec<Vec<i32>> = manuals
            .split_whitespace()
            .filter_map(|l| Some(l.split(",").map(|v| v.parse::<i32>().unwrap()).collect() ))
            .collect();
        return (rules, manuals);
    } else {
        panic!("Incorrectly formatted input data");
    }
}

fn sort_pages(pages: &Vec<i32>, rules: &Vec<Rule>) -> Vec<i32> {
    let mut pages = pages.clone();
    pages.sort_by(|a, b| {
        let rule = rules.iter().find(|r| r.x == *a && r.y == *b || r.x == *b && r.y == *a);
        if let Some(r) = rule {
            return if r.x == *a { Less } else { Greater };
        } else {
            return (a - b).cmp(a);
        }
    });
    return pages;
}

fn main() {
    let (rules, manuals) = format_data();
    let mut page_sum = 0;
    let mut incorrectly_ordered_sum = 0;
    for pages in manuals {
        let correct_order = sort_pages(&pages, &rules);
        let middle_index = pages.len() / 2;

        if pages == correct_order {
            page_sum += pages[middle_index];
        } else {
            incorrectly_ordered_sum += correct_order[middle_index];
        }
    }
    // Part 1
    println!("Middle pages sum: {}", page_sum);
    assert_eq!(page_sum, 5948);

    // Part 2
    println!("Incorrectly ordered middle pages sum: {}", incorrectly_ordered_sum);
    assert_eq!(incorrectly_ordered_sum, 3062);
}
