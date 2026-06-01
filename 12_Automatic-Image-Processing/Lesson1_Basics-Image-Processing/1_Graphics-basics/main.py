from PIL import Image
from PIL import ImageFilter
# for bonus task:
from PIL import ImageEnhance

# fix if the image cannot be found even if it is in the same folder as the script
# this happens when the terminal does not point specifically to the folder where the script is located, but to a parent folder
from pathlib import Path
script_dir = Path(__file__).resolve().parent

with Image.open(script_dir / 'original.jpg') as pic_original:
    print('Image is open\nSize:', pic_original.size)
    print('Format:', pic_original.format)
    print('Type:', pic_original.mode) # цветное, colored
    pic_original.show()

    pic_gray = pic_original.convert('L') 
    pic_gray.save(script_dir / 'gray.jpg')
    print('Image is created\nSize:', pic_gray.size)
    print('Format:', pic_gray.format)
    print('Type:', pic_gray.mode) # bw
    pic_gray.show()

    pic_blured = pic_original.filter(ImageFilter.BLUR)
    # use pic_blured.save('blured.jpg') if terminal points to the folder where the script is located
    pic_blured.save(script_dir / 'blured.jpg') 
    pic_blured.show()

    pic_up = pic_original.transpose(Image.ROTATE_180)
    # use pic_blured.save('up.jpg') if terminal points to the folder where the script is located
    pic_up.save(script_dir / 'up.jpg')
    pic_up.show()

    # Bonus 1: Mirror reflection
    pic_mirrow = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    # use pic_blured.save('mirrow.jpg') if terminal points to the folder where the script is located
    pic_mirrow.save(script_dir / 'mirrow.jpg')
    pic_mirrow.show()

    # Bonus 2: Contrast enhancing
    pic_contrast = ImageEnhance.Contrast(pic_original)
    # use pic_contrast.save('contr.jpg') if terminal points to the folder where the script is located
    pic_contrast.save(script_dir / 'contr.jpg')
    pic_contrast.show()