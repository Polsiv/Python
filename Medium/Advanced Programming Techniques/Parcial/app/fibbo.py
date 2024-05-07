from interfaces.i_probem_solver import IProblemSolver
import sys

class FibbonaciVerifier(IProblemSolver):

    def compute_results(self, data):    

        data = self.casting_to_int(data)
        results = []
        for num in data:
           results.append([num, self.find_num_in_seq(num)])
        return results
    
    @staticmethod
    def casting_to_int(data):
        try:
            casted_data = []
            for i in data:
                casted_data.append(int(i))
            return casted_data
        except ValueError:
            print("Invalid Input.")
            sys.exit()

    @staticmethod
    def find_num_in_seq(data):

        if data < 0:  
            return False

        a, b = 0, 1
        
        if data == b or data == a:
            return True
        
        while b < data:
            a, b = b, a + b
            if b == data:
                return True 
        return False