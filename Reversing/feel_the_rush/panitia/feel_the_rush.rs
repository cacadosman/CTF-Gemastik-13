extern crate rand;


use rand::prelude::*;
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
 
    let mut rng: StdRng = SeedableRng::from_seed(seed);
    
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

	let breh: Vec<char> = bruh.chars().collect();
	let mut brih = String::new();

	for (i, _x) in breh.iter().enumerate(){
		brih.push(((breh[i] as u8) ^ (i as u8)) as char);
	}

	let mut finals = String::new();
	println!("Result : ");
	for b in brih.as_bytes() { write!(finals, "{:02x}", b); }
	println!("{}", finals);
	
    Ok(())

}