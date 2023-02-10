import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")

        # Create the Text widget
        self.text = tk.Text(root, wrap='word')
        self.text.pack(fill='both', expand=True)

        # Create the menu bar
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        # Create the File menu
        file_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)

        # Create the Edit menu
        edit_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label='Edit', menu=edit_menu)
        edit_menu.add_command(label='Cut', command=self.cut_text)
        edit_menu.add_command(label='Copy', command=self.copy_text)
        edit_menu.add_command(label='Paste', command=self.paste_text)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                text = file.read()
                self.text.insert('1.0', text)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')
        if file_path:
            with open(file_path, 'w') as file:
                text = self.text.get('1.0', 'end')
                file.write(text)

    def cut_text(self):
        self.text.event_generate("<<Cut>>")

    def copy_text(self):
        self.text.event_generate("<<Copy>>")

    def paste_text(self):
        self.text.event_generate("<<Paste>>")

root = tk.Tk()
text_editor = TextEditor(root)
root.mainloop()
