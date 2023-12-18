use std::io;
use std::io::prelude::*;

use regex::Regex;

fn read_stdin() -> Vec<String> {
    let stdin = io::stdin();
    let mut lines = Vec::new();
    for line in stdin.lock().lines() {
        lines.push(line.unwrap());
    }
    lines
}

#[derive(Clone, Copy, PartialEq, Debug)]
struct Combination {
    red: u32,
    green: u32,
    blue: u32,
}

#[derive(PartialEq, Debug)]
struct Game {
    id: u32,
    sets: Vec<Combination>,
}

fn is_possible(comb: Combination) -> bool {
    comb.red <= 12 && comb.green <= 13 && comb.blue <= 14
}

fn parse_game_str(s: &str) -> u32 {
    let re = Regex::new(r"Game\s(?P<id>\d+)").unwrap();
    re.captures(s)
        .and_then(|captures| captures.name("id"))
        .and_then(|m| m.as_str().parse::<u32>().ok())
        .unwrap_or_default()
}

fn parse_set_str(s: &str) -> Combination {
    let re = Regex::new(r"(?P<count>\d+)\s(red)").unwrap();
    let red = re
        .captures(s)
        .and_then(|captures| captures.name("count"))
        .and_then(|m| m.as_str().parse::<u32>().ok())
        .unwrap_or_default();
    let re = Regex::new(r"(?P<count>\d+)\s(green)").unwrap();
    let green = re
        .captures(s)
        .and_then(|captures| captures.name("count"))
        .and_then(|m| m.as_str().parse::<u32>().ok())
        .unwrap_or_default();
    let re = Regex::new(r"(?P<count>\d+)\s(blue)").unwrap();
    let blue = re
        .captures(s)
        .and_then(|captures| captures.name("count"))
        .and_then(|m| m.as_str().parse::<u32>().ok())
        .unwrap_or_default();
    return Combination { red, green, blue };
}

fn parse(line: &str) -> Game {
    let splitted: Vec<&str> = line.split(":").collect();
    let (game_str, sets_str) = (splitted[0].trim(), splitted[1].trim());

    let game_id = parse_game_str(game_str);

    let splitted: Vec<&str> = sets_str.split("; ").collect();
    let sets = splitted.iter().map(|x| parse_set_str(x)).collect();
    Game {
        id: game_id,
        sets: sets,
    }
}

fn calc_max(game: &Game) -> Combination {
    let mut max = Combination {
        red: 0,
        green: 0,
        blue: 0,
    };
    for set in &game.sets {
        if set.red > max.red {
            max.red = set.red;
        }
        if set.green > max.green {
            max.green = set.green;
        }
        if set.blue > max.blue {
            max.blue = set.blue;
        }
    }
    max
}

#[cfg(test)]
mod test {
    use super::*;
    #[test]
    fn test_parse() {
        assert_eq!(
            parse("Game 2: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"),
            Game {
                id: 2,
                sets: vec![
                    Combination {
                        red: 4,
                        green: 0,
                        blue: 3
                    },
                    Combination {
                        red: 1,
                        green: 2,
                        blue: 6
                    },
                    Combination {
                        red: 0,
                        green: 2,
                        blue: 0
                    },
                ],
            }
        );
    }
}

fn main() {
    let ans: u32 = read_stdin()
        .iter()
        .map(|x| {
            let parsed = parse(x);
            let max = calc_max(&parsed);
            max.red * max.green * max.blue
        })
        .sum();
    println!("{}", ans);
}
