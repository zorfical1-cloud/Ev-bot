def calculate_ev(pp_line, fd_line):
    try:
        diff = fd_line - pp_line
        ev_percent = (diff / pp_line) * 100
        return round(ev_percent, 2)
    except:
        return 0
