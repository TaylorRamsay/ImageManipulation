import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

root = Tk()
root.geometry('1200x700')
root.title('Image Manipulator')
root.config(bg="skyblue")

buttonOneImg = PhotoImage(file=r"C:\\Users\\FSK8475\\Documents\\GitHub\\ImageManipulation\\lib\\Icons\\imageOne.png")
buttonTwoImg = PhotoImage(file=r"C:\\Users\\FSK8475\\Documents\\GitHub\\ImageManipulation\\lib\\Icons\\imageTwo.png")
images = [buttonOneImg, buttonTwoImg]


def addImage(k):

    path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg'), ("All Files", "*.*")])
    im = Image.open(path)
    images[k] = im
    im.thumbnail((250, 300))
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(openFile, image = tkimage)
    myvar.image = tkimage
    myvar.pack()


left_frame = Frame(root, width=400, height=690)
left_frame.grid(row=0, column=0, padx=10, pady=5)
left_frame.pack_propagate(False)
left_frame.grid_propagate(False)

#lSubFrame = Frame(left_frame, width=390, height=300, bg="black")
#left_subFrame.pack_propagate(False)
#lSubFrame.pack()

openFile = Button(left_frame, image=images[0], padx=10, pady=5, fg="white", bg="#263D42", command=lambda: addImage(0))
openFile.pack()

#lSubFrameTwo = Frame(left_frame, width=390, height=300, bg="red")
#lSubFrameTwo.pack()

openFileTwo = Button(left_frame, image=images[1], padx=10, pady=5, fg="white", bg="#263D42", command=lambda: addImage(1))
openFileTwo.pack()

#if os.path.isfile('save.txt'):
 #   with open('save.txt', 'r') as f:
  #      tempApps = f.read()
   #     apps = [x for x in tempApps if x.strip()]

#canvas = tk.Canvas(root, height=700, width=1200, bg="#263D42")
#canvas.pack()

#frame = tk.Frame(root, bg="white")
#frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


root.mainloop()


#for app in apps:
    #label = tk.Label(frame, text=app)
    #label.pack()

#with open('save.txt', 'w') as f:
 #   for app in apps:
  #      f.write(app + ',')