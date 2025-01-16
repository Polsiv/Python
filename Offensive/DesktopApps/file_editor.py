#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, messagebox

class SimpleTextEditor:
    def __init__(self, root):
        self.root = root
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill = tk.BOTH, padx = 5, pady = 5, expand = 1)
        self.current_opened_file = ""

    def confirm_exit(self):
        if messagebox.askokcancel("Exit", "You're sure to quit?"):
            self.root.destroy()

    def new_file(self):
        self.text_area.delete("1.0", tk.END)
        self.current_opened_file = ""

    def open_file(self):
        path = filedialog.askopenfilename()

        if path: 
            self.text_area.delete("1.0", tk.END)
            with open(path, 'r') as file:
                self.text_area.insert("1.0", file.read())
            
            self.current_opened_file = path
            print(self.current_opened_file)

    def save_file(self):
        if not self.current_opened_file:
            new_file_path = filedialog.asksaveasfilename()

            if new_file_path:
                self.current_opened_file = new_file_path
            else:
                pass

        with open(self.current_opened_file, 'r') as file:
            file.write(self.text_area.get("1.0", tk.END))

def main():
    root = tk.Tk()
    editor = SimpleTextEditor(root)
    menu_bar = tk.Menu(root)
    menu_options = tk.Menu(menu_bar, tearoff = 0)
    menu_options.add_command(label = "New", command = editor.new_file)
    menu_options.add_command(label = "Open", command = editor.open_file)
    menu_options.add_command(label = "Save", command = editor.save_file)
    menu_options.add_command(label = "Exit", command = editor.confirm_exit)    
    root.config(menu = menu_bar)
    menu_bar.add_cascade(label = "File", menu = menu_options)
 
    root.mainloop()

if __name__ == "__main__":
    main()