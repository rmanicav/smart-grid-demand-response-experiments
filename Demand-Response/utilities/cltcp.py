# tcp.py -- example of building and sending a raw TCP packet
# Copyright (C) 2020  Nikita Karamov  <nick@karamoff.dev>
#
# With code from Scapy (changes documented below) 
# Copyright (C) 2019  Philippe Biondi <phil@secdev.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import array
from os import sep
import socket
import struct
import pandas as pd
import numpy as np
import csv 

# This part of code was adapted from the Scapy project:
# https://github.com/secdev/scapy/blob/467431faf8389f745d2c16370baf6dafc5751731/scapy/utils.py#L368-L381
#
# Changes made:
# - removed use of checksum_endian_transform function
# - restructured code without modifying it
# - renamed variables
# - added type hints
def chksum(packet: bytes) -> int:
    if len(packet) % 2 != 0:
        packet += b'\0'

    res = sum(array.array("H", packet))
    res = (res >> 16) + (res & 0xffff)
    res += res >> 16

    return (~res) & 0xffff


class TCPPacket:
    def __init__(self,
                 src_host:  str,
                 src_port:  int,
                 dst_host:  str,
                 dst_port:  int,
                 flags:     int = 0):
        self.src_host = src_host
        self.src_port = src_port
        self.dst_host = dst_host
        self.dst_port = dst_port
        self.flags = flags

    def build(self) -> bytes:
        packet = struct.pack(
            '!HHIIBBHHH',
            self.src_port,  # Source Port
            self.dst_port,  # Destination Port
            0,              # Sequence Number
            0,              # Acknoledgement Number
            5 << 4,         # Data Offset
            self.flags,     # Flags
            8192,           # Window
            0,              # Checksum (initial value)
            0               # Urgent pointer
        )

        pseudo_hdr = struct.pack(
            '!4s4sHH',
            socket.inet_aton(self.src_host),    # Source Address
            socket.inet_aton(self.dst_host),    # Destination Address
            socket.IPPROTO_TCP,                 # PTCL
            len(packet)                         # TCP Length
        )

        checksum = chksum(pseudo_hdr + packet)

        packet = packet[:16] + struct.pack('H', checksum) + packet[18:]

        return packet


if __name__ == '__main__':
    # default parameters
    dst = '192.168.10.17'
    src = '192.168.10.17'
    src_port = '20'
    dst_port = '666'
    flags ='0b000101001'
    
    #data segment
    int_1_L =1
    int_1_L1 =10
    real_4_B =0.4

    # field nameas
    fields = ['src', 'src_port', 'dst', 'dst_port','flag'] 

    #hard code data for packets
    pktlist = []
    pktlist.append(TCPPacket(src,src_port,dst,dst_port,0b000101001))
    pktlist.append(TCPPacket(src,src_port,dst,dst_port,0b000101000))
    pktlist.append(TCPPacket(src,src_port,dst,dst_port,0b000101011))
    pktlist.append(TCPPacket(src,src_port,dst,dst_port,0b000101111))
    
    df = pd.DataFrame(pktlist)
    print(df)
         