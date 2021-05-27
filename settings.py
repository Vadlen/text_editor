import tkinter
import codecs
from tkinter import*
from tkinter.filedialog import askopenfile, asksaveasfile, askopenfilename, asksaveasfilename
from tkinter.messagebox import showerror
from tkinter import messagebox
from tkinter import filedialog

APP_NAME = 'Writing Pad'

WIDHT = 900
HEIGHT = 650

app = tkinter.Tk()

text = tkinter.Text(app, width=WIDHT - 50, height=HEIGHT, wrap='word')

class Text_editor:
    def __init__(self):
        self.name_file = tkinter.NONE
    
    def new_file(self):
        self.name_file = 'Без имянный'
        text.delete('1.0', tkinter.END)

    def save_file(self):
        data = text.get('1.0', tkinter.END)
        output = open(self.name_file, 'w', encoding='utf-8')
        output.write(data)
        output.close()

    def open_file(self):
        inp = askopenfilename()
        if inp is None:
            return

        with codecs.open(inp, encoding='utf-8') as f:
            data = f.read()
            text.delete('1.0', tkinter.END)
            text.insert("1.0", data)

    def save_file(self):
        data = text.get('1.0', tkinter.END)
        output = open(self.name_file, 'w', encoding='utf-8')
        output.write(data)
        output.close()
    
    def save_as_file(self):
        output = asksaveasfile(mode="w", defaultextension="txt")
        data = text.get("1.0", tkinter.END)
        try:
            output.write(data.rstrip())
        except Exception:
            showerror(title="Ошибка!", message="Ошобка при сохранении файла")

    def get_info(self):
        messagebox.showinfo("Справка", "Информация о нашем приложении")