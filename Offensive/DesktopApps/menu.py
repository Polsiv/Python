import tkinter as tk
from tkinter import messagebox, filedialog


def action():
    messagebox.showinfo("Menu", "test")
    path = filedialog.askopenfilename()
    print("path:", path)
def main():
    root = tk.Tk()
    root.title("Menu")

    menu_bar = tk.Menu(root)
    root.config(menu = menu_bar)

    menu1 = tk.Menu(menu_bar, tearoff = 0)
    menu_bar.add_cascade(label = "menu", menu = menu1)

    menu1.add_command(label = "number 1")
    menu1.add_command(label = "number 2")

    menu2 = tk.Menu(menu_bar, tearoff = 0)
    menu_bar.add_cascade(label = "menu 2", menu = menu2)
    menu2.add_command(label = "number 1")
    menu2.add_command(label = "number 2", command = action)
    root.mainloop()


if __name__ == "__main__":
    main()