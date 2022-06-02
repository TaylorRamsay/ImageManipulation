import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.geometry('1200x700')
root.title('Image Manipulator')
root.config(bg="skyblue")
apps = []

left_frame = Frame(root, width=200, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)

#if os.path.isfile('save.txt'):
 #   with open('save.txt', 'r') as f:
  #      tempApps = f.read()
   #     apps = [x for x in tempApps if x.strip()]

def addImage():

    path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])
    im = Image.open(path)
    im.thumbnail((250, 250))
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(left_frame,image = tkimage)
    myvar.image = tkimage
    myvar.pack()


#canvas = tk.Canvas(root, height=700, width=1200, bg="#263D42")
#canvas.pack()

#frame = tk.Frame(root, bg="white")
#frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(left_frame, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addImage)
openFile.pack()

root.mainloop()


#for app in apps:
    #label = tk.Label(frame, text=app)
    #label.pack()

#with open('save.txt', 'w') as f:
 #   for app in apps:
  #      f.write(app + ',')