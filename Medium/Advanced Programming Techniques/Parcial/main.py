from app.my_app import MyApp
from app.prime import  PrimeVerifier
from app.fibbo import FibbonaciVerifier
from app.data_handler import DataHandler
from app.problem_handler import ProblemHandler
from app.file_storage import FileStorage
import sys

def main():

    paths = {
        "fibbonaci_path": "config_paths/config_fibonacci_path.json",
        "prime_path": "config_paths/config_prime_path.json"
    }

    #inputreplit = int(input("enter 1 or 2"))
    input = int(sys.argv[1]) 

    if input == 1: 
        storage = FileStorage(paths["prime_path"])
        problem = PrimeVerifier()
    
    else:
        storage = FileStorage(paths["fibbonaci_path"])
        problem = FibbonaciVerifier()
        
    data_handler = DataHandler(storage)
    problem_handler = ProblemHandler(problem)
    myapp = MyApp(data_handler, problem_handler)

    myapp.run()

main()