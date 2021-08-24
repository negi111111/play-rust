use clap::{App, Arg};

fn main() {
    let matches = App::new("my rpn program")
        .version("1.0.0")
        .author("your name")
        .about("super awesome sample rpn calculator")
        .arg(
            Arg::new("verbose")
                .about("sets the level of verbosity")
                .short('v') // char to use for the flag
                .long("verbose")
                .required(false),
        )
        .get_matches(); // 実行時に指定されたコマンドライン引数と照合して
                        // マッチ句で取り出す
    match matches.value_of("formula_file") {
        Some(file) => println!("file specified: {}", file),
        None => println!("no file specified"),
    }
    let verbose = matches.is_present("verbose");
    println!("is verbosity specified: {}", verbose);
}

// % cargo run -- -h                                                                                                 (git)-[master]
//     Finished dev [unoptimized + debuginfo] target(s) in 0.01s
//      Running `target/debug/samplecli -h`
// my rpn program 1.0.0
// your name
// super awesome sample rpn calculator

// USAGE:
//     samplecli [FLAGS]

// FLAGS:
//     -h, --help       Prints help information
//     -v, --verbose    sets the level of verbosity
//     -V, --version    Prints version information
