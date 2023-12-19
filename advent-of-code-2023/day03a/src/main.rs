use std::io;
use std::io::prelude::*;

fn read_stdin() -> Vec<String> {
    let stdin = io::stdin();
    let mut lines = Vec::new();
    for line in stdin.lock().lines() {
        lines.push(line.unwrap() + ".");
    }
    lines.push(".".repeat(lines[lines.len() - 1].len()));
    lines.insert(0, ".".repeat(lines[0].len()));
    lines
}

fn main() {
    let map = read_stdin();
    let ans: u32 = map
        .iter()
        .enumerate()
        .map(|(i, line)| {
            if i == 0 || i == map.len() - 1 {
                return 0;
            }
            let mut nums: Vec<char> = Vec::new();
            let mut is_part = false;
            for (j, c) in line.chars().enumerate() {
                // if there are symbols in any 8 directions set is_part to true
                for x in -1..2 {
                    for y in -1..2 {
                        if x == 0 && y == 0 {
                            continue;
                        }
                        if map[(i as i32 + x) as usize][(j as i32 + y) as usize] != '.' {
                            is_part = true;
                        }
                    }
                }
                if !c.is_numeric() {
                    if nums.len() > 0 && is_part {
                        return nums.iter().collect::<String>().parse::<u32>().unwrap();
                    }
                    nums = Vec::new();
                    is_part = false;
                } else {
                    nums.push(c)
                }
            }
            0
        })
        .sum();
    println!("{}", ans);
}
