import pickle
from note import Note

class NoteHandler:
    def __init__(self, file_notes = "notes.pkl"):
        self.file_notes = file_notes    
        try:
            with open(self.file_notes, 'rb') as f:
                self.notes = pickle.load(f)
        except FileNotFoundError:
            self.notes = []
            
    def find_note(self, text):
        return [note for note in self.notes if note.matches(text)]

    def delete_note(self, i):
        if i < len(self.notes) and i >= 0:
            del self.notes[i]
            self.save_notes()
            print("\n[+] Success!")
        else:
            print("\n[!] Couldn't find that index!")
        
    def save_notes(self):
        with open(self.file_notes, 'wb') as f:
            pickle.dump(self.notes, f)
            
    def add_note(self, content):
        self.notes.append(Note(content))
        self.save_notes()
        
    def read_notes(self):
        return self.notes

    
        