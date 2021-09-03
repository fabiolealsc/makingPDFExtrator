from tkinter import *
from PIL import Image, ImageTk


def display_logo(url, row, column):
    img = Image.open(url)
    img = img.resize((int(img.size[0]/1.5), int(img.size[1]/1.5)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg='white')
    img_label.image = img
    img_label.grid(column=column, row=row, rowspan=2, sticky=NW, padx=20, pady=40)


def display_icon(url, row, column, stick):
    icon = Image.open(url)
    icon = icon.resize((20, 20))
    icon = ImageTk.PhotoImage(icon)
    icon_label = Button(image=icon, width=25, height=25)
    icon_label.image = icon
    icon_label.grid(column=column, row=row, sticky=stick)


def display_textbox(content, ro, col, root):
    text_box = Text(root, height=10, width=30, padx=10, pady=10)
    text_box.insert(1.0, content)
    text_box.tag_configure('center', justify='center')
    text_box.tag_add('center', 1.0, 'end')
    text_box.grid(column=col, row=ro, sticky=SW, padx=25, pady=25)


def extract_images(page):
    images = []
    if '/XObject' in page['/Resources']:
        xObject = page['/Resources']['/XObject'].getObject()

        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                size = xObject[obj]['/Width'], xObject[obj]['/Height']
                data = xObject[obj].getData()
                mode = ''
                if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                    mode = 'RGB'
                else:
                    mode = 'CMYK'
                img = Image.frombytes(mode, size, data)
                images.append(img)
    return images