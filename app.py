import os
import time
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import webbrowser
import pyautogui

compiler = Tk()
compiler.title("PyBlue Code Editor")
compiler.geometry("800x720")
compiler.minsize(800, 720)
compiler.maxsize(800, 720)

tabControl = ttk.Notebook(compiler) 
  
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
tab3 = ttk.Frame(tabControl) 
tab5 = ttk.Frame(tabControl) 
tab4 = ttk.Frame(tabControl) 

tabControl.add(tab1, text ='Tab 1') 
tabControl.add(tab2, text ='Tab 2') 
tabControl.add(tab3, text ='Tab 3') 
tabControl.add(tab4, text ='Tab 4') 
tabControl.add(tab5, text ='Tab 5') 
tabControl.pack(expand = 1) 

file_path = ''
file_path_2 = ''
file_path_3 = ''
file_path_4 = ''
file_path_5 = ''

def set_file_path(which_file_path, path):
    global file_path
    global file_path_2
    global file_path_3
    global file_path_4
    global file_path_5
    if which_file_path == "1":
        file_path = path
    if which_file_path == "2":
        file_path_2 = path
    if which_file_path == "3":
        file_path_3 = path
    if which_file_path == "4":
        file_path_4 = path
    if which_file_path == "5":
        file_path_5 = path

def open_file(event=None):
    path = askopenfilename(filetypes=[('Python Files', '*.py'),('C++ Files', '*.cpp'),('C Files', '*.c'),('Html Files', '*.html'),('CSS Files', '*.css'),('JS Files', '*.js'),('PythonScript Files', '*.ps'),('Txt Files', '*.txt')])
    with open(path, 'r') as file:
        code = file.read()
        i = True
        while i==True:
            tabQ = pyautogui.prompt("In which tab does you want to open this file?\n1, 2, 3, 4, 5")

            if tabQ == "1":
                editor.delete('1.0', END)
                editor.insert('1.0', code)
                set_file_path("1", path)
                i = False
            elif tabQ == "2":
                editor2.delete('1.0', END)
                editor2.insert('1.0', code)
                set_file_path("2", path)
                i = False
            elif tabQ == "3":
                editor3.delete('1.0', END)
                editor3.insert('1.0', code)
                set_file_path("3", path)
                i = False
            elif tabQ == "4":
                editor4.delete('1.0', END)
                editor4.insert('1.0', code)
                set_file_path("4", path)
                i = False
            elif tabQ == "5":
                editor5.delete('1.0', END)
                editor5.insert('1.0', code)
                set_file_path("5", path)
                i = False
            else:
                pyautogui.alert("Please only enter between 1-2-3-4-5!")
                i = True

def save(event=None):
    j = pyautogui.prompt("Of which tab does you want to save the file?\n1, 2, 3, 4, 5")
    i = True
    while i==True:
        try:
            if j == "1":
                code = editor.get('1.0', END)
                path = file_path
                with open(path, 'w') as file:
                    file.write(code)
                    set_file_path(j, path)
                i = False
            elif j == "2":
                code = editor2.get('1.0', END)
                path = file_path_2
                with open(path, 'w') as file:
                    file.write(code)
                    set_file_path(j, path)
                i = False
            elif j == "3":
                code = editor3.get('1.0', END)
                path = file_path_3
                with open(path, 'w') as file:
                    file.write(code)
                    set_file_path(j, path)
                i = False
            elif j == "4":
                code = editor4.get('1.0', END)
                path = file_path_4
                with open(path, 'w') as file:
                    file.write(code)
                    set_file_path(j, path)
                i = False
            elif j == "5":
                code = editor5.get('1.0', END)
                path = file_path_5
                with open(path, 'w') as file:
                    file.write(code)
                    set_file_path(j, path)
                i = False
            else:
                code = pyautogui.alert("Please only enter between 1-2-3-4-5!")
                i = True
        except:
            return

