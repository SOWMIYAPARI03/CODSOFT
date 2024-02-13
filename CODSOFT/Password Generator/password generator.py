import tkinter as tk
import random
import string

def generate_password():
    username = username_entry.get()
    if not username:
        password_label.config(text="Please enter a username.")
        return
    
    password_length = int(length_entry.get())
    if password_length < 1:
        password_label.config(text="Please enter a valid length.")
        return
    
    password_characters = string.ascii_letters + string.digits + string.punctuation

    generated_password = ''.join(random.choice(password_characters) for _ in range(password_length))
    password_display.config(text=f"Generated Password:\n{generated_password}")
    accept_button.config(state=tk.NORMAL)

def accept_password():
    accepted_password = password_display.cget("text").split("\n")[1]
    accepted_password_label.config(text=f"Accepted Password: {accepted_password}")


root = tk.Tk()
root.title("Password Generator")

username_label = tk.Label(root, text=" Enter The Username:")
username_label.pack(pady=10)

username_entry = tk.Entry(root)
username_entry.pack()

instructions_label = tk.Label(root, text="Enter Password Length:")
instructions_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)


password_display = tk.Label(root, text="", wraplength=300)
password_display.pack()

accept_button = tk.Button(root, text="Accept", command=accept_password, state=tk.DISABLED)
accept_button.pack(pady=10)

accepted_password_label = tk.Label(root, text="", wraplength=300)
accepted_password_label.pack()

root.mainloop()