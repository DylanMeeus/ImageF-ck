# ImageFuck

Imagefuck is a 'graphical' esolang based on Brainfuck. Instead of normal source code, the source code for ImageFuck is an image.
The pixel colours in the image make up the source, which ImageFuck can interpret as it would with normal Brainfuck code.

A more complete description can be found on [esolangs](https://www.esolangs.org/wiki/ImageFuck).

The interpret is written in Python 3 and makes use of the Python Image Library (PIL).
If you do not have PIL installed it is a simple matter of running `pip install pillow`.

Once installed you can run the program to interpret an image using `python ImageFck -i image.png`.
You can create an image from existing Brainfuck code as well by using `python ImageFck -s source.bf`.

In the examples folder you can find some images which you can use to test the program.

When creating an image for use with Imagefuck, you need to make sure you use a file format that does not deteriorate the image quality. For this I recommend either PNG or BMP.

## 'Writing' ImageFuck code
To create source code for ImageFuck, all you need is to create an image in your favourite image creation program. The only requirement is that it is saved in a file format that is lossless such as PNG.

In ImageFuck, the colour of a pixel corresponds to a specific Brainfuck instruction. The colours that are not in the table below are ignored (as are other symbols in brainfuck). To create 'comments', one would have to write something on the image indicative of a comment.

| Colour (RGB) | Brainfuck |
----------------------------
| (255,0,0)    | > |
| (0,255,0)    | . |
| (0,0,255)    | < |
| (255,255,0)  | + |
| (0,255,255)  | - |
| (255,0,188)  | [ |
| (255,128,0)  | ] |
| (102,0,204)  | , |


## Imagefuck - Brainfuck Interpreter

The interpret is actually a normal Brainfuck interpreter. All the image-code gets translated to normal brainfuck code, which is then fed to the Brainfuck interpreter that this contains.
The brainfuck interpreter can at the moment not be used as a stand-alone interpreter but I'll end up changing the source later so this can be done as well if so desired. Though there are numerous other brainfuck interpreters out there. Personally, I recommend `beef`. 

