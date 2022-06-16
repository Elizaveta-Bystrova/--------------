from tkinter import *
from tkinter import Menu
from tkinter.filedialog import askopenfilename, asksaveasfilename

file_name = None

def open_file(filepath):
    with open(filepath, "r", encoding='utf-8') as input_file:
        return input_file.read()

def save_file(filepath, text):
    with open(filepath, "w", encoding='utf-8') as output_file:
        output_file.write(text)

def click_open_file():
    filepath = askopenfilename(
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")] 
    )
    if not filepath:
        return

    text = open_file(filepath)
    txt_edit.delete("1.0", END)
    txt_edit.insert(END, text)
    root.title(f"Простой текстовый редактор - {filepath}")

    global file_name
    file_name = filepath   


def click_save_as_file():
    filepath = asksaveasfilename(
       defaultextension="txt",
       filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")], 
    )
    if not filepath:
        return
        
    text=txt_edit.get("1.0", END)
    save_file(filepath, text)
    root.title(f"Простой текстовый редактор - {filepath}")

    global file_name
    file_name = filepath   


def click_save_file():
    if not file_name:
        click_save_as_file()
        return

    text = txt_edit.get("1.0", END)
    save_file(file_name, text)


root = Tk()
root.title("Простой текстовый редактор")
root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

    
mainmenu = Menu(root)
root.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть", command=click_open_file)
filemenu.add_command(label="Сохранить как...", command=click_save_as_file)
filemenu.add_command(label="Сохранить", command=click_save_file)
mainmenu.add_cascade(label="Файл",menu=filemenu)

txt_edit = Text(root)
txt_edit.grid(row=0, column=1, sticky="nsew")

root.mainloop()