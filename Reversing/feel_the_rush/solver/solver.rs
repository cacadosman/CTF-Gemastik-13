extern crate rand;


use rand::prelude::*;
use std::fs::File;
use std::{
    io::{prelude::*},
};
use std::convert::TryInto;
use std::fmt::Write as FmtWrite;

fn main() -> std::io::Result<()> {
	let encrypted_flag = "\"}~,1y/Eu\x0e.L[ tpI~o9{`\x06bxz\x16/CnP\t\x1db?U\tt\x1a#RZs\x15heNP=/7W2:\x13\x04\x0c Mi";
	let enc_flag_vec: Vec<char> = encrypted_flag.chars().collect();
	let mut res_1 = String::new();
	
	for (i, _x) in enc_flag_vec.iter().enumerate(){
		res_1.push(((enc_flag_vec[i] as u8) ^ (i as u8)) as char);
	}


	for i in 0x00..0x40{
		for j in 0x00..0x50{
			for k in 0x00..0x60{
				let seed = [i, j, k, 1, 114, 49, 112, 220, 88, 112, 86, 148, 181, 194, 152, 209, 130, 196, 10, 59, 49, 189, 29, 228, 103, 12, 99, 230, 152, 170, 106, 33];
				
				println!("{} {} {}", i, j, k);
				let mut rng: StdRng = SeedableRng::from_seed(seed);
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