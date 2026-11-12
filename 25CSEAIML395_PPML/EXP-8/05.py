import numpy as np

a = np.array([10, 20, 30, 40])
np.save("data.npy", a)

b = np.load("data.npy")
print("Loaded array:", b)