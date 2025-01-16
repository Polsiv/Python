#!/usr/bin/env python3

import tkinter as tk

class Calculator:

    def __init__(self, root) -> None:
        self.root = root
        self.root.bind("<Key>", self.key_press)
        self.operation = ''
        self.current = ''
        self.total = 0
        self.verify_op = False
        self.display = tk.Entry(
            self.root,
            width = 15,
            font = ("Century Gothic", 25),
            justify = "right"
        )

    def key_press(self, event):
        key = event.char

        if key == "\r": # enter
            self.compute()
            return
    
        elif key == "\x08": # backspace
            self.clear_display()
            return
        
        elif key == "\x1b": # escape
            self.root.quit()
            return
        
        elif key not in "+-/*." and not key.isdigit():
            return
        
        else:
            self.click(key)

    def define_structure(self):
        self.display.grid(
            row = 0,
            column = 0, 
            padx = 5, 
            pady = 5, 
            columnspan = 4
        )

        row = 1
        col = 0
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", ".", "+",
            "="
        ]
        
        for button in buttons:
            self.create_button(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1      
                      
    def clear_display(self):
        self.display.delete("0", tk.END)
        self.verify_op = False
        self.total = 0
        self.current = ''
        self.operation = ''
        
    def click(self, value):

        self.display.insert(tk.END, value)
        if value not in "+-/*":
            self.current += value
        else:
            if self.current and not self.operation:
                self.total = float(self.current)

            self.current = ''
            self.verify_op = True
            self.operation = value

    def compute(self):
        
        try:
            if self.current and self.operation:
                if self.operation == "+":
                    self.total += float(self.current)
                if self.operation == "-":
                    self.total -= float(self.current)
                if self.operation == "*":
                    self.total *= float(self.current)
                if self.operation == "/":
                    self.total /= float(self.current)

                self.display.delete("0", tk.END)
                self.total = int(self.total) if self.total.is_integer() else self.total
                self.display.insert(tk.END, round(self.total, 7))

        except ZeroDivisionError:
            print("Not today!")
        except AttributeError:
            print("Attribute error!")
                
    def create_button(self, button_content, row, col):
        if button_content == "C":
            button = tk.Button(
                self.root,
                text = button_content, 
                width = 1, 
                command = self.clear_display
            )

        elif button_content == "=":
            button = tk.Button(
                self.root,
                text = button_content,
                width = 1,
                command = self.compute
            )

        else:
            button = tk.Button(
                self.root,
                text = button_content,
                width = 1,
                command = lambda: self.click(button_content)
            )

        button.grid(row = row, column = col, pady = 5)

def main():
    root = tk.Tk()
    root.configure(bg="#0D1B2F")
    gui = Calculator(root)
    gui.define_structure()

    root.mainloop()

if __name__ == "__main__":
    main()