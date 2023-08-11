def write(text, time, addition):
    ready = ""
    ready2 = ""
    for i in range(time):
        for i in range(addition):
            ready = ready + text
            ready = ready + " "
        ready2 = ready2 + ready + "\n"
        ready = ""
    return ready2

def write_revers(text, time, addition):
    ready = ""
    ready2 = ""
    for i in range(time):
        for i in range(addition):
            ready = ready + text[::-1]
            ready = ready + " "
        ready2 = ready2 + ready + "\n"
        ready = ""
    return ready2

def write_combo(text, time, addition):
    ready = ""
    ready2 = ""
    a = 0
    for i in range(time):
        for i in range(addition):
            if a == 0:
                ready = ready + text
                ready = ready + " "
                a = 1
            elif a == 1:
                ready = ready + text[::-1]
                ready = ready + " "
                a = 0
        ready2 = ready2 + ready + "\n"
        ready = ""
    return ready2

def writer_cool(time, addition):
    ready = ""
    ready2 = ""
    for i in range(time):
        for i in range(addition):
            ready = ready + "thanks :) "
        ready2 = ready2 + ready + "\n"
        ready = ""
    return ready2
