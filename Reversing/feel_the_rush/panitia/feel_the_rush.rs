extern crate rand;


use rand::{Rng, SeedableRng, rngs::StdRng};
use rand::seq::SliceRandom;
use std::{
    io::{prelude::*},
};
use std::fmt::Write as FmtWrite;

fn main() -> std::io::Result<()> {
    let mut rng = rand::thread_rng();
    let seed = [rng.gen_range(0,0x3f),
    		rng.gen_range(0,0x4f),
    		rng.gen_range(0,0x5f),
    		1, 114, 49, 112, 220, 88, 112, 86, 148, 181, 194, 152, 209, 130, 196, 10, 59, 49, 189, 29, 228, 103, 12, 99, 230, 152, 170, 106, 33];
 
    let mut rng = StdRng::from_seed(seed);
    println!("Encrypt Yo FLAG : ");
    let mut line1 = String::new();

    std::io::stdin()
        .read_line(&mut line1)
        .ok()
        .expect("read error");


	let mut bruh = String::new();

	for kar in line1.bytes(){
		bruh.push((kar ^ rng.gen_range(0,127)) as char);
	}

	let mut brih = String::new();

	let mut iter_count = 0;
	for item in bruh.as_bytes(){
		brih.push((item ^ iter_count) as char);
		iter_count += 1;
	}

	let normal = brih.as_bytes();
	let after_shuffle: Vec<u8> = normal.choose_multiple(&mut rng, normal.len()).cloned().collect();	

	println!("Result : ");
	let mut finals = String::new();
	for b in after_shuffle { write!(finals, "{:02x}", b); }
	println!("{}", finals);
	
    Ok(())

}
