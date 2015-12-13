from PIL import Image
import os
import glob
import os
import EXIF
import sys
from datetime import datetime

def piltest(image):
    try:
        im = Image.open(ifile)
        try:
            print(im.verify())
            pass
        except:
            print('Pil.Image.verify() failed: ' + afile + 'File number ' + str(total_files))
        except OverflowError:
            print('Python int too large to convert to C long: Is this a PSD file: ' + afile)                            
        except IOError:
            print('PIL cannot identify image file: ' + afile + 'File number ' + str(total_files))
            testlog.write('> PIL cannot identify image file \n')
            testlog.write('>' + ifile + '\n')
            pass
        except:
            print(ifile)
            print("Unexpected error doing PIL.Image.open():", sys.exc_info()[0]  + 'File number ' + str(total_files))
            raise