def save_as(event=None):
    path = asksaveasfilename(filetypes=[('Python Files', '*.py'),('C++ Files', '*.cpp'),('C Files', '*.c'),('Html Files', '*.html'),('CSS Files', '*.css'),('JS Files', '*.js'),('PythonScript Files', '*.ps'),('Txt Files', '*.txt'),('Any Files', '*.*')])
    with open(path, 'w') as file:
        i = True
        while i==True:
            tabQ = pyautogui.prompt("which tab does you want to save the file as?\n1, 2, 3, 4, 5")

            if tabQ == "1":
                code = editor.get('1.0', END)
                file.write(code)
                i = False
            elif tabQ == "2":
                code = editor2.get('1.0', END)
                file.write(code)
                i = False
            elif tabQ == "3":
                code = editor3.get('1.0', END)
                file.write(code)
                i = False
            elif tabQ == "4":
                code = editor4.get('1.0', END)
                file.write(code)
                i = False
            elif tabQ == "5":
                code = editor5.get('1.0', END)
                file.write(code)
                i = False
            else:
                code = pyautogui.alert("Please only enter between 1-2-3-4-5!")
                i = True

        set_file_path(tabQ, path)


def run(event=None):
    code_output.insert(END, '''
|---PYTHON------------------------|


''')
    j = pyautogui.prompt("Which file you want to run?\n1-2-3-4-5")
    if j == "1":
        command = f'python {file_path}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        code_output.insert(END, output)
        code_output.insert(END,  error)
        endline = '''
|---------------------------------|
'''
        code_output.insert(END,  endline)
    if j == "2":
        command = f'python {file_path_2}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        code_output.insert(END, output)
        code_output.insert(END,  error)
        endline = '''
|---------------------------------|
'''
        code_output.insert(END,  endline)
    if j == "3":
        command = f'python {file_path_3}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        code_output.insert(END, output)
        code_output.insert(END,  error)
        endline = '''
|---------------------------------|
'''
        code_output.insert(END,  endline)
    if j == "4":
        command = f'python {file_path_4}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        code_output.insert(END, output)
        code_output.insert(END,  error)
        endline = '''
|---------------------------------|
'''
        code_output.insert(END,  endline)
    if j == "5":
        command = f'python {file_path_5}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        code_output.insert(END, output)
        code_output.insert(END,  error)
        endline = '''
|---------------------------------|
'''
        code_output.insert(END,  endline)

def nodeRun(event=None):
    code_output.insert(END, '''
|---Node.js------------------------|


''')
    j = pyautogui.prompt("Which file you want to Node.js?\n1-2-3-4-5")
    if j == "1":
        command = f'node {file_path}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        code_output.insert(END, output)
        code_output.insert(END,  error)
    if j == "2":
        command = f'node {file_path_2}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        code_output.insert(END, output)
        code_output.insert(END,  error)
    if j == "3":
        command = f'node {file_path_3}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        code_output.insert(END, output)
        code_output.insert(END,  error)
    if j == "4":
        command = f'node {file_path_4}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        code_output.insert(END, output)
        code_output.insert(END,  error)
    if j == "5":
        command = f'node {file_path_5}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        code_output.insert(END, output)
        code_output.insert(END,  error)
    # os.system(f"node {file_path}")
    # code_output.insert(END, os.system("cmd"))

def webRun(event=None):
    j = pyautogui.prompt("Which file you want to run?\n1-2-3-4-5")
    if j == "1":
        webbrowser.open(file_path)
    if j == "2":
        webbrowser.open(file_path_2)
    if j == "3":
        webbrowser.open(file_path_3)
    if j == "4":
        webbrowser.open(file_path_4)
    if j == "5":
        webbrowser.open(file_path_5)

