import tkinter as tk

def button_click(event):
    current_text = result_label['text']
    button_text = event.widget['text']
    
    if button_text == '=':
        try:
            result = eval(current_text)
            result_label['text'] = str(result)
        except:
            result_label['text'] = 'Error'
    elif button_text == 'C':
        result_label['text'] = ''
    else:
        result_label['text'] = current_text + button_text

root = tk.Tk()
root.title("Calculator")

result_label = tk.Label(root, text='', width=20, height=2, font=('Helvetica', 20))
result_label.grid(row=0, column=0, columnspan=5)


button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
         'C'
]
row_val = 1
col_val = 0

for label in button_labels:
    button = tk.Button(root, text=label, width=5, height=2, font=('Helvetica', 16))
    button.grid(row=row_val, column=col_val)
    button.bind('<Button-1>', button_click)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
root.mainloop()
