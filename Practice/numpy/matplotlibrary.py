import numpy as np
import matplotlib.pyplot as plt

space = np.linspace(0, 1000, 10)
#Should print from 0 to 10 in 0.1 gaps
space2 = np.arange(0, 10, 1)
#print(space2)


#<----------------Graphic for sin function------------>

space3 = np.arange(0, 12.58, 0.1)

plt.figure(figsize=(20, 10))
plt.plot(space3, np.cos(space3), label="Linspace")
plt.legend()
plt.show()

#<----------------Graphic for popultion------------>

countries = {
    "Countries" : ["Col", "Germany", "Mexico", "Brasil", "EE.UU"],
    "Population" : [51.52, 83, 126.7, 214.3, 331.9]
}

plt.bar(x = countries["Countries"], height=countries["Population"])
plt.title("Populations around the world")
plt.ylabel("Millions")
plt.xlabel("Countries")
plt.grid(visible=True)
plt.show()

#<----------------Another graphic for popultion------------>

plt.scatter(x = countries["Countries"], y = countries["Population"])
plt.show()


#<----------------Another graphic -------------------------->

plt.scatter(x = np.linspace(0, 100, 100), y = np.linspace(0, 100, 100)**2)
plt.show()


