// a function to read from stdin and return vec consisting of each line as string

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
    // find first digit in a string
    let first = str.chars().find(|c| c.is_digit(10)).unwrap();
    let last = str.chars().rfind(|c| c.is_digit(10)).unwrap();
    format!("{first}{last}").parse::<u32>().unwrap()
}

// add test for find_calibration_value under test module

#[cfg(test)]
mod test {
    use super::*;
    #[test]
    fn test_find_calibration_value() {
        assert_eq!(find_calibration_value(&String::from("1abc2")), 12);
        assert_eq!(find_calibration_value(&String::from("pqr3stu8vwx")), 38);
        assert_eq!(find_calibration_value(&String::from("treb7uchet")), 77);
    }
}

fn main() {
    let ans: u32 = read_stdin().iter().map(|x| find_calibration_value(x)).sum();
    println!("{}", ans);
}
