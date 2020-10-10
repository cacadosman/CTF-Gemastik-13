## Judul Soal
Feel The Rush

## Deskripsi Soal
i can feel it, yeah i can feel it. can you ?<br>
i am feeling the encrypted flag is :<br>
227d7e2c31792f45750e2e4c5b207470497e6f397b600662787a162f436e50091d623f5509741a23525a731568654e503d2f3757323a13040c204d69<br>
Author : 0x124f13

## Penjelasan Singkat Soal
Soal ini dibuat menggunakan bahasa pemrograman Rust.
Tahap awal yaitu dibentuk suatu list object seed dengan 3 byte yang di-random dan byte lainnya telah di-hardcode.
Setelah itu input teks pada stdin di-xor dengan random.randrange yang dimana sistem random telah di set seed nya.
Setelah itu hasilnya di-xor dengan indeks karakter pada string.

Penyelesaian soal hanya membalik proses yang telah dijelaskan.

## Catatan Deploy Soal
- Soal tidak perlu di-deploy
- Peserta diberikan binary `feel_the_rush` pada folder `peserta`

## Catatan Panitia
- file `flag` dan `source code` dari binary terdapat pada folder `panitia`


## Catatan Solver
Solver soal terdapat pada binary rust bernama `solver` pada folder `solver` . Tinggal run