use std::collections::HashMap;
use std::fmt::format;
use std::io;
use std::io::prelude::*;

fn read_stdin() -> Vec<String> {
    let stdin = io::stdin();
    let mut lines = Vec::new();
    for line in stdin.lock().lines() {
        lines.push(line.unwrap());
    }
    lines
}

fn find_calibration_value(str: &String) -> u32 {
    let map = HashMap::from([
        ("one", '1'),
        ("two", '2'),
        ("three", '3'),
        ("four", '4'),
        ("five", '5'),
        ("six", '6'),
        ("seven", '7'),
        ("eight", '8'),
        ("nine", '9'),
    ]);
    let mut first: char = '0';

    'outer1: for i in 0..str.len() {
        if str.chars().nth(i).unwrap().is_digit(10) {
            first = str.chars().nth(i).unwrap();
            break;
        } else {
            for (key, value) in map.iter() {
                if str[i..].starts_with(key) {
                    first = value.clone();
                    break 'outer1;
                }
            }
        };
    }
    let mut last: char = '0';
    'outer2: for i in (0..str.len()).rev() {
        if str.chars().nth(i).unwrap().is_digit(10) {
            last = str.chars().nth(i).unwrap();
            break;
        } else {
            for (key, value) in map.iter() {
                if str[i..].starts_with(key) {
                    last = value.clone();
                    break 'outer2;
                }
            }
        };
    }
    format!("{first}{last}").parse::<u32>().unwrap()
}

fn main() {
    let ans: u32 = read_stdin().iter().map(|x| find_calibration_value(x)).sum();
    println!("{}", ans);
}

#[cfg(test)]
mod test {
    use super::*;
    #[test]
    fn test_find_calibration_value() {
        assert_eq!(find_calibration_value(&String::from("abcone2threexyz")), 13);
        assert_eq!(find_calibration_value(&String::from("xtwone3four")), 24);
        assert_eq!(
            find_calibration_value(&String::from("4nineeightseven2")),
            42
        );
        assert_eq!(find_calibration_value(&String::from("zoneight234")), 14);
        assert_eq!(find_calibration_value(&String::from("7pqrstsixteen")), 76);
        assert_eq!(find_calibration_value(&String::from("oneight")), 18);
    }
}
