from .data_handler import DataHandler
from .problem_handler import ProblemHandler
class MyApp:
    def __init__(self, data_handler_instance: DataHandler, problem_handler_instance: ProblemHandler):
        self.data_handler = data_handler_instance
        self.problem_handler = problem_handler_instance

    def run(self):
        data = self.data_handler.read_data() or []
        results = self.problem_handler.compute_results(data)
        self.data_handler.save_data(results)
