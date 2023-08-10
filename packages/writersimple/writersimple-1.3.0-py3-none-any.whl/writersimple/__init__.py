def write(what, time, addition):
    ready = ""
    for i in range(time):
        for i in range(addition):
            ready = ready + what
            ready = ready + " "
        print(ready)
        ready = ""

def write_revers(what, time, addition):
    ready = ""
    for i in range(time):
        for i in range(addition):
            ready = ready + what[::-1]
            ready = ready + " "
        print(ready)
        ready = ""

def write_combo(what, time, addition):
    ready = ""
    a = 0
    for i in range(time):
        for i in range(addition):
            if a == 0:
                ready = ready + what
                ready = ready + " "
                a = 1
            elif a == 1:
                ready = ready + what[::-1]
                ready = ready + " "
                a = 0

        print(ready)
        ready = ""

def writer_cool(time, addition):
    ready = ""
    for i in range(time):
        for i in range(addition):
            ready = ready + "thanks :) "
        print(ready)
        ready = ""
