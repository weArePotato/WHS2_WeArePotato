from tkinter import *
import tkinter.filedialog   #модуль filedialog для диалогов открытия/закрытия файла

def Quit(ev):
    global root
    root.destroy()
    
def LoadFile(ev):
    ftypes = [('Bullcode', '*.bc')] # Фильтр файлов
    fn = tkinter.filedialog.Open(root, filetypes = ftypes).show()
    root.title(f"{fn} - Bull-code")
    if fn == '':
        return  
    textbox.delete('1.0', 'end')    # Очищаем окно редактирования
    textbox.insert('1.0', open(fn).read())   # Вставляем текст в окно редактирования
   
     
    global cur_path
    cur_path = fn # Храним путь к открытому файлу
   
def SaveFile(ev):
    try:
        open(cur_path, 'w').write(textbox.get('1.0', 'end'))
    except NameError:
        fn = tkinter.filedialog.SaveAs(root, filetypes = [('Bullcode', '*.bc')]).show()
        if fn == '':
            return
        open(fn, 'wt').write(textbox.get('1.0', 'end'))
        
def SetCommand(ev):
    try:
        command_text.set(f"$: bullcode {cur_path} --config __main__")
    except NameError:
        command_text.set("$: bullcode <file_path> --config __main__")
        
root = Tk()   # объект окна верхнего уровня создается от класса Tk модуля tkinter. 
#Переменную, связываемую с объектом, часто называют root (корень)

root.title(u'Bull-code')
root.geometry("1110x600")


panelFrame = Frame(root, height = 60, bg = 'gray')
textFrame = Frame(root, height = 340, width = 600)

panelFrame.pack(side = 'top', fill = 'x')   #упакуем с привязкой к верху
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)  

textbox = Text(textFrame, font='Arial 14', wrap='word')  #перенос по словам метод wrap
scrollbar = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side = 'left', fill = 'both', expand = 1)  #текстбокс слева
scrollbar.pack(side = 'right', fill = 'y')    #расположим скролбар (лифт) справа

command_text = StringVar(root)
command_text.set("Command here")

img = PhotoImage(file="./icon.png")

loadBtn = Button(panelFrame, text = 'Load')
saveBtn = Button(panelFrame, text = 'Save')
runBtn = Button(panelFrame, text = 'Get command', bg='#A9A9A9',fg='green')
quitBtn = Button(panelFrame, text = 'Exit', bg='#A9A9A9',fg='red')
commandLabel = Label(panelFrame, textvariable = command_text, bg='white', fg='black', font=('arial', 16, 'bold'))
imageLabel = Label(panelFrame, image=img, bg = 'gray')

loadBtn.bind("<Button-1>", LoadFile)
saveBtn.bind("<Button-1>", SaveFile)
runBtn.bind("<Button-1>", SetCommand)
commandLabel.bind("<Button-1>", None)
imageLabel.bind("<Button-1>", None)
quitBtn.bind("<Button-1>", Quit)

loadBtn.place(x = 10, y = 10, width = 130, height = 40)
saveBtn.place(x = 150, y = 10, width = 130, height = 40)
runBtn.place(x = 290, y = 10, width = 130, height = 40)
quitBtn.place(x = 430, y = 10, width = 100, height = 40)
commandLabel.place(x = 540, y = 10, width = 500, height = 40)
imageLabel.place(x = 1050, y = 10, height = 40)

root.mainloop()
