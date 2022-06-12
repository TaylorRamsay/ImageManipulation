import tkinter as tk
from tkinter import *
from tkinter import filedialog
from turtle import width
from PIL import Image, ImageTk
import os, copy

from numpy import save, typename

class ImageManipulator(Frame):

    __root = Tk()
    __root.geometry('1200x700')
    __root.title('Image Manipulator')
    __root.config(bg="skyblue")
    __buttonOneImg = PhotoImage(file=r"C:\\Users\\FSK8475\\Documents\\GitHub\\ImageManipulation\\lib\\Icons\\imageOne.png")
    __buttonTwoImg = PhotoImage(file=r"C:\\Users\\FSK8475\\Documents\\GitHub\\ImageManipulation\\lib\\Icons\\imageTwo.png")
    __images = [__buttonOneImg, __buttonTwoImg]

    def initFrames(self):
        self.left_frame = Frame(self.__root, width=400, height=690)
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)
        self.left_frame.pack_propagate(False)
        self.left_frame.grid_propagate(False)

        self.middle_frame = Frame(self.__root, width= 750, height=690)
        self.middle_frame.grid(row=0, column=1, padx=10, pady=5)
        self.middle_frame.pack_propagate(False)
        self.middle_frame.grid_propagate(False)


    def initButtons(self):
        self.openFile = Button(self.left_frame, image=self.__images[0], padx=10, pady=5, fg="white", bg="#263D42", command=lambda: self.addImageOne(0))
        self.openFile.pack()

        self.openFileTwo = Button(self.left_frame, image=self.__images[1], padx=10, pady=5, fg="white", bg="#263D42", command=lambda: self.addImageTwo(1))
        self.openFileTwo.pack()

        self.process = Button(self.middle_frame, text="PROCESS", padx=10, pady=5, fg="white", bg="#263D42", command=self.verticalCuts)
        self.process.pack()

        self.save = Button(self.middle_frame, text="SAVE", padx=10, pady=5, fg="white", bg="#263D42", command=self.saveFile)
        self.save.pack()

    def addImageOne(self, k):

        path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg'), ("All Files", "*.*")])
        im = Image.open(path)
        cop = copy.deepcopy(im)
        self.__images[k] = cop
        im.thumbnail((250, 300))
        tkimage = ImageTk.PhotoImage(im)
        #self.openFile.image=im
        myvar=Label(self.openFile, image = tkimage)
        myvar.image = tkimage
        myvar.pack()

    def addImageTwo(self, k):

        path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg'), ("All Files", "*.*")])
        im = Image.open(path)
        cop = copy.deepcopy(im)
        self.__images[k] = cop
        im.thumbnail((250, 300))
        tkimage = ImageTk.PhotoImage(im)
        myvar=Label(self.openFileTwo, image = tkimage)
        myvar.image = tkimage
        myvar.pack()

    def verticalCuts(self):

        strip_height = self.__images[0].height
        position = 0

        print(self.__images[0].format, self.__images[0].size, self.__images[0].mode)
        print(self.__images[1].format, self.__images[1].size, self.__images[1].mode)

        for x in range(self.__images[1].width):
            cut_region = (position, 0, position + 1, strip_height)
            cut = self.__images[0].crop(cut_region)
            position += 2
            self.__images[1].paste(cut, (position, 0))

        print(position)
        thumb = copy.deepcopy(self.__images[1])
        thumb.thumbnail((500, 500))
        tkimage= ImageTk.PhotoImage(thumb)
        myvar=Label(self.middle_frame, image=tkimage)
        myvar.image = tkimage
        myvar.pack()
        self.__images[1].save("C:\\Users\\FSK8475\\Documents\\GitHub\\ImageManipulation\\lib\\Icons\\Processed\\test.jpg")

    def saveFile(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension='*.jpg*')
        self.__images[1].save(f)

    def __init__(self, master=__root):
        Frame.__init__(self, master)
        self.grid()
        self.initFrames()
        self.initButtons()

img = ImageManipulator()
img.mainloop()