from app.my_app import MyApp
from app.data_handler import DataHandler
from app.problem_handler import ProblemHandler
from app.file_storage import FileStorage
import sys
from shapes import square


def main():

    paths = {
        "fibbonaci_path": "config_paths/config_fibonacci_path.json",
        "prime_path": "config_paths/config_prime_path.json"
    }

    
    input = int(sys.argv[1]) 

    if input == 1: 
        storage = FileStorage(paths["prime_path"])
    else:
        storage = FileStorage(paths["fibbonaci_path"])

    data_handler = DataHandler(storage)
    problem_handler = ProblemHandler()
    myapp = MyApp(data_handler, problem_handler)

    myapp.run()

main()