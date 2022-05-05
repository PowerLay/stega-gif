from PIL import Image
from re import findall


def stega_decrypt():

    a = []
    keys = []
    img = Image.open(input("path to image: "))
    f = open(input('path to keys: '), 'r')
    y = str([line.strip() for line in f])

    for i in range(len(findall(r'\d+\s\((\d+)\,', y))):
        coords = (
            (
                int(findall(r'\((\d+)\,', y)[i]),
                int(findall(r'\,\s(\d+)\)', y)[i])
            )
        )
        frame = int(findall(r'(\d+)\s\(', y)[i])
        keys.append((frame, coords))

    for key in keys:
        print(key)

        frame, coords = key
        img.seek(frame)
        pix = img.load()
        a.append(pix[coords][0])

    return ''.join([chr(elem) for elem in a])


print("you message: ", stega_decrypt())
