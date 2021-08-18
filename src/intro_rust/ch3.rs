use std::io::Write;
fn main(){
    // let it = Iter {
    //     current: 0,
    //     max: 10,
    // };
    // for num in it {
    //     println!("{}", num);
    // }
    // let x = add(1,2);
    // println!("x={}", x);
    // let y = abs(-32);
    // println!("y={}", y);
    // let p = Person{
    //     name: String::from("taro"),
    //     age: 20,
    // };
    // p.say_name().say_age();
    // p.say_name();
    // p.say_age();

    // 関連関数の場合の呼び出し
    // インスタンスからメソッド呼び出しではばく、型から関数を呼ぶ形式
    // let p = Person::new("taro", 20);
    // p.say_name().say_age();
    let s = concat!("a", "b", 3);
    println!("s={}", s);
    // {:?}: フォーマット文字列のプレースホルダ
    let s = format!("{}-{:?}", s, ("D", 5));
    println!("s={}", s);
    let s = format!("{}{}", "abc", "def");
    println!("s={}", s);

    // ====
    print!("hello");
    // 改行有り
    println!("hello {}", "world");
    eprint!("hello {}", "error");
    eprintln!("hello");

    // バイト列書き込み用 vec宣言
    let mut w = Vec::new();
    write!(&mut w, "{}", "ABC");
    writeln!(&mut w, "is DEF");
    dbg!(w);
    // 出力
    //     [ch3.rs:44] w = [
    //     65,
    //     66,
    //     67,
    //     105,
    //     115,
    //     32,
    //     68,
    //     69,
    //     70,
    //     10,
    // ]
    println!("defined in file: {}", file!());
    println!("defined in line: {}", line!());
    println!("is test: {}", cfg!(unix));
    // コンパイル時の環境変数取得
    println!("CARGO_HOME: {}", env!("CARGO_HOME"));
    // 出力
    // defined in file: ch3.rs
    // defined in line: 60
    // is test: true
    // CARGO_HOME: /home/tanno/.cargo
    // ====

    println!("// ====");
    let mut p = HappyPerson{
        name: "takeshi".to_string(),
        state: Emotion::Happy,
    };
    println!("{}", p.get_happy());
}

// 構造体====
enum Emotion{
    Anger,
    Happy,
}
trait Emotional {
    fn get_happy(&mut self)-> String;
    fn get_anger(&mut self) -> String;
    fn tell_state(&self) -> String;
}

struct HappyPerson {
    name: String,
    state: Emotion,
}

impl Emotional for HappyPerson {
    fn get_anger(&mut self) -> String {
        unimplemented!()
    }
    fn get_happy(&mut self) -> String {
        format!("{} is always happy", self.name)
    }
    fn tell_state(&self) -> String {
        todo!()
    }
}

struct Iter {
    current: usize,
    max: usize,
}

struct Person {
    name: String,
    age: u32,
}


// 構造体にメソッドを impl で追加
impl Person {
    fn say_name(&self) -> &Self{
        print!("Hello, my name is {}", self.name);
        // 自分自身を末尾に定義してメソッドチェーン化
        self
    }
    fn say_age(&self) -> &Self{
        print!("I am {} years old", self.age);
        self
    }
}

// 関連関数
impl Person {
    fn new(name: &str, age: u32) -> Person {
        Person {
            name: String::from(name),
            age: age,
        }
    }
}


// return 書かないの？？？
// 関数内の最後に、セミコロン無しで記述された値を戻り値として扱うルール
// 処理途中は return 置いて早期終了するもOK
fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn abs(number: i32) -> i32 {
    if number < 0 {
        return -number;
    }
    // キモい
    // return 書いてもいいのかな？
    // number <-こう書いてもいいみたい
    return number
}

// 構造体にメソッドを紐付ける
// データとそれに関連する振る舞いをあわせてカプセル化できる
impl Iterator for Iter {
    type Item = usize;
    fn next(&mut self) -> Option<usize>{
        self.current += 1;
        if self.current -1 < self.max {
            Some(self.current -1)
        } else {
            None
        }
    }
}
