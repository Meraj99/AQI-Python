import matplotlib.pyplot as plt
import numpy as np

xValues, yValues = np.genfromtxt('CSV/AqiGeneral.csv', delimiter=',', unpack=True, dtype="U")

arr = np.array([0, 0, 0, 0, 0, 0])
count = xValues.size

mean = 0
variance = 0

for y in yValues:
    if y == "Healthy":
        arr[5] = arr[5] + 1
    elif y == "Moderate":
        arr[4] = arr[4] + 1
    elif y == "Unhealthy for Sensitive Groups":
        arr[3] = arr[3] + 1
    elif y == "Unhealthy":
        arr[2] = arr[2] + 1
    elif y == "Very Unhealthy":
        arr[1] = arr[1] + 1
    elif y == "Hazardous":
        arr[0] = arr[0] + 1

plt.ylabel("Frequency")
plt.bar(np.arange(arr.size), arr)
plt.xticks(np.arange(arr.size), ("Hazardous", "V. Unhealthy", "Unhealthy", "Unhealthy for SGs", "Moderate", "Healthy"))
plt.show()

for i in range(0, arr.size):
    mean += (i - 1) * arr[i]
mean = mean / count

for i in range(0, arr.size):
    variance += (i * ((arr[i] - mean) ** 2))
variance = variance / count
SD = variance ** 0.5

print("General")
print("Mean Score: " + str(round(mean, 2)))
print("Variance: " + str(round(variance, 2)))
print("SD: " + str(round(SD, 2)))
print()
####################################################################
xValues, yValues = np.genfromtxt('CSV/AqiBangalore.csv', delimiter=',', unpack=True)
variance = 0
mean = np.sum(yValues) / xValues.size

for y in yValues:
    variance += (mean - y) ** 2
variance = variance / xValues.size
SD = variance ** 0.5

if mean > 0 and int(mean) <= 50:
    AQI = "Healthy"
elif mean <= 100:
    AQI = "Moderate"
elif mean <= 150:
    AQI = "Unhealthy for Sensitive Groups"
elif mean <= 200:
    AQI = "Unhealthy"
elif mean <= 300:
    AQI = "Very Unhealthy"
else:
    AQI = "Hazardous"

print("Bangalore")
print("Mean: " + str(round(mean, 2)))
print("Variance: " + str(round(variance, 2)))
print("SD: " + str(round(SD, 2)))
print("Air Quality: " + AQI)

plt.plot(xValues, yValues, marker='o')
plt.axhline(mean, color="red", linewidth=0.5, linestyle="dashed")

plt.title('Air Quality Index for February, 2019 (Bangalore)')

plt.xlabel('Day')
plt.ylabel('Concentration of Particulate Matter (PM10)')

plt.show()
