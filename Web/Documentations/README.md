## Judul Soal
Documentations

## Deskripsi Soal
> Nothing special. Just a plain documentation page. For security reason, I decided to block the internet access <br>Author: コト

## Hint Soal
- The flag is located at `current directory`

---

## Penjelasan Singkat Soal
Soal ini berisikan sebuah web service berupa laman `dokumentasi python` yang dijalankan menggunakan Flask sebagai `base` servernya. <br><br>
Sebagaimana tertera pada `source code` yang diberikan, webservice hanya akan memberikan isi dari `__doc__` sehingga peserta perlu menggunakan pendekatan `Blind SSTI`.<br>

Karena beberapa limitasi karakter, kita perlu melakukan pendekatan lain yang salah satunya memanfaatkan `Exception` dari `IndexError` untuk mengetahui karakter manakah yang terdapat pada substring.<br>

Dalam hal ini, `Exception` dapat kita identifikasi ketika server memberikan response berupa `500 Internal server error`. Sedangkan untuk karakter yang benar, kita akan mendapatkan response berupa `__doc__` dari `int`.

Selebihnya, kita dapat menemukan `os module` dengan melakukan traversing sedemikian sehingga kita memperoleh response berisikan dokumentasi `OS routines for NT or Posix`.

Perlu diketahui, karena adanya `dns-redirection` & `character restriction`, proses `reverse shell` ke `domain-name` atau `public ip` menjadi sulit untuk dilakukan.

## Catatan Deploy Soal
- Folder deploy soal di server terdapat pada folder `server`
- Ubah port yang diinginkan untuk service soal pada file `docker-compose.yml`
- run `docker-compose build`
- Lalu tinggal `docker-compose up -d`

## Catatan Solver
Solver soal terdapat pada script python2 bernama `sv.py` pada folder `solver` . Tinggal mengganti HOST dan PORT nya.<br>

Berikut merupakan cuplikan dari hasil pengeksekusian script pada `localhost`:

```bash
$ time python2 sv.py

main.py requirements.txt run.sh static templates zzzz_fl4g_uwu 

gemastik13.i_th0ught_it_w4s_s3cure_en0ugh_f3bd301.

python2 sv2.py  4.09s user 0.45s system 9% cpu 46.670 total

```

Adanya constraint `blind`, infrastruktur server diusahakan dapat berjalan dengan baik pada trafik request yang tinggi