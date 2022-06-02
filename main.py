import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.geometry('1200x700')
root.title('Image Manipulator')
root.config(bg="skyblue")
images = []

left_frame = Frame(root, width=400, height=690)
left_frame.grid(row=0, column=0, padx=10, pady=5)
left_frame.pack_propagate(False)
left_frame.grid_propagate(False)

left_subFrame = Frame(left_frame, width=390, height=300, bg="black")
#left_subFrame.pack_propagate(False)
left_subFrame.pack()

#if os.path.isfile('save.txt'):
 #   with open('save.txt', 'r') as f:
  #      tempApps = f.read()
   #     apps = [x for x in tempApps if x.strip()]

def addImage():

    path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])
    im = Image.open(path)
    images.append(im)
    im.thumbnail((250, 300))
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(left_subFrame,image = tkimage)
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