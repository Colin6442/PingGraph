import subprocess, matplotlib.pyplot as plt, matplotlib.animation as animation, collections
from datetime import datetime

fig = plt.figure()
fig.patch.set_facecolor('xkcd:black')
graph = fig.add_subplot(1,1,1)
graph.set_facecolor('xkcd:black')
graph.spines['bottom'].set_color('white')
graph.spines['top'].set_color('white')
graph.spines['right'].set_color('white')
graph.spines['left'].set_color('white')
graph.tick_params(axis='x', colors='white')
graph.tick_params(axis='y', colors='white')
one = []
for x in range(101):
    one.append(x)
two = [0] * 101
line = [100] * 101
count = 0
x = collections.deque(one)
y = collections.deque(two)
collect = []


def loop(num):
    log = open(r"C:\Users\colin\PycharmProjects\Python_3\Other\log\pings.txt", "r")
    for i, thing in enumerate(log):
        if num < 100:
            x[num%100] = float(num%100)
            try:
                y[num%100] = float(thing)
            except:
                print("hi")
        else:
            y.rotate(-1)
            try:
                y[100] = float(thing)
            except:
                print("hi")
    log.close()
    log = open(r"C:\Users\colin\PycharmProjects\Python_3\Other\log\pings.txt", "w")
    log.write("")
    log.close()
    graph.clear()
    graph.bar(x, y)
    graph.plot(x, line, "r")

ani = animation.FuncAnimation(fig, loop, interval=1000)
plt.show()
