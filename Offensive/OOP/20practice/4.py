class Temperature:

    def __init__(self, temp):
        self.__temp = self._check_range(temp)

    def _check_range(self, celcius):
        if celcius >= -100 and celcius <= 200:
            return celcius
        else:
            raise ValueError("Number out of range")

    @property
    def celcius(self):
        return self.__temp2

    @celcius.setter
    def celcius(self, temp):
        self.__temp = self._check_range(temp)
    
    @property
    def farenheit(self):
        return (self.__temp * 9 / 5) + 32

    @farenheit.setter
    def farenheit(self, temp):
        self.__temp = (temp - 32) * 5 / 9



temp = Temperature(100)
print(temp.celcius)
print(temp.farenheit)

temp.farenheit = 3
print(temp.celcius)
print(temp.farenheit)

