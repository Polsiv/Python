#!/usr/bin/env python3
import socket
from tkinter import *
import threading
from tkinter.scrolledtext import ScrolledText
import ssl


def send_message(client_socket, username, text_widget, entry_widget):

    message = entry_widget.get()
    client_socket.sendall(f"{username}: {message}".encode())

    entry_widget.delete(0, END)
    text_widget.configure(state = 'normal')
    text_widget.insert(END, f"{username}: {message}\n")
    text_widget.configure(state = 'disabled')


def receive_message(client_socket, text_widget):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            text_widget.configure(state = 'normal')
            text_widget.insert(END, message)
            text_widget.configure(state = 'disabled')
        except:
            break

def list_users_request(client_socket):
    client_socket.sendall("!users".encode())

def exit_request(client_socket, username, app):
    client_socket.sendall(f"\n{username} has left the chat!\n".encode())
    client_socket.close()

    app.quit()
    app.destroy()

def app():

    # client socket
    host = '127.0.0.1'
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client_socket = ssl.wrap_socket(client_socket) #deprecated
    client_socket.connect((host, port))
    username = input("Enter your username: ")
    client_socket.sendall(username.encode())

    App = Tk()
    App.title("Chat")

    frame_widget = Frame(App)
    text_widget = ScrolledText(App, state = 'disabled') # cant type
    entry_widget = Entry(frame_widget)
    entry_widget.bind("<Return>", lambda _: send_message(client_socket, username, text_widget, entry_widget))
    button_widget = Button(
        frame_widget,
        text = "Send",
        height = 1,
        command = lambda: send_message(client_socket, username, text_widget, entry_widget)
    )
    list_users = Button(App, text = "List Users", command = lambda: list_users_request(client_socket))

    leave = Button(App, text = "Leave", command = lambda: exit_request(client_socket, username, App))
    
    text_widget.pack()
    frame_widget.pack(fill = BOTH, expand = 1, pady = 4, padx = 10,)
    entry_widget.pack(side = LEFT, fill = BOTH, expand = 1)
    button_widget.pack(side = RIGHT, padx = 5)
    list_users.pack(padx = 5, pady = 5)
    leave.pack()
    

    thread = threading.Thread(target = receive_message, args = (client_socket, text_widget))
    thread.daemon = True
    thread.start()
    


    App.mainloop()
    client_socket.close()

if __name__ == "__main__":
    app()