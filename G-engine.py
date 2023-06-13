__author__ = "ItzFimes"

#Set a variable that lets G-engine know if it is online on offline, starting value is always "True"(online)
internetcn = True

#Import a bunch of stuff, if importing something fails a .bat file is run to try to install it
from os import read

try:
    import subprocess
except:
    print("Subprocess not found")
    input("Press enter to exit")
    exit()
try:
    import time
except:
    print("Time not found")
    print("Installing")
    subprocess.call[r"gengine\Installers\timeinstall.bat"]
    input("Press enter to restart and apply changes")
    exit()

try:
    import colorama
    from colorama import Fore,Back,Style
except:
    print("Colorama not found")
    print("Installing")
    subprocess.call[r"gengine\Installers\coloramainstall.bat"]
    input("Press enter to restart and apply changes")
    exit()

try:
    import os
except:
    print("OS not found")
    print("Installing")
    subprocess.call["gengine\Installers\osinstall.bat"]
    input("Press enter to restart and apply changes")
    exit()
try:
    import requests
except:
    #Messing around with colors
    print("\033[91m {}\033[00m".format("Request missing"))
    print("\033[92m {}\033[00m".format("Installing"))
    subprocess.call[r"genginge\Installers\requestinstall.bat"]
    input("Press enter to restart and apply chnges")
    exit()
try:
    import tkinter
    from tkinter import *
    from tkinter import messagebox
    
except:
        print("\033[91m {}\033[00m".format("404 Tkinter not found"))
        subprocess.call[r"gengine\Installers\tkinstall.bat"]
        
    
#Checks the version number and compares it to the version on GitHub
print('Checking version')

ver = b"0.0.2\n"
url = 'https://raw.githubusercontent.com/ItzFimes/ProjectG/main/test.txt'
try:
    r = requests.get(url)
    print(r.content)
except:
    print("Error 11001 No conection")
    internetcn = False
try:
    if r.content == ver:
        print("Version is up to date")
        print(r.content)
except:
    print("No internet")

filename = url.split('/')[-1]
print(filename)


#If the version is up-to-date it continues loading, if not it updates it. *FEATURE IN BETA*
if internetcn == True:
    if  r.content == ver:
        print("'Version is up to date")
    if r.content != ver:
        print("New version avivable would you like to download it?")
        print("Y/N")
        yndownload = input()
        if yndownload == "Y":
            print("Downloading")
            dwlink1 = "https://raw.githubusercontent.com/ItzFimes/ProjectG/main/G-engineNew.py"
            dw1 = requests.get(dwlink1)
            print("G-engine.exe sucessfully downloaded")
            filename = dwlink1.split('/')[-1]
            with open(filename,'wb') as output_file:
                output_file.write(dw1.content)
else:
    print("Skipped update check")
#Should display a loading screen - but it doesn't. It's only purpose right now is to notify the user that something is loading
l = Tk()

#Gets the current screen resolution and prints it to the console
screen_width = l.winfo_screenwidth()
screen_height = l.winfo_screenheight()
str_screen_height = str(screen_height)
str_screen_width = str(screen_width)
print(str_screen_height)
print(str_screen_width)
print(type(str_screen_height))
print(type(str_screen_width))

#Sets the resolution to previously defined values
l.geometry(str_screen_width + "x" + str_screen_height)
#Configures the loading screen's properties
l.config(background="#222222")
l.title("G-Engine - Loading")
l.iconbitmap("gengine\Logos\Logo_that_one_"
             "that_you_cant_see_in_fullscreen.ico")

#Should display a loading logo
loading_logo = PhotoImage(file = "gengine\Logos\Logo-destine.png")
Label1 = Label(l, wraplength = 230, fg="white",image=loading_logo,borderwidth=0,compound="center",highlightthickness = 0,padx=0,pady=0)
Label1.place(relx=0.5,rely=0.5, anchor="c")

#Exits the loading screen
def load_exit():
    l.destroy()

#Should display a continue button. Doesn't work. But it's okay because it would be annoying if it did :)
lbuttonIMG = PhotoImage(file="gengine\Buttons\continue_button.png")
lbutton = Button(l,text="",font=("Lucida console",20),command = load_exit,borderwidth=0,compound="center",highlightthickness = 0)
lbutton.config(image=lbuttonIMG)
lbutton.place(relx=0.5, rely=0.7, anchor="c")

#A piece of code that is useless but the rest of the code doesn't work if I delete it
#Checks if G-os is ready to download
print('Checking if G-OS is ready to download')

ready_url = 'https://raw.githubusercontent.com/ItzFimes/ProjectG/main/G-os/ready.txt'
try:
    ready_to_download_g_os = requests.get(ready_url)
    rtdwgos = ready_to_download_g_os.content
    print(ready_to_download_g_os.content)
except:
    print("Error 11001 No conection")

try:    
    if rtdwgos == b"0\n":
        print("Version is up to date")
        print(ready_to_download_g_os.content)
        #Lets the program know that a part of loading finished
        load_completed = True
except:
    print("No internet")
    # Lets the program know that a part of loading finished
    load_completed= True

#Yeah... Uhh... Idk what this part of the code does
load_loop = True

if load_completed == True:

    load_exit()
else:
    print("Not loaded yet")

l.mainloop()

#Old function. This used to show G-engine what apps are currently installed
def apps():
    print("Entering apps")
    appsinstalled= os.listdir(r"gengine\apps")
    print(appsinstalled)

