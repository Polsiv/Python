from interfaces.i_probem_solver import IProblemSolver

class FibbonaciVerifier(IProblemSolver):
    def compute_results(self, data):
        results = []
        for num in data:
           results.append([num, self.find_num_in_seq(num)])

        return results

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