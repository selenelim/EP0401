# Import the modules needed (ONLY TESTABLE ON RASP PI)
import RPi.GPIO as GPIO
from time import sleep
import spidev
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
spi = spidev.SpiDev()
spi.open(0, 0)

# Count up continuously
count = 0

# Lists to store readings (0–1023) and entry numbers (0, 1, 2, ...)
readings = []
entries = []

# One graph, and put this at row 1, col 1
fig = plt.figure()
pot_graph = fig.add_subplot(1, 1, 1)

def animate(i):
    # Make variables global
    global count

    # Read potentiometer value
    spi.max_speed_hz = 1350000
    r = spi.xfer2([1, 8 << 4, 0])
    pot_value = ((r[1] & 3) << 8) + r[2]

    # For each list: keep 10 items, add new item at back, increment count
    if count > 9:
        readings.pop(0)
        entries.pop(0)
    readings.append(pot_value)
    entries.append(count)
    count += 1

    # Update plot
    pot_graph.clear()
    pot_graph.plot(entries, readings)
    pot_graph.set_xlabel('1-sec samples', fontsize=10)
    pot_graph.set_ylabel('potentiometer values', fontsize=10)
    pot_graph.set_title('Matplotlib live graph')

# Animate the graph with 1-second interval
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
