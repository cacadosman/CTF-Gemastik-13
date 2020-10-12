extern crate rand;


use rand::{Rng, SeedableRng, rngs::StdRng};
use rand::seq::SliceRandom;
use std::{
    io::{prelude::*},
};
use std::fmt::Write as FmtWrite;

fn main() -> std::io::Result<()> {
	let encrypted_flag = "\x0e+\x15t\\>\x14P\x16\x03\x00q\x13@\x08!bA`5\x11<eUFw2h<O#\n4'\x01l2\x06Z";
	let enc_flag_bytes = encrypted_flag.as_bytes();

	for i in 0x00..0x40{
		for j in 0x00..0x50{
			for k in 0x00..0x60{
				let seed = [i, j, k, 1, 114, 49, 112, 220, 88, 112, 86, 148, 181, 194, 152, 209, 130, 196, 10, 59, 49, 189, 29, 228, 103, 12, 99, 230, 152, 170, 106, 33];
				let mut rng = StdRng::from_seed(seed);
				println!("{} {} {}", i, j, k);
				
				for t in 0..39{
					rng.gen_range(0, 0x7f);
				}

				let before_shuffle = vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38];
				let after_shuffle: Vec<u8> = before_shuffle.choose_multiple(&mut rng, before_shuffle.len()).cloned().collect();
				let mut awal: [u8; 39] = [0; 39];

				for w in 0..39 {
                                       awal[after_shuffle[w as usize] as usize] = enc_flag_bytes[w as usize];
                                }				

				let mut rng = StdRng::from_seed(seed);
				let mut res_1 = String::new();

				for (i, _x) in awal.iter().enumerate(){
					res_1.push(((awal[i] as u8) ^ (i as u8)) as char);
				}

                                
                                let mut poss_flag = String::new();

                                for kar in res_1.bytes(){
                                        poss_flag.push((kar ^ rng.gen_range(0,127)) as char);
                                }

				if poss_flag.contains("gemastik13{"){
					println!("{}", poss_flag);
					std::process::exit(0x0100);
				}
			}	
		}
	}


    Ok(())

}
