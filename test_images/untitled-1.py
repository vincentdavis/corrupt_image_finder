from PIL import Image
import os
import glob
import os
import EXIF
from datetime import datetime

print('starting')

#path = os.getcwd()
path = '/Volumes/Hafnium/Pictures'
#os.walk
#path = '/Users/vincentdavis/Dropbox/Camera Uploads'

#knowimagetypes = set(['.jpg', '.JPG', '.jpeg', '.tif', '.TIF', 'CR2'])

# Image types known to by supported by Python Image Library (incomplete)
pil_image_types = set(['.jpg', '.JPG', '.jpeg', '.tif', '.TIF'])
# Image types known to be supported by EXIF (incomplete)
exif_image_types = set(['.jpg', '.JPG', '.jpeg', '.tif', '.TIF', 'CR2'])
# File extentions that are known to be images. 
# This does not exclude that they may not be an image
# may not all be supported
know_image_types = set(['.tif'])

# Files extentions found
found_file_types = set([])
# File types found. Based on known file
found_image_types = set([])
# Posiible images, based on test_every=1 which tries exif and image.verify()
found_possible_images = set([])

# Defualt is to test pil_image_types and exif_image_types
testtypes = pil_image_types and exif_image_types
ingore = set([])
ignoretypes = knowfiletypes | ingore
unknowtypes = set([])

badlist = open('bad-image-list', 'w')
goodlist = open('good-image-list', 'w')
unknownlist = open('unknowtypes', 'w')

h_date = '> ' + str(datetime.now())+'\n'
h_root_path = '> ' + str(path)+'\n'
badlist.write(h_date)
badlist.write(h_root_path)
goodlist.write(h_date)
goodlist.write(h_root_path)
unknownlist.write(h_date)
unknownlist.write(h_root_path)

def pil_test(ifile):
        try:
                im = image.open(ifile)
                if im.verify() == None:
                        return True
                else:
                        return False
                
        except:
                return False
        
def exif_test(ifile):
        try:
                im = open(ifile, 'rb')
                tags = EXIF.process_file(im)
                tag_count = len(tags)
                return (True, tag_count) 
        except:
                return (False, None)
                        
def image_test(path = os.getcwd(),recursive = True, pil=True, exif=True, testtypes, find_all = False):
        '''
        path: the path to search and test
        recursive: search and test in all sub folder
        pil: test with using image.verify()
        exif: test with EXIF.proccess_file(image)
        testtypes: type of image files to test, based on file extention
        find_all: try pil and or exif tes on every file (image or not)
        '''
        for rpath, dirlist, filelist in os.walk(path):
                       for afile in filelist:
                #print(afile + " Type " + os.path.splitext(afile)[1])
                pil = 0
                exif = 0
        
                if os.path.splitext(afile)[1] in knowimagetypes:
                        ifile = os.path.join(rpath, afile)
                        print(ifile)
                        ok = 0
                        
                        pil_result = pil_test(ifile)
                                
                           
                        except:
                                print(verify)
                                badlist.write('PIL Failure - ' + ifile + '\n')
                            
                        #try:
                         #       print('pil - ' + str(len(im.info)))
                        #except:
                         #       pass
                            
                            
                        try:
                                im = open(ifile, 'rb')
                                tags = EXIF.process_file(im)
                                print('exif - ' + str(len(tags)))
                                exif = 1
                        except:
                                print('2oops')
                                
                        if len(tags) == 0 and pil == 1:
                                goodlist.write('EXIF # = ' +str(len(tags)) + ' | PIL = ' + str(verify) + '\n')
                                #'EXIF DateTimeOriginal'
                                goodlist.write(ifile + '\n')
                                
                        
            

     
badlist.close()
goodlist.close()
unknownlist.close()