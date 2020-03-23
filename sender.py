from scapy.all import *
import time
import io


def first():
    cfn = "Competitor\t2\tFirstName\tДарья"
    cln = "Competitor	2	LastName	Безбокова"
    lt = "Time	2	LaneTime	783044	Rank	5	Lap	2	Points	0.00"

    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cfn), count=1)
    time.sleep(10)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cln), count=1)
    time.sleep(10)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=lt), count=1)


def first_fast():
    cfn = "Competitor\t2\tFirstName\tДарья"
    cln = "Competitor	2	LastName	Безбокова"
    lt = "Time	2	LaneTime	783044	Rank	5	Lap	2	Points	0.00"

    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cfn), count=1)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cln), count=1)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=lt), count=1)


def second():
    cfn = "Competitor	3	FirstName	Алина"
    cln = "Competitor	3	LastName	Фам"
    lt = "Time	3	LaneTime	771329	Rank	3	Lap	2	Points	0.00"

    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cfn), count=1)
    time.sleep(10)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cln), count=1)
    time.sleep(10)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=lt), count=1)


def second_fast():
    cfn = "Competitor	3	FirstName	Алина"
    cln = "Competitor	3	LastName	Фам"
    lt = "Time	3	LaneTime	771329	Rank	3	Lap	2	Points	0.00"

    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cfn), count=1)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cln), count=1)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=lt), count=1)


def third():
    cfn = "Competitor	4	FirstName	Анастасия"
    cln = "Competitor	4	LastName	Ордина"
    lt = "Time	4	LaneTime	668408	Rank	1	Lap	2	Points	0.00"

    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cfn), count=1)
    time.sleep(10)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cln), count=1)
    time.sleep(10)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=lt), count=1)


def third_fast():
    cfn = "Competitor	4	FirstName	Анастасия"
    cln = "Competitor	4	LastName	Ордина"
    lt = "Time	4	LaneTime	668408	Rank	1	Lap	2	Points	0.00"

    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cfn), count=1)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cln), count=1)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=lt), count=1)


def four():
    cfn = "Competitor	5	FirstName	Валерия"
    cln = "Competitor	5	LastName	Старостина"
    lt = "Time	5	LaneTime	727810	Rank	2	Lap	2	Points	0.00"

    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cfn), count=1)
    time.sleep(10)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cln), count=1)
    time.sleep(10)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=lt), count=1)


def four_fast():
    cfn = "Competitor	5	FirstName	Валерия"
    cln = "Competitor	5	LastName	Старостина"
    lt = "Time	5	LaneTime	727810	Rank	2	Lap	2	Points	0.00"

    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cfn), count=1)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cln), count=1)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=lt), count=1)


def five():
    cfn = "Competitor	6	FirstName	Ксения"
    cln = "Competitor	6	LastName	Веселова"
    lt = "Time	6	LaneTime	778243	Rank	4	Lap	2	Points	0.00"

    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cfn), count=1)
    time.sleep(10)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cln), count=1)
    time.sleep(10)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=lt), count=1)


def five_fast():
    cfn = "Competitor	6	FirstName	Ксения"
    cln = "Competitor	6	LastName	Веселова"
    lt = "Time	6	LaneTime	778243	Rank	4	Lap	2	Points	0.00"

    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cfn), count=1)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cln), count=1)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=lt), count=1)


def broken_data():
    cfn = "Competitor	8	FirstName	"
    cln = "Competitor	8	LastName	"
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cfn), count=1)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cln), count=1)


def test_case_1():
    first()
    time.sleep(15)
    second()
    time.sleep(15)
    third()
    time.sleep(15)
    four()
    time.sleep(15)
    five()


def test_case_3():
    first_fast()
    second_fast()
    third_fast()
    four_fast()
    five_fast()


def test_case_2():
    cfn = "Competitor\t2\tFirstName\tДарья"
    cln = "Competitor	3	LastName	Безбокова"
    lt = "Time	4	LaneTime	783044	Rank	5	Lap	2	Points	0.00"

    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cfn), count=1)
    time.sleep(10)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=cln), count=1)
    time.sleep(10)
    send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=lt), count=1)


def global_test():
    # path = 'resources/kekw.txt'
    path = 'resources/raw_kekw'
    with io.open(path, encoding='utf-8') as file:
        for line in file:
            send(IP(dst="127.0.0.1") / UDP(dport=26, sport=1049) / Raw(load=line), count=1)
        # time.sleep(2)

# second_fast()
# test_case_1()
# test_case_2()
# test_case_3()
# broken_data()
global_test()
# 192.168.1.12:1049 > 192.168.1.255:26
