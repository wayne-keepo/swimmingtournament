from scapy.all import *
import sys
import argparse
from constants import *
from packet_processing import *
import json
import io
import datetime

# отбросить знаки после запятой (не округляется)
# отсортировать по рангу (rank)

path_to_log = 'res/log_{}'.format(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))

IDX_KEY = 'index'
INF_KEY = 'info'
RANK_KEY = 'rank'
IS_FULL_KEY = 'isfull'
infos = []  # [..{'index': N, 'info': Info}..]
log = {'result': []}


def handle_packet(pkt):
    try:
        if pkt.haslayer('UDP'):
            udp = pkt['UDP']
            if pkt.haslayer(Raw) is True:
                data = udp.getlayer(Raw).load
                data = data.decode('utf-8')
                data = data.replace('\r', '')
                data = data.strip()
                if len(data.split('\t')) > 3:
                    if (LANE_TIME in data and UNUSED_TRACK not in data and LAP in data) or (
                            (COMPETITOR in data) and ((FIRST_NAME in data) or (LAST_NAME in data))):
                        # print("\t[LOG_HP] Infos len: {} | infos_data:{}".format(len(infos), infos))
                        idx = int(data.split('\t')[1])
                        check = False
                        if len(infos) > 0:
                            for obj in infos:
                                ii = int(obj.get(IDX_KEY))
                                if ii == idx:
                                    inf = parsing_data(data, obj.get(INF_KEY))
                                    obj[INF_KEY] = inf
                                    check = True
                                    break
                            if check is False:
                                inf = parsing_data(data)
                                kekw = {IDX_KEY: idx, INF_KEY: inf}
                                infos.append(kekw)

                        else:
                            inf = parsing_data(data)
                            kekw = {IDX_KEY: idx, INF_KEY: inf}
                            infos.append(kekw)

                        for o in infos:
                            o[RANK_KEY] = o[INF_KEY].rank
                            o[IS_FULL_KEY] = o[INF_KEY].is_full()
                            print("\t idx: {}\n\t {} isFull:{}".format(o[IDX_KEY], o[INF_KEY].to_string(),
                                                                       o[IS_FULL_KEY]))
                        print(len(log['result']))
                        print()
                        with io.open(path_to_log, 'w', encoding='utf-8') as file:
                            log['result'] = create_log_info(infos)
                            if len(log['result']) > 0:
                                file.write(str(log))

    except (UnicodeError, AttributeError):
        pass


def create_log_info(info):
    kek = []
    for o in info:
        if o[INF_KEY].is_full() is True:
            kek.append({IDX_KEY: o[IDX_KEY], INF_KEY: o[INF_KEY].to_string()})
    return kek


def start_sniffing():
    dport = 26
    bpf = 'udp and udp dst port {}'.format(dport)

    print("[*] Start sniffing...")
    # print(bpf is None)
    # if bpf is not None:
    sniff(prn=handle_packet)
    # sniff(filter=bpf, prn=handle_packet)
    print("[*] Stop sniffing")


if __name__ == '__main__':
    start_sniffing()
