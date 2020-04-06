def in_minuts(seconds):
    seconds = seconds / 10000
    h = seconds // (60 * 60)
    m = (seconds - h * 60 * 60) // 60
    s = seconds - (h * 60 * 60) - (m * 60)
    return show_time(m, s)


def show_time(m, s):
    tmp = str(s).split('.')
    sec = tmp[0]
    mils = tmp[1][0:2]
    if s < 10:
        f = '{:.0f}:0{}.{}'.format(m, sec, mils)
    else:
        f = '{:.0f}:{}.{}'.format(m, sec, mils)

    return f

