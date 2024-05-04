from interfaces.i_problem_solver import IProblemSolver

class PrimeVerifier(IProblemSolver):
    def compute_results(self, data):
        results = []
        num, nums = data
        
        for i in range(num):
            if nums[i] <= 1:
                results.append([False, nums[i]])
                continue
            
            prime = True
            for j in range(2, int(nums[i]**0.5) + 1):
                if nums[i] % j == 0:
                    prime  = False
                    break
            
            results.append([prime, nums[i]])
                    
        return num, results


            
                
            

