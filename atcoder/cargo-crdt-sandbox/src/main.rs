use crdts::{GCounter, CvRDT, CmRDT};


fn main() {
    println!("Hello, world!");
    let mut gc1 = GCounter::<u32>::new();
    let mut gc2 = GCounter::<u32>::new();
    gc1.apply(gc1.inc(1));
    gc2.apply(gc2.inc(2));
    gc1.merge(gc2.clone());
    println!("{}", gc1.read());
    println!("{}", gc2.read());
    gc2.merge(gc1.clone());
    println!("{}", gc2.read());
}
