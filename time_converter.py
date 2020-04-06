def in_minuts(seconds):
    seconds = seconds / 10000
    h = seconds // (60 * 60)
    m = (seconds - h * 60 * 60) // 60
    s = seconds - (h * 60 * 60) - (m * 60)
    tmp = str(s).split('.')
    if s < 10:
        return '{:.0f}:0{}.{}'.format(m, tmp[0], tmp[1][0:2])
    else:
        return '{:.0f}:{}.{}'.format(m, tmp[0], tmp[1][0:2])