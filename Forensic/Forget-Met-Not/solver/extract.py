from scapy.all import *
from base64 import b64decode

pcap = rdpcap('log.pcap')
pkts = {}

for p in pcap:
    if p[ICMP].type == 0:
        _id   = p[ICMP].id
        _seq  = p[ICMP].seq
        _data = p[ICMP].load

        section = pkts.get(_id, dict())
        if not section:
            pkts[_id] = section

        data = b64decode(_data[7:])
        section[_seq] = Ether(data)

packets = []
for key, val in pkts.iteritems():
    for k,v in val.iteritems():
        packets.append(v)

packets = PacketList(packets)
wrpcap('http.pcap', packets)
