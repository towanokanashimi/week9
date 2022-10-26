import numpy as np

average_pulse_max = max(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print (average_pulse_max)

average_pulse_min = min(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print (average_pulse_min)

calorie_burnage = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]
average_calorie_burnage = np.mean(calorie_burnage)
print(average_calorie_burnage)