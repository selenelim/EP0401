import matplotlib.pyplot as plt
import csv
import numpy as np

# Create empty lists to store data
n = []
temp = []
humi = []

# Read data from CSV file
with open('/Users/selene/EP0401/sensordata.txt', 'r') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        if not row or len(row) < 3:
            continue  # Skip empty or invalid lines
        n.append(int(row[0]))       # Append sample number
        temp.append(int(row[1]))    # Append temperature
        humi.append(int(row[2]))    # Append humidity

# Calculate average temperature and humidity
mean_temp = int(np.mean(temp))
mean_humi = int(np.mean(humi))

# Create lists of repeated average values (flat lines)
ave_temp = [mean_temp] * len(n)
ave_humi = [mean_humi] * len(n)

# Plot the data
plt.plot(n, temp, label='temperature')
plt.plot(n, humi, label='humidity')
plt.plot(n, ave_temp, label='mean temperature')
plt.plot(n, ave_humi, label='mean humidity')

# Add labels, title, legend
plt.xlabel('last 10 samples, 2 sec intervals')
plt.ylabel('temperature in deg C & humidity in %')
plt.title('Sensor data from AM2302')
plt.legend()

# Show the graph
plt.show()
