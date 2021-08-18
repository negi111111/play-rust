struct Dove;
struct Duck;

trait Tweet {
    fn tweet(&self);
    fn tweet_twice(&self) {
        self.tweet();
        self.tweet();
    }
    fn shout(&self) {
        println!("fdsfdsafsafads");
    }
}

impl Tweet for Dove {
    fn tweet(&self) {
        println!("cool!");
    }
}

impl Tweet for Duck {
    fn tweet(&self) {
        println!("quack!");
    }
}

// ジェネリクス
// 代入値によってコンパイル時に型の組み合わせだけ関数が作られ呼び出しが高速化される
fn make_tuple<T, S>(t: T, s: S) -> (T, S) {
    (t, s)
}

// fn calc_data(data: String) -> String {
//     println!("{}", data);
//     // これが値の参照を返却するもの
//     data
// }

fn calc_data(data: &String) -> String {
    println!("{}", data);
}

fn main(){

    // let mut important_data = "hello".to_string();
    let important_data = "hello".to_string();
    // 値の所有権を渡し、返してもらう
    // important_data = calc_data(important_data);
    // println!("{}", important_data)

    calc_data(&important_data);
    println!("{}", &important_data);

    // let t1 = make_tuple(1,2);
    // let dov = Dove{};
    // 静的ディスパッチ：コンパイル時に処理内容がわかっているため
    // dov.tweet();
    // dov.tweet_twice();
    // dov.shout();

    // let duck = Duck{};
    // 動的ディスパッチ：Appの振る舞いにより処理内容が変化する（コンパイル時にはわからん）
    // Vec<Box<>dyn Tweet> の部分が動的ディスパッチ
    // 画一的にポインタとして扱う
    // let bird_vec: Vec<Box<dyn Tweet>> = vec![Box::new(dov), Box::new(duck)];
    // for bird in bird_vec {
    //     bird.tweet();
    // }
}