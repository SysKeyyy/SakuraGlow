# :                                       :
# :           S A K U R A G L O W         :   ╾━╤デ╦︻
# :_______________________________________:  
# Please update the offstets before use.
# ________________________________________________________________
from tkinter import * # gui module
import tkinter as tk
import pymem # pymem to see csgo process
import pymem.process
import os # to get system root

root = tk.Tk()

root.geometry("600x550")
root.title("Sakuraglow v1.0")
root.configure(bg="light blue")
root.resizable(0,0)

# about
def about():
    os.system("start about.txt")
    

# quit function
def quit_btn():
    quit()

# glow function
def glow():
    print("glow enabled [+]")
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    dwEntityList = (0x4DA3F5C)
    dwGlowObjectManager = (0x52EC550)
    m_iGlowIndex = (0xA438)
    m_iTeamNum = (0xF4)
    m_fFlags = ()
    m_iCrosshairId = (0xB3E4)
    dwForceAttack = (0x31D54B4)
    dwLocalPlayer = (0xD8C2CC)

Label (text="Sakuraglow", fg="orchid1", bg="light blue", font="Consolas 50").pack()

# Add Image
glow_btn = PhotoImage(file="images\\button_enable-glow.png")
about_btn = PhotoImage(file="images\\button_about.png")
quit_button = PhotoImage(file="images\\button_quit.png")

# gui
class gui():
    button1 = Button(root, image = glow_btn, bg="light blue", borderwidth = 0, command=glow)

    button1.pack()

    button2 = Button(root, image = about_btn, bg="light blue", borderwidth = 0, command=about)

    button2.pack()

    button3 = Button(root, image = quit_button, bg="light blue", borderwidth = 0, command=quit_btn)

    button3.pack()

    root.mainloop()
