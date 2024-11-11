class Note:
    def __init__(self, content):
        self.content = content
        
    def matches(self, text):
        return text in self.content
        
    def __str__(self):
        return self.content