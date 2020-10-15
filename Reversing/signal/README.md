## Judul Soal
Signal

## Deskripsi Soal
Sepertinya program ini memanggil fungsi dengan cara yang tidak biasa...<br>
Author : flammenwerfer

## Penjelasan Singkat Soal
Soal ini menggunakan bahasa pemrograman C. Program akan mengenkripsi string yang diberikan menjadi 50 byte ciphertext. Pemanggilan fungsi enkripsi pada program dilakukan dengan menggunakan fungsi `signal` dan `raise`. Enkripsi dilakukan per blok dengan besar 5 byte.

Dalam melakukan enkripsi, program akan membaca 5 byte dari `/dev/urandom` yang akan digunakan untuk menentukan index subtitusi dari ciphertext. Oleh karena itu, kita bisa merecover 5 byte random tersebut dengan memanfaatkan known plaintext flag. Lima karakter pertama dari flag ("gemas" dari `gemastik13{\w+}`) dienkripsi, kemudian dixor dengan index dari ciphertext untuk mendapatkan byte random tersebut.

Langkah selanjutnya yaitu dengan membalik operasi enkripsi pada blok berikutnya untuk mendapatkan plaintext.

## Catatan Deploy Soal
- Soal tidak perlu di-deploy
- Peserta diberikan binary `sig` dan enkripsi dari flag `flag` pada folder `peserta`

## Catatan Panitia
- file `flag.txt` dan `source code` dari binary terdapat pada folder `panitia`

## Catatan Solver
Solver soal terdapat script python bernama `solver.py` pada folder `solver` . Tinggal run


