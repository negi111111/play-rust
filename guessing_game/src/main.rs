use rand::Rng;
use std::io;

fn main() {
    // println!("buess the number");
    // println!("please input your guess");
    // let mut guess = String::new();
    // //
    // io::stdin()
    //     .read_line(&mut guess)
    //     .expect("failed to read line");
    // println!("you guessed: {}", guess);
    println!("guess the number");
    // let secret_number = rand::thread_rng().gen_range(1, 101);
    let secret_number = rand::thread_rng().gen_range(1, 101);
    println!("the secret number is : {}", secret_number);
    println!("please input your guess");
    let mut guess = String::new();

    io::stdin().read_line(&mut guess).expect("failed the guess");
    println!("you guessed : {}", guess);
}
