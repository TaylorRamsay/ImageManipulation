from PIL import Image
import glob, os

def verticalCuts(imageOne, imageTwo):

    imageOne = Image.open("C:\\Users\\FSK8475\\Documents\\ImageManipProgram\\blueFractal.jpg")
    imageTwo = Image.open("C:\\Users\\FSK8475\\Documents\\ImageManipProgram\\weaver.jpg")

    strip_height = imageOne.height
    position = 0

    print(imageOne.format, imageOne.size, imageOne.mode)
    print(imageTwo.format, imageTwo.size, imageTwo.mode)


    for x in range(imageTwo.width):
        cut_region = (position, 0, position + 1, strip_height)
        cut = imageOne.crop(cut_region)
        position += 2
        imageTwo.paste(cut, (position, 0))

    print(position)
    imageTwo.save("C:\\Users\\FSK8475\\Documents\\ImageManipProgram\\test.jpg")