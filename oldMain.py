import tkinter as tk
from tkinter import *
from tkinter import filedialog
from turtle import width
from PIL import Image, ImageTk
import os, copy

from numpy import save, typename

class ImageManipulator(Frame):
    def initWidgets(self):
        self.leftFrame = Frame(self, width=400, height=690)
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)
        self.left_frame.pack_propagate(False)
        self.left_frame.rid_propagate(False)


root = Tk()
root.geometry('1200x700')
root.title('Image Manipulator')
root.config(bg="skyblue")


buttonOneImg = PhotoImage(file=r"C:\\Users\\FSK8475\\Documents\\GitHub\\ImageManipulation\\lib\\Icons\\imageOne.png")
buttonTwoImg = PhotoImage(file=r"C:\\Users\\FSK8475\\Documents\\GitHub\\ImageManipulation\\lib\\Icons\\imageTwo.png")
images = [buttonOneImg, buttonTwoImg]


def addImageOne(k):

    path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg'), ("All Files", "*.*")])
    im = Image.open(path)
    cop = copy.deepcopy(im)
    images[k] = cop
    im.thumbnail((250, 300))
    tkimage = ImageTk.PhotoImage(im)
    openFile.image=im
    #myvar=Label(openFile, image = tkimage)
    #myvar.image = tkimage
    #myvar.pack()

def addImageTwo(k):

    path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg'), ("All Files", "*.*")])
    im = Image.open(path)
    cop = copy.deepcopy(im)
    images[k] = cop
    im.thumbnail((250, 300))
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(openFileTwo, image = tkimage)
    myvar.image = tkimage
    myvar.pack()

def verticalCuts():

    strip_height = images[0].height
    position = 0

    print(images[0].format, images[0].size, images[0].mode)
    print(images[1].format, images[1].size, images[1].mode)

    for x in range(images[1].width):
        cut_region = (position, 0, position + 1, strip_height)
        cut = images[0].crop(cut_region)
        position += 2
        images[1].paste(cut, (position, 0))

    print(position)
    thumb = copy.deepcopy(images[1])
    thumb.thumbnail((500, 500))
    tkimage= ImageTk.PhotoImage(thumb)
    myvar=Label(middle_frame, image=tkimage)
    myvar.image = tkimage
    myvar.pack()
    images[1].save("C:\\Users\\FSK8475\\Documents\\GitHub\\ImageManipulation\\lib\\Icons\\Processed\\test.jpg")

def saveFile():
    f = filedialog.asksaveasfile(mode='w', defaultextension='*.jpg*')
    images[1].save(f)


left_frame = Frame(root, width=400, height=690)
left_frame.grid(row=0, column=0, padx=10, pady=5)
left_frame.pack_propagate(False)
left_frame.grid_propagate(False)

middle_frame = Frame(root, width= 750, height=690)
middle_frame.grid(row=0, column=1, padx=10, pady=5)
middle_frame.pack_propagate(False)
middle_frame.grid_propagate(False)

openFile = Button(left_frame, image=images[0], padx=10, pady=5, fg="white", bg="#263D42", command=lambda: addImageOne(0))
openFile.pack()

openFileTwo = Button(left_frame, image=images[1], padx=10, pady=5, fg="white", bg="#263D42", command=lambda: addImageTwo(1))
openFileTwo.pack()

process = Button(middle_frame, text="PROCESS", padx=10, pady=5, fg="white", bg="#263D42", command=verticalCuts)
process.pack()

save = Button(middle_frame, text="SAVE", padx=10, pady=5, fg="white", bg="#263D42", command=saveFile)
save.pack()


root.mainloop()
