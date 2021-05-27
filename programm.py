import tkinter
from tkinter import*

from settings import *

editor = Text_editor()

app.title(APP_NAME)
app.minsize(width=WIDHT, height=HEIGHT)
app.maxsize(width=WIDHT, height=HEIGHT)


scroll = Scrollbar(app, orient=VERTICAL, command=text.yview)
scroll.pack(side='right', fill= "y")
text.configure(yscrollcommand=scroll.set)
text.pack()

menuBar = tkinter.Menu(app)

app_menu = tkinter.Menu(menuBar)
app_menu.add_command(label='Новый', command=editor.new_file)
app_menu.add_command(label='Открыть', command=editor.open_file)
app_menu.add_command(label='Сохранить', command=editor.save_file)
app_menu.add_command(label='Сохранить как', command=editor.save_as_file)

help_menu = tkinter.Menu(menuBar)
help_menu.add_command(label='Посотреть справку')
help_menu.add_command(label='Отправить отзыв')
help_menu.add_command(label='О программе')

menuBar.add_cascade(label='Файл', menu=app_menu)
menuBar.add_cascade(label='Справка', command=editor.get_info)
menuBar.add_cascade(label='Вид')
menuBar.add_cascade(label='Выход', command=app.quit)

app.config(menu=menuBar)

app.mainloop()