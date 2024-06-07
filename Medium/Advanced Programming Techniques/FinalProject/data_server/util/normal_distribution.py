#pylint: disable = R0903, C0114
import numpy as np
from .i_number_generator import INumberGenerator

class NormalDistribution(INumberGenerator):
    """Class that implements interface and generates a list of random numbers using normal distribution"""

    def gen_numbers(self, low_limit, sup_limit, amount) -> list[int]:
        """uses numpy library to use normal distribution"""
        mean = (low_limit + sup_limit) / 2

        std_dev = (sup_limit - low_limit) / 6

        rd_numbers = np.random.normal(mean, std_dev, amount)

        rd_numbers = np.clip(rd_numbers, low_limit, sup_limit)

        rd_numbers_list = rd_numbers.tolist()

        rd_num_int_list = [int(num) for num in rd_numbers_list]

        return rd_num_int_list
