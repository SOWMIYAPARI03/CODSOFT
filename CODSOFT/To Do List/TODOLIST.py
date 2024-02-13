import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def update_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        updated_task = entry.get()
        if updated_task:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index[0], updated_task)
            entry.delete(0, tk.END)

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

listbox = tk.Listbox(root, width=40)
listbox.pack()

add_button = tk.Button(root, text="Add", command=add_task)
update_button = tk.Button(root, text="Edit", command=update_task)
remove_button = tk.Button(root, text="Delete", command=remove_task)

add_button.pack(pady=2)
update_button.pack(pady=2)
remove_button.pack(pady=2)

root.mainloop()
