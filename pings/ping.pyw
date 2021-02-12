import subprocess, matplotlib.pyplot as plt, matplotlib.animation as animation, collections
from datetime import datetime

fig = plt.figure()
graph = fig.add_subplot(1, 1, 1)
one = [0] * 101
two = [70] * 101
line = [100] * 101
count = 0
x = collections.deque(one)
y = collections.deque(two)

log = open(r"C:\Users\colin\PycharmProjects\Python_3\Other\log\pings.txt", "w")
log.write("")
log.close()

while True:
    try:
        ping = subprocess.check_output("ping google.com -n 2")
        ping = ping.decode("utf-8")
        start = ping.find("Average")
        end = ping[start:-1].find("ms")
        log = open(r"C:\Users\colin\PycharmProjects\Python_3\Other\log\pings.txt", "a+")
        log.write(str(ping[start + len("Average = "): start + end]) + "\n")
        log.close()
    except:
        None





