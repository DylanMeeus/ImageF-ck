""" Interpreter for visual brainfuck. Executes an image as brainfuck instructions """

import sys,math
from PIL import Image
from Brainfck import Brainfck



global colour_to_bf

class ImageCreator:
    """ turn a brainfuck program into an image """
    def __init__(self):
        pass

    def create_image(self,source):
        """ Creates ImageFkc source based on BrainF*ck source """
        # use the map in reverse
        global colour_to_bf
        bf_to_colour = dict((v,k) for k,v in list(colour_to_bf.items()))
        # read the source file
        file = open(source,'r')
        content = file.read()
        colours = []
        for char in content:
            if char in bf_to_colour:
                colours.append(bf_to_colour[char])

        # push the colours to an image
        size = int(math.sqrt(len(colours)))+1
        image = Image.new('RGB',(size,size))
        image.putdata(colours)
        image.save(source+'.png')


class Interpreter:
    """ interprets the image """

    def __init__(self, file):
        global colour_to_bf
        bf = self.read_pixels_as_brainfuck(file)
        bfi = Brainfck.Interpreter(bf)
        bfi.interpret()
        print(bf)


    def read_pixels_as_brainfuck(self,file):
        global colour_to_bf
        image = Image.open(file)
        brainfuck = ''
        pixels = image.load()
        for r in range(image.size[0]):
            for c in range(image.size[1]):
               if pixels[c,r] in colour_to_bf:
                   brainfuck += colour_to_bf[pixels[c,r]]
               else:
                   pass # we don't care about any other colours
        return brainfuck




if __name__ == '__main__':
    global colour_to_bf

    # create the colour set that we will use
    # red              #green           #blue           # yellow
    colour_to_bf = {(255,0,0) : '>', (0,255,0) : '.', (0,0,255) : '<', (255,255,0) : '+'
        , (0,255,255) : '-', (255,0,188) : '[', (255,128,0) : ']', (102,0,204) : ','}
    # cyan            # pink            #orange              #purple

    if len(sys.argv) <= 1:
        print("need to pass a file to interpret!")
        exit()

    if(sys.argv[1] == '-i'):
        print("interpreting file.." + sys.argv[2])
        i = Interpreter(sys.argv[2])
    elif(sys.argv[1] == '-s'):
        print("translating source to image..")
        ic = ImageCreator()
        ic.create_image(sys.argv[2])