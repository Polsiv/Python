from app.my_app import MyApp
from app.filestorage import FileStorage
from app.data_handler import DataHandler
from app.fibonnaci_verifier import Fibonnaciverifier
from app.prime_verifier import PrimeVerifier


def main():

 
    storage = FileStorage()
    data_handler = DataHandler(storage)
    prime = PrimeVerifier()
    fibbo = Fibonnaciverifier()
    problem = []
    myapp = MyApp(data_handler, prime, fibbo)
    
    user_input = int(input("Enter a number: 1) for Prime number. 2) For Fibonnaci"))
    myapp.run(user_input)
    
main()