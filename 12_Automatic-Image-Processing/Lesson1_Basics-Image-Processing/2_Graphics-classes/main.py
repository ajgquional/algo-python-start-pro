from PIL import Image
from PIL import ImageFilter

# fix if the image cannot be found even if it is in the same folder as the script
# this happens when the terminal does not point specifically to the folder where the script is located, but to a parent folder
from pathlib import Path
script_dir = Path(__file__).resolve().parent

class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = list()

    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print('File not found!')
        self.original.show()

    def do_left(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)

        # Bonus: Automatic naming for edited images
        # Original (kept for reference):
        # temp_filename = self.filename.split('.')
        # new_filename = temp_filename[0] + str(len(self.changed)) + '.jpg'
        p = Path(self.filename)
        new_filename = f"{p.stem}{len(self.changed)}{p.suffix}"

        # use rotated.save(new_filename) if terminal points to the folder where the script is located
        rotated.save(script_dir / new_filename)

    # Bonus: Crop the image of baby koala
    def do_cropped(self):
        box = (250, 100, 600, 400) #left, up, right, down
        cropped = self.original.crop(box)
        self.changed.append(cropped)

        # Bonus: Automatic naming for edited images
        # Original (kept for reference):
        # temp_filename = self.filename.split('.')
        # new_filename = temp_filename[0] + str(len(self.changed)) + '.jpg'
        p = Path(self.filename)
        new_filename = f"{p.stem}{len(self.changed)}{p.suffix}"

        # use cropped.save(new_filename) if terminal points to the folder where the script is located
        cropped.save(script_dir / new_filename)


# use MyImage.save('original.jpg') if terminal points to the folder where the script is located
MyImage = ImageEditor(script_dir / 'original.jpg')
MyImage.open()

MyImage.do_left()
MyImage.do_cropped()

for im in MyImage.changed:
    im.show()
