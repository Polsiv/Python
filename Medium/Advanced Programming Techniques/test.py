class Context:
    def __init__(self):
        self.current_state = "A"

    def request(self):
        if self.current_state == "A":
            print("Transitioning to State A")
            self.current_state = "B"
        elif self.current_state == "B":
            print("Transitioning to State B")
            self.current_state = "C"
        elif self.current_state == "C":
            print("Transitioning to State C")
            self.current_state = "A"

# Usage
if __name__ == "__main__":
    context = Context()

    for _ in range(5):
        context.request()
    