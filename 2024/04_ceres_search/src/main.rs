use std::{fs::File, io::Read, ops::Range};

fn read_file() -> String {
    let mut file = File::open("./data.txt").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    return contents;
}

fn format_data() -> Vec<Vec<String>> {
    let contents = read_file().to_owned();
    let mut letters: Vec<Vec<String>> = Vec::new();
    for line in contents.lines() {
        let row: Vec<String> = line.split("").filter_map(|char| match char {
            "" => None,
            _ => Some(char.to_string())
        }).collect();
        letters.push(row);
    }
    return letters;
}

fn get_word<'a>(
    word_range: &Range<usize>,
    letters: &'a Vec<Vec<String>>,
    row_index: usize,
    col_index: usize,
    row_mod: isize,
    col_mod: isize
) -> Vec<&'a String> {
    return word_range
        .clone()
        .filter_map(
            move |i| {
                let row_index = (row_index as isize + (row_mod * i as isize)) as usize;
                let col_index = (col_index as isize + (col_mod * i as isize)) as usize;
                return Some(&letters[row_index][col_index]);
            }
        ).collect::<Vec<&String>>();
}

fn main() {
    let letters = format_data();

    // Part 1
    let word = Vec::from(["X", "M", "A", "S"]);
    let word_range = 0..word.len();
    let mut word_count = 0;
    for (row_index, row) in letters.iter().enumerate() {
        for (col_index, letter) in row.iter().enumerate() {
            if *letter != word[0] {
                continue;
            }

            let space_right = col_index <= row.len() - word.len();
            let space_left = col_index >= word.len() - 1;
            let space_down = row_index <= letters.len() - word.len();
            let space_up = row_index >= word.len() - 1;

            let mut is_target_word = |found_word: Vec<&String>| {
                if word == found_word {
                    word_count += 1;
                }
            };

            let modifiers = [
                (space_right, 0, 1),
                (space_left, 0, -1),
                (space_down, 1, 0),
                (space_up, -1, 0),
                (space_right && space_down, 1, 1),
                (space_right && space_up, -1, 1),
                (space_left && space_down, 1, -1),
                (space_left && space_up, -1, -1)
            ];

            for (has_space, row_mod, col_mod) in modifiers {
                if has_space {
                    is_target_word(get_word(&word_range, &letters, row_index, col_index, row_mod, col_mod));
                }
            }
        }
    }
    println!("Count of {}: {}", word.join(""), word_count);
    assert_eq!(word_count, 2483);

    // Part 2
    let word = Vec::from(["M", "A", "S"]);
    let word_range = 0..word.len();
    let mut word_count = 0;
    for (row_index, row) in letters.iter().enumerate() {
        for (col_index, letter) in row.iter().enumerate() {
            if *letter != word[1] {
                continue;
            }

            let space_right = col_index < row.len() - 1;
            let space_left = col_index > 0;
            let space_down = row_index < letters.len() - 1;
            let space_up = row_index > 0;
            
            if space_up && space_down && space_left && space_right {
                let left_bottom_start = get_word(&word_range, &letters, row_index + 1, col_index - 1, -1, 1);
                let left_top_start = get_word(&word_range, &letters, row_index - 1, col_index - 1, 1, 1);

                let matches_one_direction = |mut found_word: Vec<&String>| {
                    if word == found_word {
                        return true;
                    } else {
                        found_word.reverse();
                        return word == found_word;
                    }
                };

                let left_bottom_matches = matches_one_direction(left_bottom_start);
                let left_top_matches = matches_one_direction(left_top_start);

                if left_bottom_matches && left_top_matches {
                    word_count += 1;
                }
            }
        }
    }
    println!("Count of X-MAS: {}", word_count);
    assert_eq!(word_count, 1925);
}
