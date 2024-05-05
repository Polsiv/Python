from interfaces.i_probem_solver import IProblemSolver

class PrimeVerifier(IProblemSolver):
    def compute_results(self, data):
        results = []
        for num in data:
            results.append([num, self.get_primes(num)])
        return results

    @staticmethod
    def get_primes(data):
    
        if data <= 1:
            return False
        
        for j in range(2, int(data ** 0.5) + 1):
            if data  % j == 0:
                return False
        return True


            
                
            

