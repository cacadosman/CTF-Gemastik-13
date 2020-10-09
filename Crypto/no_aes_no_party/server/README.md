## Judul Soal
No AES No Party

## Deskripsi Soal
Loh e loh e ...
Author : 0x124f13

## Penjelasan Singkat Soal
Soal ini menggunakan enkripsi AES mode CFB untuk enkripsi key yang akan digunakan untuk enkripsi flag denagn AES mode ECB.<br>
Karena mode CFB pada library pycryptodome menggunakan variabel tambahan `segment_size` yang defaultnya adalah 8 bit (1 byte),<br>
Maka dibutuhkan enkripsi sebanyak (2^n) - 1 untuk recovery n byte dari key. Key yang butuh di-recovery sebanyak 8 bytes, sehingga diperlukan 255 kali enkripsi. Lalu peserta tinggal brute-force 2 byte terakhir dari adds_key , setelah itu tinggal dekripsi encrypted flag yang diberikan

## Catatan Deploy Soal
- Ubah port yang diinginkan untuk service soal pada file `docker-compose.yml`
- run `docker-compose build`
- Lalu tinggal `docker-compose up -d`

## Catatan Solver
Solver soal terdapat pada script python bernama `solver.py` . Tinggal mengganti HOST dan PORT nya.