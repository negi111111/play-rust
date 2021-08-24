// fn main() {
//     println!("Hello, world!");
// }


pub fn add(x:i32, y:i32) -> i32{
    return x + y;
}

#[test]
//　パニックを発生させるテス
#[should_panic]
fn test_add(){
    assert_eq!(add(1,2), 3);

}