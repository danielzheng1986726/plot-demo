import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)
y = x ** 2
plt.figure()
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = x^2")
plt.grid(True)
plt.savefig("square_plot.png")
