from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import copy

class ImageManipulator(Frame):

    __root = Tk()
    __root.geometry('1200x800')
    __root.title('Image Manipulator')
    __root.config(bg="skyblue")
    __buttonOneImg = PhotoImage(file=r"C:\\Users\\CDK345\\Documents\\GitHub\\ImageManipulation\\lib\\Icons\\imageOne.png")
    __processedImg = PhotoImage(file=r"C:\\Users\\CDK345\\Documents\\GitHub\\ImageManipulation\\lib\\Icons\\imageTwo.png")
    __images = [__buttonOneImg, __buttonTwoImg, __processedImg]

    def initFrames(self):
        self.left_frame = Frame(self.__root, width=400, height=790)
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)
        self.left_frame.pack_propagate(False)
        self.left_frame.grid_propagate(False)

        self.middle_frame = Frame(self.__root, width= 750, height=790)
        self.middle_frame.grid(row=0, column=1, padx=10, pady=5)
        self.middle_frame.pack_propagate(False)
        self.middle_frame.grid_propagate(False)

    def initButtons(self):
        self.imgOne = Label(self.left_frame, image=self.__images[0])
        self.imgOne.grid(row=0, column=0, padx=2, pady=5)

        self.openFile = Button(self.left_frame, text="Select Image One", padx=10, pady=5, fg="white", bg="#263D42", command=lambda: self.addImageOne(0))
        self.openFile.grid(row=1, column=0)

        self.imgTwo = Label(self.left_frame, image=self.__images[1])
        self.imgTwo.grid(row=2, column=0, padx=2, pady=5)

        self.openFileTwo = Button(self.left_frame, text="Select Image Two", padx=10, pady=5, fg="white", bg="#263D42", command=lambda: self.addImageTwo(1))
        self.openFileTwo.grid(row=3, column=0)

        self.processedImg = Label(self.middle_frame, image=self.__images[2], pady=5)
        self.processedImg.pack()

        self.process = Button(self.middle_frame, text="PROCESS", padx=10, pady=5, fg="white", bg="#263D42", command=self.verticalCuts)
        self.process.pack()

        self.save = Button(self.middle_frame, text="SAVE", padx=10, pady=5, fg="white", bg="#263D42", command=self.saveFile)
        self.save.pack()

    def addImageOne(self, k):
        path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg'), ("All Files", "*.*")])
        im = Image.open(path)
        cop = copy.deepcopy(im)
        self.__images[k] = cop
        im.thumbnail((390, 300))
        tkimage = ImageTk.PhotoImage(im)
        self.openFile.image=im
        self.imgOne.configure(image=tkimage)
        self.imgOne.image=tkimage
        self.imgOne.grid(row=0, column=0)

    def addImageTwo(self, k):
        path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg'), ("All Files", "*.*")])
        im = Image.open(path)
        cop = copy.deepcopy(im)
        self.__images[k] = cop
        im.thumbnail((390, 300))
        tkimage = ImageTk.PhotoImage(im)
        self.imgTwo.configure(image=tkimage)
        self.imgTwo.image=tkimage
        self.imgTwo.grid(row=2, column=0)

    def process(self):
        resizedImg = self.processedImg.resize((self.__images[0].width, self.__images[0].height))

    def verticalCuts(self):
        strip_height = self.__images[0].height
        position = 0
        self.__images[2] = Image.new(self.__images[0].mode, (self.__images[0].width, self.__images[0].height), color=0)

        print(self.__images[0].format, self.__images[0].size, self.__images[0].mode)
        print(self.__images[1].format, self.__images[1].size, self.__images[1].mode)

        for x in range(self.__images[0].width):
            if x % 2 == 0:
                cut_region = (position, 0, position + 1, strip_height)
                cut = self.__images[0].crop(cut_region)
                self.__images[2].paste(cut, (position, 0))
            else:
                cut_region = (position, 0, position + 1, strip_height)
                cut = self.__images[1].crop(cut_region)
                self.__images[2].paste(cut, (position, 0))

            position += 1

        print(position)
        thumb = copy.deepcopy(self.__images[2])
        thumb.thumbnail((500, 500))
        tkimage= ImageTk.PhotoImage(thumb)
        self.processedImg.configure(image=tkimage)
        self.processedImg.image=tkimage
        self.processedImg.pack()
        self.__images[2].save("C:\\Users\\CDK345\\Documents\\GitHub\\ImageManipulation\\lib\\Icons\\Processed\\test.jpg")

    def saveFile(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension='*.jpg*')
        self.__images[2].save(f)

    def __init__(self, master=__root):
        Frame.__init__(self, master)
        self.grid()
        self.initFrames()
        self.initButtons()

img = ImageManipulator()
img.mainloop()