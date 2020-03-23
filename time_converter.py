def in_minuts(seconds):
    SEC_CONST = 10000
    seconds = seconds/SEC_CONST
    h = seconds // (60 * 60)
    m = (seconds - h * 60 * 60) // 60
    s = seconds - (h * 60 * 60) - (m * 60)
    if s < 10:
        f = '{:.0f}:{}{:.2f}'.format(m, int(s / 10), s)
    else:
        f = '{:.0f}:{:.2f}'.format(m, s)
    return f
