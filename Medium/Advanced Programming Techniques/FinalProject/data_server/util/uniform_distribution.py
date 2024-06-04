import numpy as np
from .i_number_generator import INumberGenerator

class UniformDistribution(INumberGenerator):
    
    def gen_numbers(self, low_limit, sup_limit, amount) -> list[int]:
        rd_numbers = np.random.uniform(low_limit, sup_limit, amount)

        np.random.uniform()
        rd_numbers_list = rd_numbers.tolist()  

        rd_num_int_list = [int(num) for num in rd_numbers_list]

        return rd_num_int_list
