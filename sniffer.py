from scapy.all import *
from operator import itemgetter
from constants import *
from packet_processing import *
from sheets import *

# 1) +
# отбросить знаки после запятой (не округляется) [готово]
# отсортировать по рангу (rank) [готово]

# 2) ?
# разделять данные на заплывы (Heat) [готово]
# сделать пул процессов и передавать им данные, возможно использовать очередь [хз, вроде и так норм]

heats = []


def send_to_spreadsheet(heat: Heat):
    print('heats: {}'.format(heats))
    print("sorting...")
    data = heat.sort_by_rank()
    spd = []
    for info in data:
        spd.append(info.spreadsheet_data())
    print("send to google sheet")
    print('sended data: {}'.format(spd))
    spreadsheet_processing(spd)
    Heat.isSended = True
    # proc = multiprocessing.Process(target=spreadsheet_processing, args=(sorted_infos,))
    # daemon = threading.Thread(target=spreadsheet_processing, args=(sorted_infos,))
    # daemon.setDaemon(True)
    # daemon.start()
    # proc.daemon = True
    # proc.start()


def handle_packet(pkt):
    try:
        if pkt.haslayer('UDP') is True:
            udp = pkt['UDP']
            if pkt.haslayer(Raw) is True:
                data = udp.getlayer(Raw).load
                data = data.decode('utf-8')
                data = data.replace('\r', '')
                data = data.strip()
                tmp = data.split('\t')
                """
                HEAT = 'Heat'
                HEAT_NUMBER = 'HeatNumber'
                HEAT_NAME = 'HeatName'
                HEAT_LAPS = 'Laps'
                
                self.heat_number = heat_number
                self.heat_name = heat_name
                self.laps = laps
                self.infos = infos
                """
                # check that data have necessary heat/competitor/track
                if ((HEAT in tmp) and ((HEAT_NUMBER in tmp) or (HEAT_NAME in tmp) or (HEAT_LAPS in tmp))) or \
                        ((COMPETITOR in tmp) and ((FIRST_NAME in tmp) or (LAST_NAME in tmp))) or \
                        (LANE_TIME in tmp and UNUSED_TRACK not in tmp and LAP in tmp):

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

                    # print(heats)
                    if not Heat.isSended:
                        for o in heats:
                            if int(o.heat_number) == Heat.current_heat:
                                if o.isFull():
                                    send_to_spreadsheet(o)
                                    break

    except (UnicodeError, KeyError) as err:
        print("Some do wrong...")
        print(err)
        pass


def start_sniffing():
    dport = 26
    bpf = 'udp and udp dst port 26'

    print("[*] Start sniffing...")
    print("Sniff all packet from 26 port and UDP proto")
    # print(bpf is None)
    # if bpf is not None:
    sniff(filter=bpf, prn=handle_packet)
    # sniff(filter=bpf, prn=handle_packet)
    print("[*] Stop sniffing")


if __name__ == '__main__':
    start_sniffing()
