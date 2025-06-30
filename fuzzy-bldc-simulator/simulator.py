import numpy as np
import matplotlib.pyplot as plt

def fuzzy_control(error, d_error):
    # Placeholder fuzzy rule base
    return -0.5 * error + 0.3 * d_error

time = np.linspace(0, 2, 100)
error = np.sin(time)
d_error = np.gradient(error)
output = [fuzzy_control(e, de) for e, de in zip(error, d_error)]

plt.plot(time, output)
plt.title("Fuzzy Controller Output")
plt.xlabel("Time (s)")
plt.ylabel("Control Signal")
plt.grid(True)
plt.show()
