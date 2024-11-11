import os
from getpass import getpass
from note_handler import NoteHandler


def show_notes(notes):
    if notes:
        print('\n[+] Displaying current notes:\n')
        for i, note in enumerate(notes):
            print(f"{i + 1}: {note}")
    else:
        print('\n[!] There are no notes to display\n')
        
def main():
    
    note_handler = NoteHandler()
    
    while True:
        print(f"\n-------------\nM\n-------------")
        print("1. Add Note")
        print("2. Read all notes")
        print("3. Search note")
        print("4. Remove note")
        print("5. Exit")
        
        opt = int(input("\n[+] Choose: "))
        
        if opt == 1:
            content = input("\n[+] Enter the content: ") 
            note_handler.add_note(content)
            
        elif opt == 2:  
            notes = note_handler.read_notes()
            show_notes(notes)
            
        elif opt == 3:
            text = input("\n[+] Enter the text so we can find the respective note: ")
            notes =  note_handler.find_note(text)
            show_notes(notes)
            
        elif opt == 4:
            i = int(input("Enter the index for the note to delete: "))
            note_handler.delete_note(i)
            
        elif opt == 5:
            break
        else:
            print("Wrong option")
        
        getpass("\n[+] Press <Enter> to continue")
    
        os.system('cls' if os.name == 'nt' else 'clear')
        


if __name__ == "__main__":
    main()