# Im2ascii
A small python project that transforms images into ascii text

First of all import the package with:
```
pip install im2ascii
```
now import the package to your code:
```
import im2ascii
```
Now lets use it!

The only function is asciify, see:
```
im2ascii.asciify("/full/path/to/image.png")
```
This will return your image except it is typed in ascii characters!

### Aditional Parameters
There are only two aditional paramters for the function, square and invert. 
The square parameter makes sure your image is returned squared and not a rectangle. This is activated by default on the function, to deactivate it just use:
```
asciify('image.png', square=False)
```

The invert parameter invert the tones on the result of the image. like so:
For white tones, a '.' will be added, and for darker tones, a '@' will be the result. if you use ``invert=True``, this will be inverted.