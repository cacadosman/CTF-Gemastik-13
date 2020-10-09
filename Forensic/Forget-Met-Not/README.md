## Judul Soal
Forget-Me-Not

## Deskripsi Soal
>This little journey may be ended, but these memories will last forever<br>Author: コト

## Hint Soal
- It was just a glimpse of memory, but I remembered that I had ever learned about network tunneling before

---

## Penjelasan Penyelesaian Soal
Given a `xz compressed` file, contained packet-capture file named `log.pcap`.
<br><br>
Based on `static analysis`, we found several ICMP packet with different `Id` & `Sequence number`

```bash
$ tshark -r log.pcap | head
    1   0.000000 0.000000000   172.90.0.1 → 172.90.0.2   ICMP 141 Echo (ping) request  id=0x0009, seq=48/12288, ttl=64
    2   0.084440 0.084440000   172.90.0.2 → 172.90.0.1   ICMP 139 Echo (ping) reply    id=0x0009, seq=48/12288, ttl=64
    3   0.143215 0.058775000   172.90.0.1 → 172.90.0.2   ICMP 141 Echo (ping) request  id=0x000b, seq=5/1280, ttl=64
    4   0.179083 0.035868000   172.90.0.2 → 172.90.0.1   ICMP 2128 Echo (ping) reply    id=0x000b, seq=5/1280, ttl=64
    5   0.225552 0.046469000   172.90.0.1 → 172.90.0.2   ICMP 137 Echo (ping) request  id=0x0008, seq=109/27904, ttl=64
    6   0.253352 0.027800000   172.90.0.2 → 172.90.0.1   ICMP 139 Echo (ping) reply    id=0x0008, seq=109/27904, ttl=64
    7   0.305836 0.052484000   172.90.0.1 → 172.90.0.2   ICMP 137 Echo (ping) request  id=0x0003, seq=10/2560, ttl=64
    8   0.340737 0.034901000   172.90.0.2 → 172.90.0.1   ICMP 139 Echo (ping) reply    id=0x0003, seq=10/2560, ttl=64
    9   0.382688 0.041951000   172.90.0.1 → 172.90.0.2   ICMP 137 Echo (ping) request  id=0x0002, seq=89/22784, ttl=64
   10   0.473194 0.090506000   172.90.0.2 → 172.90.0.1   ICMP 2753 Echo (ping) reply    id=0x0002, seq=89/22784, ttl=64
```

We also found that there are difference response between `ICMP request` and `ICMP reply`

```bash
# Glimpse of ICMP Request
$ tshark -r log.pcap -Y 'icmp.type eq 8' -Tfields -e data | head -1 | xxd -r -p
Request: aHR0cHM6Ly9jdGYuZ2VtYXN0aWsuaWQvaW1hZ2VzL2ZsYWcuanBnL2Nyb3AvKDY2NywxMDQ4KS82
Njd4MTA0OA==

$ echo aHR0cHM6Ly9jdGYuZ2VtYXN0aWsuaWQvaW1hZ2VzL2ZsYWcuanBnL2Nyb3AvKDY2NywxMDQ4KS82Njd4MTA0OA== | base64 -d
https://ctf.gemastik.id/images/flag.jpg/crop/(667,1048)/667x1048

# Glimpse of ICMP Reply
$ tshark -r log.pcap -Y 'icmp.type eq 0' -Tfields -e data | head -1 | xxd -r -p
Reply: AkKsWgACAkI86w2mCABFAAA00rZAAEAGD1asWgABrFoAAtmKAbtFugKJXRl+04AQBPdY3gAAAQEI
ClTANjpE7uqr
```

According to the hint, we knew that there was a `network tunneling` scheme. Thus, we can assummed that the `ICMP tunneling` distinguish:

a. `request payload`, contained `URL/Endpoint`<br>
b. `reply payload`, contained tunneled `Ether/IP packet`<br>

Based on documentations, we found that:

```markdown
the identifier might be used like a port in TCP or UDP to identify a session, and the sequence number might be incremented on each echo request sent
```

That means, each `Id` and `Sequence number` has different kind of request `session`. Using scapy, then we re-construct each `session` and extract the `Ether/Ip packet` respectively.

