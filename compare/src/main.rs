// https://doc.rust-jp.rs/book-ja/ch02-00-guessing-game-tutorial.html
use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
    println!("guess the number");
    let secret_number = rand::thread_rng().gen_range(1, 101);
    println!("the secret number is: {}", secret_number);
    loop {
        println!("Please input your guess");
        let mut guess = String::new();
        io::stdin()
            .read_line(&mut guess)
            .expect("failed to the guess");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("you guessed: {}", guess);
        match guess.cmp(&secret_number) {
            Ordering::Less => println!("too small"),
            Ordering::Greater => println!("too big"),
            Ordering::Equal => {
                println!("you win");
                break;
            }
        }
    }
}
