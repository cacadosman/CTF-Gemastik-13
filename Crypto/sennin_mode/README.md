## Judul Soal
Sennin Mode

## Deskripsi Soal
Apakah kamu harus mempunyai kekuatan sennin mode untuk menyelesaikan soal ini ?<br>
Author : 0x124f13

## Penjelasan Singkat Soal
Soal ini awalnya melakukan generate seed untuk random dari value flag. Disini, sengaja range bit yang digunakan masih berada pada karakter flag yang diketahui yaitu "gemastik13{". Hanya saja terdapat tambahan 1 karakter dari flag sesudahnya, sehingga dibutuhkan brute-force 1 karakter untuk mendapatkan seed yang valid.

Cara kerjanya dalam hal ini peserta dapat memprediksi panjang dari flag yaitu 66, sehingga dapat menyelesaikan tahap untuk generasi seed. Setelah seed didapatkan, peserta tinggal melakukan solve pada persamaan linear yang didapatkan dari nilai x dan y dengan menggunakan tools SageMath.

## Catatan Deploy Soal
- Folder deploy soal di server terdapat pada folder `server`
- Soal dibuat dengan Python 3
- Ubah port yang diinginkan untuk service soal pada file `docker-compose.yml`
- run `docker-compose build`
- Lalu tinggal `docker-compose up -d`

## Catatan Solver
Note : Sebelumnya, harus menginstall `sage` versi terbaru.
Solver soal terdapat pada script python3 bernama `solver.py` dalam folder `solver` . Tinggal mengganti HOST dan PORT nya.