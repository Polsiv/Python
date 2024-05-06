from app.my_app import MyApp
from app.prime import  PrimeVerifier
from app.fibbo import FibbonaciVerifier
from app.data_handler import DataHandler
from app.problem_handler import ProblemHandler
from app.file_storage import FileStorage
import sys

def main():

    input = int(sys.argv[1]) 
    paths = {
        "fibbonaci_path": "config_paths/config_fibbonaci_path.json",
        "prime_path": "config_paths/config_prime_path.json"
    }

    if input == 1: 
        storage = FileStorage(paths["prime_path"])
        problem = PrimeVerifier()
        print("prime output file created.")

    if input == 2:
        storage = FileStorage(paths["fibbonaci_path"])
        problem = FibbonaciVerifier()
        print("fibonacci output file created.")
        
    data_handler = DataHandler(storage)
    problem_handler = ProblemHandler(problem)
    myapp = MyApp(data_handler, problem_handler)

    myapp.run()

main()