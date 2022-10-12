import uuid
import os
from PIL import Image
import glob,os,shutil

def generate_unqiue_id(folder_path):
    uid = uuid.uuid4().hex+'.jpg'
    new_filename = os.path.join(folder_path,uid)
    return new_filename, uid

def fileter_dataset(filename):
    file_kb_sz = os.stat(filename).st_size / 1024
    # if flag is true, then move file to trash folder
    flag = False

    if file_kb_sz < 5:
        print(f'File Size is less than 5kb. File size is {file_kb_sz}.')
        flag = True

    with Image.open(filename) as img:
        width, height = img.size
        img_min = min(width, height)
        if img_min < 200:
            print('img_min(width,height) is less than 200.')
            flag = True
        if width < height:
            width, height = height, width
        if width / height > 3.0:
            print('Aspect ratio is greater than 3.0.')
            flag = True

    return flag

def generate_label(path):
    im =Image.open(glob.glob(os.path.join(path,'*.jpg'))[0])
    im.show()
    brand = input('What is brand of shoes? ')
    name = input('What is name of shoes? ')
    upper = input('What are the characteristics of the upper? ')
    midsole = input('What is the color of the midsole? ')
    outsole = input('What is the color of the outsole? ')
    toebox = input('What are the characteristics of the toebox? ')
    tongue = input('What are the characteristics of the tongue? ')
    heeltap = input('What is the color of the heeltap? ')
    top = input('Is it low top or high top? ')
    shoelace = input('What is the color of the shoelace? ')
    label = f'brand is {brand}, name is {name}, upper is {upper}, midsole is {midsole},' \
            f'outsole is {outsole}, toebox is {toebox}, tongue is {tongue}, heeltap is {heeltap},' \
            f'top is {top}, shoelace is {shoelace}.'
    print(f'label is {label}')
    return label