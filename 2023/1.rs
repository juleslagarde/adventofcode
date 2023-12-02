use std::io::{self, BufRead};

const DIGITS: [&str; 9] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

fn match_str(a: &str, b: &str) -> bool {
    a.starts_with(b) || b.starts_with(a)
}

fn get_digit(i: usize, line: &str) -> Option<u8> {
    match line.chars().nth(i) {
        Some('1'..='9') => line.chars().nth(i).unwrap().to_digit(10).map(|d| d as u8),
        _ => {
            #[cfg(step2)]
            {
                DIGITS.iter().enumerate().find_map(|(j, digit)| {
                    if match_str(&line[i..], digit) {
                        Some((j + 1) as u8)
                    } else {
                        None
                    }
                })
            }
            #[cfg(not(step2))]
            None
        }
    }
}

fn main() {
    let stdin = io::stdin();
    let mut buffer = String::new();

    let mut sum: u32 = 0;
    while stdin.lock().read_line(&mut buffer).unwrap() > 0 {
        let size = buffer.trim_end().len();
        let first = (0..size)
            .find_map(|i| get_digit(i, &buffer))
            .unwrap_or(0);

        let last = (0..size)
            .rev()
            .find_map(|i| get_digit(i, &buffer))
            .unwrap_or(0);

        sum += (first as u32)*10+(last as u32);

        buffer.clear();
    }
    println!("sum : {}", sum);
}
