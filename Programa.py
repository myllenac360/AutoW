from tkinter import *
from tkinter import ttk
import pyautogui
import keyboard;
import time;

#a = True

while True:
    if keyboard.is_pressed('f4'):
        print("hello world");
        #keyboard.is_pressed('alt');
        #keyboard.is_pressed('tab');
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
        break;

def fechar(*args):
    try:
        a = True
        while True:
                print("hi");
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                break;
    except:
            pass

def status(*args):
        try:
            a = True
            if (a==True):
                ttk.Label(mainframe, text="Status ON").grid(ccolumn=1, row=3, sticky=E)
                #ttk.Button(mainframe, text="Status ON", command=status).grid(column=1, row=3, sticky=E);
            else:
                ttk.Label(mainframe, text="Status OFF").grid(ccolumn=1, row=3, sticky=E)
                #ttk.Button(mainframe, text="Status OFF", command=status).grid(column=1, row=3, sticky=E);

        except:
            pass

def ligar(*args):
    try:
        a = True
        while True:
            print("hello world");
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            break;
    except:
        pass;

root = Tk()
root.title("Programa")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)



# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Fechar", command=fechar).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="Status ON/OFF", command=status).grid(column=1, row=3, sticky=E)
ttk.Button(mainframe, text="Ligar Macro (F4)", command=ligar).grid(column=2, row=2, sticky=(W, E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)


root.bind("<Return>", fechar)
root.bind("<Return>", status)
root.bind("<Return>", ligar)

root.mainloop()