```bash
$ python2 extract.py
          
$ tshark -r http.pcap | head
    1   0.000000 0.000000000   172.90.0.1 → 172.90.0.2   TCP 74 55654 → 443 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM=1 TSval=1421792592 TSecr=0 WS=128
    2  -0.087328 -0.087328000   172.90.0.2 → 172.90.0.1   TCP 74 443 → 55654 [SYN, ACK] Seq=0 Ack=1 Win=65160 Len=0 MSS=1460 SACK_PERM=1 TSval=1156417985 TSecr=1421792592 WS=128
    3  -0.097532 -0.010204000   172.90.0.1 → 172.90.0.2   TCP 66 55654 → 443 [ACK] Seq=1 Ack=1 Win=64256 Len=0 TSval=1421792592 TSecr=1156417985
    4   0.854538 0.952070000   172.90.0.1 → 172.90.0.2   TLSv1 583 Client Hello
    5   0.730184 -0.124354000   172.90.0.2 → 172.90.0.1   TCP 66 443 → 55654 [ACK] Seq=1 Ack=518 Win=64768 Len=0 TSval=1156418000 TSecr=1421792607
    6   0.755532 0.025348000   172.90.0.2 → 172.90.0.1   TLSv1.2 1539 Server Hello, Certificate, Server Key Exchange, Server Hello Done
    7   0.786620 0.031088000   172.90.0.1 → 172.90.0.2   TCP 66 55654 → 443 [ACK] Seq=518 Ack=1474 Win=64128 Len=0 TSval=1421792612 TSecr=1156418005
    8   0.269027 -0.517593000   172.90.0.1 → 172.90.0.2   TLSv1.2 159 Client Key Exchange, Change Cipher Spec, Encrypted Handshake Message
    9  -0.241270 -0.510297000   172.90.0.2 → 172.90.0.1   TCP 66 443 → 55654 [ACK] Seq=1474 Ack=611 Win=64768 Len=0 TSval=1156418007 TSecr=1421792614
   10  -0.082556 0.158714000   172.90.0.2 → 172.90.0.1   TLSv1.2 117 Change Cipher Spec, Encrypted Handshake Message
                    
```

Here, we found several `encrypted SSL packet` of `HTTP request`. Luckily, we also found `ssl.log` which contained `CLIENT_RANDOM` to decrypt the `SSL packet` directly.

After successfully decrypt the packet, we found severals pieces of `PNG image` from previous `HTTP request`

```bash
$ tshark -r http.pcap -Y data -Tfields -e data | xxd -r -p > ssl.log

$ tshark -r http.pcap -o "tls.keylog_file:ssl.log" --export-object http,files

$ file files/*  
files/667x1048:     PNG image data, 667 x 1048, 8-bit/color RGB, non-interlaced
files/667x1048(1):  PNG image data, 667 x 1048, 8-bit/color RGB, non-interlaced
files/667x1048(10): PNG image data, 667 x 1048, 8-bit/color RGB, non-interlaced
files/667x1048(11): PNG image data, 667 x 1048, 8-bit/color RGB, non-interlaced
files/667x1048(12): PNG image data, 667 x 1048, 8-bit/color RGB, non-interlaced
files/667x1048(13): PNG image data, 667 x 1048, 8-bit/color RGB, non-interlaced
files/667x1048(14): PNG image data, 667 x 1048, 8-bit/color RGB, non-interlaced
files/667x1048(15): PNG image data, 667 x 1048, 8-bit/color RGB, non-interlaced
files/667x1048(2):  PNG image data, 667 x 1048, 8-bit/color RGB, non-interlaced
files/667x1048(3):  PNG image data, 667 x 1048, 8-bit/color RGB, non-interlaced
files/667x1048(4):  PNG image data, 667 x 1048, 8-bit/color RGB, non-interlaced
files/667x1048(5):  PNG image data, 667 x 1048, 8-bit/color RGB, non-interlaced
files/667x1048(6):  PNG image data, 667 x 1048, 8-bit/color RGB, non-interlaced
files/667x1048(7):  PNG image data, 667 x 1048, 8-bit/color RGB, non-interlaced
files/667x1048(8):  PNG image data, 667 x 1048, 8-bit/color RGB, non-interlaced
files/667x1048(9):  PNG image data, 667 x 1048, 8-bit/color RGB, non-interlaced

```

Basically, we can directly see the character of `flag`. But for aesthetically purpose, we can also concate the `pieces of image` to get the original `flag.jpg`

```bash
$ python2 concate.py 
$ file flag.jpg 
flag.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 5336x2096, components 3
```