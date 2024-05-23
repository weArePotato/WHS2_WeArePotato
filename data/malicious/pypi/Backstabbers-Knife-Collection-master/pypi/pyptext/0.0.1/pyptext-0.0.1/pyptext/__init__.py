#A WAYY simpler version of asciify made by Rafael Rayes
# Requires Pilow
def asciify(path, invert=False, square=True):
    from PIL import Image
    ASCII_CHARS = ['.',',',':',';','+','*','?','%','S','#','@']
    if invert == False:
        ASCII_CHARS = ASCII_CHARS[::-1]
    result = []
    im = Image.open(str(path))
    im = im.convert('L')
    im = im.resize((50, 50))
    for i in range(50):
        for j in range(50):
            pixel = im.getpixel((i, j))
            result.append(ASCII_CHARS[(round(pixel/25))])
            if square == True:
                result.append(' ')
        result.append('\n')
    return ''.join(result)
