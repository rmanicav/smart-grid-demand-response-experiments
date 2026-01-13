from pcapfile import savefile
from pcapfile.protocols.linklayer import ethernet
from pcapfile.protocols.network import ip
from pcapfile.protocols.transport import tcp
import binascii
testcap = open('data/httptcp.pcap', 'rb')
capfile = savefile.load_savefile(testcap, verbose=True)
eth_frame = ethernet.Ethernet(capfile.packets[0].raw())
print(eth_frame)
ip_packet = ip.IP(binascii.unhexlify(eth_frame.payload))
print(ip_packet)
tcp_packet = tcp.TCP(binascii.unhexlify(eth_frame.payload))
print(tcp_packet)

print(tcp_packet.dst_port)
print(tcp_packet.src_port)
print(tcp_packet.seqnum)
print(tcp_packet.ack)
print(tcp_packet.payload)

#b'feff200001000000010000000800450000300f414000800691eb91fea0ed41d0e4df0d2c005038affe130000000070022238c30c0000020405b401010402'