from scapy.all import *
import sys
from operator import itemgetter
from constants import *
from packet_processing import *
from sheets import *
import json
from pprint import pprint

heats = []


# забрать фамилии перед стартом (приходит после блока Heats) [!]  [дорожка(0-9), имя фамилия, клуб нейм]
# очищать конечный результат после прихода данных о новом заплыве[!]
# забирать номер заплыва и описание (event descr)

# dummy = ['', '', '', '']


def send_to_spreadsheet(heat: Heat):
    print('-----------------------------------------------------------------')
    print(f'current heat: {Heat.current_heat}')
    data = heat.sort_by_rank()
    spd = []
    for info in data:
        spd.append(info.spreadsheet_data())
    print('sended data: ')
    pprint(spd)
    # spreadsheet_processing(spd)
    Heat.isSended = True


def handle_packet(pkt):
    try:
        if pkt.haslayer(Raw) is True:
            data = pkt.getlayer(Raw).load
            data = data.decode('utf-8')
            tmp = data.replace('\r', '').strip().split('\t')

            if ((HEAT_NUMBER in tmp) or (HEAT_LAPS in tmp)) or \
                    ((FIRST_NAME in tmp) or (LAST_NAME in tmp)) or \
                    (LANE_TIME in tmp and UNUSED_TRACK not in tmp):

                if HEAT_NUMBER in tmp:
                    Heat.current_heat = int(tmp[2])

                if len(heats) == 0:
                    heat = parsing_data(tmp)
                    heats.append(heat)
                    Heat.isSended = False
                else:
                    is_new_heat = True
                    for o in heats:
                        if int(o.heat_number) == Heat.current_heat:
                            parsing_data(tmp, o)
                            is_new_heat = False
                            break
                    if is_new_heat:
                        new_heat = parsing_data(tmp)
                        heats.append(new_heat)
                        Heat.isSended = False

                if not Heat.isSended:
                    for o in heats:
                        if int(o.heat_number) == Heat.current_heat:
                            if o.isFull():
                                send_to_spreadsheet(o)
                                break

    except (UnicodeError, AttributeError, KeyError) as err:
        # print("Some do wrong...")
        # print(err)
        pass


def start_sniffing():
    port = sys.argv[2]

    # dport = 26
    bpf = 'udp and udp dst port 26'

    print("[*] Start sniffing...")
    # print("Sniff all packet from 26 port and UDP proto")
    # print(bpf is None)
    # if bpf is not None:
    sniff(filter=bpf, prn=handle_packet, store=0)
    # sniff(filter=bpf, prn=handle_packet)
    print("[*] Stop sniffing")


if __name__ == '__main__':
    start_sniffing()
