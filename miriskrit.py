#Виджет Entry - ввод текстовой инфы в наше окно и как их обробатывать
import tkinter as tk

def get_entry():
    value = name.get() #получаем значение
    if value:
        print(value)
    else:
        print('Empty Entry')

def delete_entry():
    name.delete(0,'end') #3 аргумента, указываем начало
    #если по конец,то 'end' или tk.END

def submit():
    print(name.get())
    print(password.get())
    delete_entry()
    password.delete(0,'end')
#узнаём шо под *, а потом удаляем

win = tk.Tk()
win.geometry("500x920")
win.title('Моё 1-ое приложение')

tk.Label(win, text='Имя').grid(row=0, column=0,stick='w')
tk.Label(win, text='Пароль').grid(row=1, column=0,stick='w')
name = tk.Entry(win)
password = tk.Entry(win,show='*')
name.grid(row=0, column=1)
password.grid(row=1, column=1)
#show подставится заместо слов

tk.Button(win,text='get',command=get_entry).grid(row=2, column=0,stick='we')
tk.Button(win,text='delete',command=delete_entry).grid(row=2, column=1,stick='we')
tk.Button(win,text='Submit',command=submit).grid(row=3, column=0,stick='we')
tk.Button(win,text='insert',command=lambda: name.insert(1, 'hello'))\
    .grid(row=2, column=2, stick='we')

win.grid_columnconfigure(0,minsize=100)
win.grid_columnconfigure(1,minsize=100)
win.mainloop()