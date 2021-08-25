// 素の実装
// fn main() {
//     let width = 30;
//     let height = 40;
//     let rect = (30, 40);

//     println!(
//         "the area ofthe rectangle is {} square pixels.",
//         area(rect) // area(width, height)
//     );
// }

// // fn area(width: u32, height: u32) -> u32 {
// //     width * height
// // }

// fn area(dimensions: (u32, u32)) -> u32 {
//     dimensions.0 * dimensions.1
// }

// // 構造体
// #[derive(Debug)]
// struct Rectangle {
//     width: u32,
//     height: u32,
// }

// fn main() {
//     let rect1 = Rectangle {
//         width: 30,
//         height: 40,
//     };
//     println!("{:#?}", rect1);
//     println!("the area of the rectangle {}", area(&rect1));
// }

// fn area(rectangle: &Rectangle) -> u32 {
//     rectangle.width * rectangle.height
// }
#[dirive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

// 構造体にメソッドを追加うすr
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30, height: 40,
    }
    // in
    let rect2 = Rectangle {
        width: 10, height: 30,
    }
    // out
    let rect3 = Rectangle {
        width: 300, height: 45,
    }
    println!("{:#?}", rect1.area());
    println!("{}", rect1.can_hold(&rect2));
    println!("{}", rect1.can_hold(&rect3));    
}
