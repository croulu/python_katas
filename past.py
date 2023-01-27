def past(h, m, s):
    return sec_in_msec(hou_in_sec(h) + min_in_sec(m) + s)


def sec_in_msec(s):
    return s * 1000


def min_in_sec(m):
    return m * 60


def hou_in_min(h):
    return h * 60


def hou_in_sec(h):
    return hou_in_min(h) * 60
