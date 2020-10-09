#!/bin/bash

python2 extract.py;
tshark -r http.pcap -Y data -Tfields -e data | xxd -r -p > ssl.log
tshark -r http.pcap -o "tls.keylog_file:ssl.log" --export-object http,files
tshark -r http.pcap -o "tls.keylog_file:ssl.log" -Y http.request.method | grep -oP '\d{0,4}x\d{0,4}' > dimension
tshark -r http.pcap -o "tls.keylog_file:ssl.log" -Y http.request.method | grep -oP '\d{0,4},\d{0,4}' | tr ',' ' ' > offset
python2 concate.py
