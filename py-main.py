import subprocess
from tkinter import *
from tkinter import ttk

compiler = Tk()
compiler.title("PyBlue Code Editor")
compiler.geometry("800x720")
compiler.minsize(800, 720)
compiler.maxsize(800, 720)

file_path = 'D:\\CODING\\PYTHON\\Production\\Python\\PyBlue\\test.js'

def run():
    command = f'node {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert(END, output)
    code_output.insert(END,  error)

code_output = Text(height=10)
code_output.pack()

bt = Button(compiler, text="Run", command=run)
bt.pack()

compiler.mainloop()