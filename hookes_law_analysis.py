import random
import numpy as np
import matplotlib.pyplot as plt


def force(k, x):
    return k * x


extensions = [1, 2, 3, 4, 5]

x_values = []
for cm in extensions:
    x_values.append(cm / 100)

forces = []
for x in x_values:
    forces.append(force(200, x))

random.seed(1)
noisy_forces = []
for f in forces:
    noisy_forces.append(f + random.uniform(-0.3, 0.3))

slope_noisy = (noisy_forces[4] - noisy_forces[0]) / (x_values[4] - x_values[0])
print("k from two points =", round(slope_noisy, 1))

k_fit, intercept = np.polyfit(x_values, noisy_forces, 1)
print("k from best fit =", round(k_fit, 1))

fit_line = []
for x in x_values:
    fit_line.append(k_fit * x + intercept)

plt.plot(x_values, forces, "-", label="true line (k = 200)")
plt.plot(x_values, noisy_forces, "o", label="simulated readings")
plt.plot(x_values, fit_line, "--", label="best fit")
plt.xlabel("Extension (m)")
plt.ylabel("Force (N)")
plt.title("Hooke's Law: force against extension")
plt.legend()
plt.savefig("hookes_law_plot.png")
plt.show()