#Shows the Gminal installer window. Used to manage Gminal installation
def gminal_installer():  # sourcery skip: ensure-file-closed

    gmin_install_dir_read = open(r"app_paths\gminal.gres", "r")
    gmin_install_dir_readq = gmin_install_dir_read.read()
    gmin_install_dir_read.close()

    def gminal_install_manager(hascrashed):
        if hascrashed == "1":
            messagebox.showerror("Runtime error", "Gminal couldn't start")
        else:
            print("OK :)")
        print("Gminal not installed/dir not found")
        m.withdraw()
        gmu = Tk()
        gmu.title("Gminal install manager")
        gmu.geometry(f"{str_screen_width}x{str_screen_height}")
        gmu.config(background="#222222")
        bing1img = PhotoImage(file=r"gengine/icons/install_gminal_centered.png", master=gmu)
        bing1 = Button(gmu, wraplength=230, borderwidth=0, compound="center", highlightthickness=0,image = bing1img)
        bing1.place(relx=0.25, rely=0.5, anchor="c")
        defpthgminimg = PhotoImage(file=r"gengine/icons/def_gmin_inst_path_new.png",master=gmu)
        defpthgmin = Button(gmu, wraplength=230, borderwidth=0, compound="center", highlightthickness=0,image = defpthgminimg)
        defpthgmin.place(relx=0.61, rely=0.5, anchor="c")
        uninsgminimg1 = PhotoImage(file=r"gengine/icons/uninstall_gminal.png",master=gmu)
        uninstgminb1 = Button(gmu, wraplength=230, borderwidth=0, compound="center", highlightthickness=0,image = uninsgminimg1)
        uninstgminb1.place(relx=0.40, rely=0.5, anchor="c")
        updatgminimg = PhotoImage(file=r"gengine/icons/updat_gmin.png",master=gmu)
        updatgmin = Button(gmu, wraplength=230, borderwidth=0, compound="center", highlightthickness=0,image = updatgminimg)
        updatgmin.place(relx=0.76, rely=0.5, anchor="c")
        def goback():
            m.deiconify()
            gmu.destroy()

        backbtnimg = PhotoImage(file=r"gengine/icons/back_arrow_100.50px.png",master=gmu)
        backbtn1 = Button(gmu, wraplength=230, borderwidth=0, compound="center", highlightthickness=0,image = backbtnimg,command=goback)
        backbtn1.place(relx=0.05, rely=0.9, anchor="c")

        def closeallgmu():
            try:
                m.deiconify()
                gmu.destroy()
            except:
                messagebox.showerror("Error on line 249",
                                     "An error occurred on line 249 in function 'm.destroy()': couldn't close 'm'")
                messagebox.showerror("Soluton, WoW so useful, so stonks, good soluton",
                                     "Please kill G-engine in taskmanager")

        gmu.protocol("WM_DELETE_WINDOW", closeallgmu)
        gmu.mainloop()
    if gmin_install_dir_readq == "0":

        gminal_install_manager("OK :)")
    else:
        print(f"gminal dir is: {gmin_install_dir_readq}")
        try:
            subprocess.call([gmin_install_dir_readq])
        except:
            gminal_install_manager("1")




m = Tk()
m.geometry(str_screen_width + "x" + str_screen_height)
m.title("G-engine")
m.config(background="#222222")
m.iconbitmap("gengine\Logos\Logo_that_one_that_you_cant_see_in_fullscreen_but_new.ico")





sidepanel = Frame(m,bg="#1E1E1E",bd="1",width=500,height=screen_height)
sidepanel.place(anchor="c",relx=0,rely=0.5)

full_store_ico = PhotoImage(file = r"gengine\icons\Store.png",master= m)
Label1 = Button(m, wraplength = 230,image=full_store_ico,borderwidth=0,compound="center",highlightthickness =0)
Label1.place(relx=0.04,rely=0.2, anchor="c")

full_app_ico = PhotoImage(file= r"gengine\icons\Library.png",master = m)
full_app_button_l = Button(m, wraplength=230, image=full_app_ico, borderwidth=0,compound="center", highlightthickness=0,command=apps)
full_app_button_l.place(relx=0.01,rely=0.25)

genginemain_ico = PhotoImage(file = f"gengine\icons\gengine_new.png",master = m)
Label3 = Label(m, wraplength = 230,image=genginemain_ico,borderwidth=0,compound="center",highlightthickness =0)
Label3.place(relx=0.06,rely=0.1, anchor="c")

loadimage = PhotoImage(file=f"gengine\icons\gminal_ico_forking_corners.png",master = m)
roundedbutton= Button(m, wraplength=230, image=loadimage, borderwidth=0,compound="center", highlightthickness=0, command=gminal_installer)
roundedbutton.place(relx=0.3, rely=0.3, anchor="c")

loadimage2 = PhotoImage(file=r"gengine\icons\nss_gengine_logo.png",master = m)
roundedbutton2= Button(m, wraplength=230, image=loadimage2, borderwidth=0,compound="center", highlightthickness=0)
roundedbutton2.place(relx=0.5, rely=0.3, anchor="c")

settingsimg1 = PhotoImage(file=r"gengine\icons\Settings.png")
settingsb1 = Button(m, wraplength = 230,image=settingsimg1,borderwidth=0,compound="center",highlightthickness =0)
settingsb1.place(relx=0.05, rely=0.9, anchor="c")
def closeall():
    try:
        m.destroy()
    except:
        messagebox.showerror("Error on line 249","An error occurred on line 249 in function 'm.destroy()': couldn't close 'm'")
        messagebox.showerror("Soluton, WoW so useful, so stonks, good soluton", "Please kill G-engine in taskmanager")

m.protocol("WM_DELETE_WINDOW", closeall)
m.mainloop()
