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

fn get_horizontal_word<'a>(
    word_range: &Range<usize>,
    row: &'a Vec<String>,
    col_index: usize,
    col_mod: isize
) -> Vec<&'a String> {
    return word_range
        .clone()
        .filter_map(|i| Some(&row[(col_index as isize + (col_mod * i as isize)) as usize]))
        .collect::<Vec<&String>>()
}

fn get_vertical_word<'a>(
    word_range: &Range<usize>,
    letters: &'a Vec<Vec<String>>,
    row_index: usize,
    col_index: usize,
    row_mod: isize
) -> Vec<&'a String> {
    return word_range
        .clone()
        .filter_map(|i| Some(&letters[(row_index as isize + (row_mod * i as isize)) as usize][col_index]))
        .collect::<Vec<&String>>();
}

fn get_diagonal_word<'a>(
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

            let mut handle_horizontal = |col_mod: isize| {
                is_target_word(get_horizontal_word(&word_range, row, col_index, col_mod));
            };

            if space_right {
                handle_horizontal(1);
            }
            if space_left {
                handle_horizontal(-1);
            }

            let mut handle_vertical = |row_mod: isize| {
                is_target_word(get_vertical_word(&word_range, &letters, row_index, col_index, row_mod));
            };

            if space_down {
                handle_vertical(1);
            }
            if space_up {
                handle_vertical(-1);
            }

            let mut handle_diagonal = |row_mod: isize, col_mod: isize| {
                is_target_word(get_diagonal_word(&word_range, &letters, row_index, col_index, row_mod, col_mod));
            };

            if space_right && space_down {
                handle_diagonal(1, 1);
            }
            if space_right && space_up {
                handle_diagonal(-1, 1);
            }
            if space_left && space_down {
                handle_diagonal(1, -1);
            }
            if space_left && space_up {
                handle_diagonal(-1, -1);
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
                let left_bottom_start = get_diagonal_word(&word_range, &letters, row_index + 1, col_index - 1, -1, 1);
                let left_top_start = get_diagonal_word(&word_range, &letters, row_index - 1, col_index - 1, 1, 1);

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
