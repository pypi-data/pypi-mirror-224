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

def cipher(key, text_to_cipher):
    ready = ""
    for i in range(len(text_to_cipher)):
        for p in range(len(key)):
            if text_to_cipher[i] == key[p]:
                ready = ready + str(p)
                ready = ready + ","
                break
            elif text_to_cipher[i] == " ":
                ready = ready + " "
                break
            elif text_to_cipher[i] != key[p] and p + 1 == len(key):
                ready = ready + "!"
                ready = ready + ","
    return ready

def uncipher(key, text_to_uncipher):
    a = 0
    number = ""
    ready = ""
    for i in range(len(text_to_uncipher)):
        for p in range(len(key)):
            if text_to_uncipher[i] == ",":
                try:
                    if number != "":
                        number = int(number)
                        ready = ready + key[number]
                        number = ""
                except:
                    ready = ready + "!"
                    ready = ready + ","
                    number = ""
            elif text_to_uncipher[i] == "!":
                ready = ready + "!"
            elif text_to_uncipher[i] == " ":
                ready = ready + " "
                break
            else:
                number = number + text_to_uncipher[i]
                break
    return ready
