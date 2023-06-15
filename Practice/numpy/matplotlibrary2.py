import numpy as np
import matplotlib.pyplot as plt

#<-----------Graphing 3 graphs--------------->

x = np.linspace(0, 10, 10000)
y = np.sin(x)
z = np.cos(x)
s = np.log(x)

plt.figure(figsize=(15, 3))

plt.subplot(1, 3, 1)
plt.plot(x, y, "b--")

plt.subplot(1, 3, 2)
plt.plot(x, z, "r-")

plt.subplot(1, 3, 3)
plt.plot(x[::500], s[::500], "gx")

plt.show()

#<-----------Graphing an image--------------->

image = np.array([[255, 0],
                  [112, 50]])

plt.imshow(image, cmap="Blues")
plt.show()



