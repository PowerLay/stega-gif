from PIL import Image, ImageDraw, ImageSequence
from random import randint
import io


def stega_encrypt():

    keys = []  # сюда будут помещены ключи
    frames = []  # массив кадров
    # создаём объект изображения
    img = Image.open(input("path to image: "))  # создаём объект изображения
    width = img.size[0]  # ширина
    height = img.size[1]  # высота
    f = open('keys.txt', 'w')  # текстовый файл для ключей

    for frame in ImageSequence.Iterator(img):
        b = io.BytesIO()
        frame.save(b, format="GIF")
        frame = Image.open(b)
        frames.append(frame)

    for elem in ([ord(elem) for elem in input("text here: ")]):
        coords = (randint(1, width-10), randint(1, height-10))
        frame_id = randint(1, img.n_frames-1)

        img.seek(frame_id)

        pix = img.load()  # все пиксели тут
        draw = ImageDraw.Draw(frames[frame_id])  # объект рисования

        g, b = pix[coords][1:3]
        draw.point(coords, (elem, g, b))

        b = io.BytesIO()
        frames[frame_id].save(b, format="GIF")
        frame = Image.open(b)
        frames[frame_id] = frame

        f.write(str(frame_id) + " " + str(coords)+'\n')

    print('keys were written to the keys.txt file')
    frames[0].save('newimage.gif', save_all=True, append_images=frames[1:])
    f.close()


stega_encrypt()