def psrun(event=None):
    j = pyautogui.prompt("Which file you want to run?\n1-2-3-4-5")
    if j == "1":
        os.startfile("cmd")
        time.sleep(3)
        pyautogui.write("py-script")
        pyautogui.press("enter")
        pyautogui.write(file_path)
        pyautogui.press("enter")
    if j == "2":
        os.startfile("cmd")
        time.sleep(3)
        pyautogui.write("py-script")
        pyautogui.press("enter")
        pyautogui.write(file_path_2)
        pyautogui.press("enter")
    if j == "3":
        os.startfile("cmd")
        time.sleep(3)
        pyautogui.write("py-script")
        pyautogui.press("enter")
        pyautogui.write(file_path_3)
        pyautogui.press("enter")
    if j == "4":
        os.startfile("cmd")
        time.sleep(3)
        pyautogui.write("py-script")
        pyautogui.press("enter")
        pyautogui.write(file_path_4)
        pyautogui.press("enter")
    if j == "5":
        os.startfile("cmd")
        time.sleep(3)
        pyautogui.write("py-script")
        pyautogui.press("enter")
        pyautogui.write(file_path_5)
        pyautogui.press("enter")

def minCpp(event=None):
    j = pyautogui.prompt("Which file you want to run with MinGw?\n1-2-3-4-5")
    ej = pyautogui.prompt("Enter the Executable Name:")
    if j == "1":
        os.startfile("cmd")
        time.sleep(3)
        pyautogui.write(message=f"gcc {file_path} -o {ej}")
        pyautogui.press("enter")
        pyautogui.write(message=f"{ej}.exe")
        pyautogui.press("enter")
    if j == "2":
        os.startfile("cmd")
        time.sleep(3)
        pyautogui.write(message=f"node {file_path_2} -o {ej}")
        pyautogui.press("enter")
        pyautogui.write(message=f"{ej}.exe")
        pyautogui.press("enter")
    if j == "3":
        os.startfile("cmd")
        time.sleep(3)
        pyautogui.write(message=f"node {file_path_3} -o {ej}")
        pyautogui.press("enter")
        pyautogui.write(message=f"{ej}.exe")
        pyautogui.press("enter")
    if j == "4":
        os.startfile("cmd")
        time.sleep(3)
        pyautogui.write(message=f"node {file_path_4} -o {ej}")
        pyautogui.press("enter")
        pyautogui.write(message=f"{ej}.exe")
        pyautogui.press("enter")
    if j == "5":
        os.startfile("cmd")
        time.sleep(3)
        pyautogui.write(message=f"gcc {file_path_5} -o {ej}")
        pyautogui.press("enter")
        pyautogui.write(message=f"{ej}.exe")
        pyautogui.press("enter")

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', accelerator='Ctrl+O', command=open_file)
file_menu.add_command(label='Save', accelerator='Ctrl+S', command=save)
file_menu.add_command(label='Save As', accelerator='Ctrl+Z', command=save_as)
file_menu.add_command(label='Exit', accelerator='Ctrl+Q', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', accelerator='Ctrl+P', command=run)
run_bar.add_command(label='PythonScript', accelerator='Ctrl+N', command=psrun)
run_bar.add_command(label='C/C++', accelerator='Ctrl+M', command=minCpp)
run_bar.add_command(label='Web', accelerator='Ctrl+W', command=webRun)
run_bar.add_command(label='Node.js', accelerator='Ctrl+J', command=nodeRun)
menu_bar.add_cascade(label='Execute', menu=run_bar)

compiler.config(menu=menu_bar)

editor = Text(tab1)
editor.pack()
editor2 = Text(tab2)
editor2.pack()
editor3 = Text(tab3)
editor3.pack()
editor4 = Text(tab4)
editor4.pack()
editor5 = Text(tab5)
editor5.pack()

code_output = Text(height=10)
code_output.pack()

compiler.bind("<Control-o>", open_file)
compiler.bind("<Control-s>", save)
compiler.bind("<Control-z>", save_as)
compiler.bind("<Control-q>", exit)
compiler.bind("<Control-p>", run)
compiler.bind("<Control-n>", psrun)
compiler.bind("<Control-j>", nodeRun)
compiler.bind("<Control-w>", webRun)
compiler.bind("<Control-m>", minCpp)

compiler.mainloop()





