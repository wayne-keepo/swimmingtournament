from classes import *
from constants import *
from pprint import pprint

from time_converter import in_minuts

smas = ['Heat	HeatNumber	1',
        'Heat	HeatName	Заплыв 1',
        'Heat	Description	',
        'Heat	StartTime	438000000',
        'Heat	DistanceM	100',
        'Heat	SpeedMS	0.00',
        'Heat	Laps	2']

for s in smas:
    tmp = s.replace('\r', '')
    tmp = tmp.split('\t')
    print('mas: {} len: {}'.format(tmp, len(tmp)))


class B(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def print(self):
        return self.name


class A(object):
    l: list

    def __init__(self, inf: list, name: str):
        self.inf = inf
        self.name = name

    def add_to_inf(self, data):
        self.inf.append(data)

    def print(self):
        return 'name: {}\ninf: {}'.format(self.name, self.inf)


b1 = B('b1')
b2 = B('b2')
b3 = B('b3')
b4 = B('b4')


# bm1 = [b1.print(), b2.print()]
# bm2 = [b3.print(), b4.print()]
#
# a1 = A([b1.print(), b2.print()], 'a1')
# a2 = A(bm1, 'a2')
#
# print(a1.print())
# print(a2.print())
#
# a1.add_to_inf(b3)
#
# print(a1.print())
# print(a2.print())
#
#
# kek = [1,3,4,5]
# kk = '{}'.format(kek)
#
# print(kk)


class Heat(object):
    current_heat: int

    def __init__(self, heat_number=-1, heat_name='', laps=-1, infos=None):
        self.heat_number = heat_number
        self.heat_name = heat_name
        self.laps = laps
        self.infos = infos

    def add_info(self, info: B):
        if self.infos is None:
            self.infos = []
            self.infos.append(info)
        else:
            self.infos.append(info)

    @staticmethod
    def get_current_heat():
        return Heat.current_heat

    @staticmethod
    def set_current_heat(heat: int):
        Heat.current_heat = heat

    def __repr__(self):
        return 'heat_number: {}, heat_name: {}, laps: {}, infos: {}'. \
            format(self.heat_number, self.heat_name, self.laps, self.infos)


l = [['1', '2', 'Михаил Васильков', '0:51.07'], ['2', '1', 'Андрей Настин', '0:51.68']]
print('mas: {} len: {}'.format(l, len(l)))

dummy = ['', '', '', '']

for item in range(len(l), 10):
    l.append(dummy)

print('mas: {} len: {}'.format(l, len(l)))
"""
    Sniff packets and return a list of packets.

    Args:
        count: number of packets to capture. 0 means infinity.
        store: whether to store sniffed packets or discard them
        prn: function to apply to each packet. If something is returned, it
             is displayed.
             --Ex: prn = lambda x: x.summary()
        session: a session = a flow decoder used to handle stream of packets.
                 e.g: IPSession (to defragment on-the-flow) or NetflowSession
        filter: BPF filter to apply.
        lfilter: Python function applied to each packet to determine if
                 further action may be done.
                 --Ex: lfilter = lambda x: x.haslayer(Padding)
        offline: PCAP file (or list of PCAP files) to read packets from,
                 instead of sniffing them
        timeout: stop sniffing after a given time (default: None).
        L2socket: use the provided L2socket (default: use conf.L2listen).
        opened_socket: provide an object (or a list of objects) ready to use
                      .recv() on.
        stop_filter: Python function applied to each packet to determine if
                     we have to stop the capture after this packet.
                     --Ex: stop_filter = lambda x: x.haslayer(TCP)
        iface: interface or list of interfaces (default: None for sniffing
               on all interfaces).
        monitor: use monitor mode. May not be available on all OS
        started_callback: called as soon as the sniffer starts sniffing
                          (default: None).

    The iface, offline and opened_socket parameters can be either an
    element, a list of elements, or a dict object mapping an element to a
    label (see examples below).

    Examples: synchronous
      >>> sniff(filter="arp")
      >>> sniff(filter="tcp",
      ...       session=IPSession,  # defragment on-the-flow
      ...       prn=lambda x: x.summary())
      >>> sniff(lfilter=lambda pkt: ARP in pkt)
      >>> sniff(iface="eth0", prn=Packet.summary)
      >>> sniff(iface=["eth0", "mon0"],
      ...       prn=lambda pkt: "%s: %s" % (pkt.sniffed_on,
      ...                                   pkt.summary()))
      >>> sniff(iface={"eth0": "Ethernet", "mon0": "Wifi"},
      ...       prn=lambda pkt: "%s: %s" % (pkt.sniffed_on,
      ...                                   pkt.summary()))

    Examples: asynchronous
      >>> t = AsyncSniffer(iface="enp0s3")
      >>> t.start()
      >>> time.sleep(1)
      >>> print("nice weather today")
      >>> t.stop()
    """
