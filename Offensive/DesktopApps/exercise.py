#!/usr/bin/env python3

import tkinter as tk

def button_pressed():
    print("Buttom clicked!")

def get_data(input_label):
    data = input_label.get()
    print(data)


def get_data_for_Text(input_label):
    data = input_label.get("1.0", tk.END) # 1: first line, 0: first char
    print(data)

def main():
    # main class
    root = tk.Tk()
    
    # set windows size
    root.geometry('1000x1000')

    # root.title("First Desktop App")

    # labels
    label = tk.Label(root, text = "Hello World", bg = "#000000")
    label2 = tk.Label(root, text = "Second Label lol", bg = "#464646")
    label3 = tk.Label(root, text = "Third Label lol", bg = "#464646")
    label4 = tk.Label(root, text = "Fourth lol", bg = "#464646")

    # buttom
    buttom = tk.Button(root, text = "Click me", command = button_pressed)

    # placing shit using place (lol)
    place_label = tk.Label(root, text = "Place") 
    place_label2 = tk.Label(root, text = "Place 2") 
    place_label3 = tk.Label(root, text = "Place 3") 

    # Frames
    frame = tk.Frame(root, bg = "#4F4F4F", bd = 2)
    label5 = tk.Label(frame, text = "Inside the frame!")
    label6 = tk.Label(frame, text = "Inside the frame!")

    # canvas
    canvas = tk.Canvas(root, width = 300, height = 300, bg = "#FFF")


    # inputs
    input_label = tk.Entry(root)
    input_buttom = tk.Button(root, text = "Send", command = lambda: get_data(input_label))

    # for text
    #input_label = tk.Text(root)

    # there are 3 ways to organize the content, grind(), place(), pack()
    # using both grid and pack at the same time isnt compatible

    # using pack
    buttom.pack(fill = tk.X) # fill the X axis
    label.pack(fill = tk.Y, side = tk.LEFT)
    label2.pack()
    label3.pack()
    input_label.pack(pady = 5) #padding-y 5 px
    input_buttom.pack()
    label5.pack()
    label6.pack()
    canvas.pack()

    # figures 
    oval = canvas.create_oval(50, 50, 150, 150, fill = "#2D2DF7") # positions
    rectangle = canvas.create_rectangle(300, 50, 200, 450, fill = "#00E3A5")
    line = canvas.create_line(50,250, 200, 320, fill = "#4B5BE6", width = 3)

    # using grid

    grid_label = tk.Label(root, text = "Grid")
    # grid_label.grid(row = 1, column = 0, columnspan = 2)

    # using place
    place_label.place(x = 20, y = 20) # pixels
    place_label2.place(relx = 0.8, rely = 0.2) # percentage
    place_label3.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER) # takes the label center
    frame.place(relx = 0.4, rely = 0.4, anchor = tk.CENTER)

    # run the program
    root.mainloop()

if __name__ == "__main__":
    main()


