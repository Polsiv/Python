import customtkinter as ctk

def callback():
    print("Button Pressesd")


def main():
    app = ctk.CTk()
    app.title("My App")
    
    button = ctk.CTkButton(app, text = "Button", command = callback)
    button.grid(row = 0, column = 0, padx = 5, pady = 5)

    app.mainloop()

if __name__ == "__main__":
    main()