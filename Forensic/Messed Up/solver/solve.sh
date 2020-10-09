#!/bin/bash
# Restore pcap order
reordercap messed-up.pcap ordered.pcap;
# Exfiltrate Http-only packet
tshark -r ordered.pcap -Y http -w http.pcap;
# Extract login data (contained email)
tshark -r http.pcap -Y "$(tshark -r http.pcap -Y 'frame.time_delta > 0.75' | awk '{print $1-5}' | xargs -Iz echo 'frame.number=='z' || ' | tr -d '\n' | rev | cut -c5- | rev)" -Tfields -e urlencoded-form.value > email;                                                                                                                                       
# Extract note data (contained ssti payload)
tshark -r http.pcap -Y "$(tshark -r http.pcap -Y 'frame.time_delta > 0.75' | awk '{print $1-1}' | xargs -Iz echo 'frame.number=='z' || ' | tr -d '\n' | rev | cut -c5- | rev)" -Tfields -e urlencoded-form.value > payload
python2 sv.py;
# Extract flag.zip
echo "UEsDBBQDAAAIAEeTRlFrhl3uRwAAAE4AAAAIAAAAZmxhZy50eHQFwUsKgDAMBcC9p2loV17mYTGWUhIhiT/EuzvTWBaPPii/WzL4LhnGxZOCcBVH2EPaEAlSBoMClSPYANQjoHxmk64r5vubflBLAQI/AxQDAAAIAEeTRlFrhl3uRwAAAE4AAAAIACQAAAAAAAAAIIDAgQAAAABmbGFnLnR4dAoAIAAAAAAAAQAYAAAP43/Tm9YBAA/jf9Ob1gEAjd8pDpzWAVBLBQYAAAAAAQABAFoAAABtAAAAAAA="| base64 -d > flag.zip;
unzip flag.zip;
cat flag.txt;