import  tkinter as tk
from tkinter import CENTER, filedialog, Text
import os

from matplotlib.pyplot import gray #allows us to open apps

#ARRAY OF APPS
apps = []
counter = 0

if os.path.isfile('save.txt'):
        with open('save.txt', 'r') as f:
                tempApps = f.read()
                tempApps = tempApps.split(',')
                apps = [x for x in tempApps if x.strip()]

def addApp():
    filename = filedialog.askopenfilename(initialdir="/", title= "Select File",
    filetypes=(("executables", "*exe"), ("all files", "*.*")))

    apps.append(filename)
    counter = len(apps)
    for app in apps:
        if counter > 1:
                counter = counter - 1

        else:
                label = tk.Label(frame, text=app, bg="gray")
                label.pack()
                counter = counter + 1

def runApp():
    for app in apps:
        os.startfile(app)



#-------------------------------------SCREEEN----------------------------------------------

root = tk.Tk()

canvas = tk.Canvas(root, height=600, width= 500, bg="#7c27f4")
canvas.pack()

frame = tk.Frame(root, bg = "#f9f4f4")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

openFile = tk.Button( root, text="Open", padx=10, pady=5, fg="white",
        bg="#7c27f4", command=addApp ) #addApp function to add the app on the workflow
openFile.pack()

runApp = tk.Button( root, text="Run", padx=10, pady=5, fg="white",
        bg="#7c27f4", command=runApp ) #addApp function to add the app on the workflow
runApp.pack()


root.mainloop()


#-------------------------------------SCREEEN----------------------------------------------


#-----------Generating the main file to store your daily apps-----------------------
with open('save.txt', 'w') as f:
        for app in apps:
                f.write(app + ',')