# ImageFuck

Imagefuck is a 'graphical' esolang based on Brainfuck. Instead of normal source code, the source code for ImageFuck is an image.
The pixel colours in the image make up the source, which ImageFuck can interpret as it would with normal Brainfuck code.

A more complete description can be found on (esolangs)[https://www.esolangs.org/wiki/ImageFuck].

The interpret is written in Python 3 and makes use of the Python Image Library (PIL).
If you do not have PIL installed it is a simple matter of running `pip install pillow`.

Once installed you can run the program to interpret an image using `python ImageFck -i image.png`.
You can create an image from existing Brainfuck code as well by using `python ImageFck -s source.bf`.

In the examples folder you can find some images which you can use to test the program.

When creating an image for use with Imagefuck, you need to make sure you use a file format that does not deteriorate the image quality. For this I recommend either PNG or BMP.




