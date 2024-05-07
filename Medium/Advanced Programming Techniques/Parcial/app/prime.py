from interfaces.i_probem_solver import IProblemSolver
import sys
class PrimeVerifier(IProblemSolver):

    def compute_results(self, data):
        
        data = self.casting_to_int(data)
        results = []
        for num in data:
            results.append([num, self.get_primes(num)])
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
    def get_primes(data):
    
        if data <= 1:
            return False
        
        for j in range(2, int(data ** 0.5) + 1):
            if data  % j == 0:
                return False
        return True


            
                
            

