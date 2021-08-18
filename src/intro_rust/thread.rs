// TODO
// 共有メモリ方式による複数スレッドから１つのデータにアクセスする方法
// メッセージ
use std::thread;
fn main(){
    // クロージャーを受け取る
    // 宣言： |args|{body} 
    // 引数受け取らない：||{body}
    // thread::spawn(|| {
    //     // このままだとprintされる前にプログラムが終了する可能性あり
    //     println!("Hello, world!");
    // });
    // dbg!(handle.join());
    // let handle = thread::spawn(||{
    //     println!("Hello, world!");
    // });
    // dbg!(handle.join());
    let mut handles = Vec::new();
    
    for x in 0..10 {
        handles.push(thread::spawn(|| {
            println!("hello, : {}", x);
        }));

    }
    for handle in handles {
        let _ = handle.join();
    }
}