from scapy.all import *
import re
import os
import codecs
from time_converter import in_minuts
from constants import *
from classes import *


packets = rdpcap('resources/test.pcapng')
print(len(packets))
print(len(packets.sessions()))

# print(packets[13].show())
i = 0
# for packet in packets:
#     # str = packet.payload
#     print(i)
#     i = i + 1
#     if packet.hasLa is not None:
#         print(packet.getlayer(Raw))
#
#     # if packet.getlayer(scapy.layers) is not None:
#     #     # s = str(packet.getlayer(Raw).load, 'utf-8')
#     #     # print(s)
#     #     print(packet.getlayer(Raw))
s = packets.sessions()
kekw_file = codecs.open("resources/raw_kekw", "wb")

competitors = []
tracks = []
infos = []
for key, value in s.items():
    # print(i)
    # print(key)
    # print(value)
    i = i + 1
    if ':26' in key:
        print(key)
        for v in value:
            # print(v)
            try:
                s = v['UDP'].getlayer(Raw).load
                # s = s.decode('utf-8')
                # s = s.replace('\r', '')
                # s = s.strip()
                # if LANE_TIME in s and UNUSED_TRACK not in s and LAP in s:
                #     s = s.split('\t')
                #     print(len(s))
                #     print(s)
                # if (COMPETITOR in s) and ((FIRST_NAME in s) or (LAST_NAME in s)):
                #     s = s.split('\t')
                #     print(len(s))
                #     print(s)



                kekw_file.write(s)
            except AttributeError:
                kekw_file.close()
                pass
kekw_file.close()