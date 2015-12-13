from PIL import Image
import os
import glob
import os
import EXIF
import sys
from datetime import datetime

test_image_types = set(['.jpg', '.JPG', '.jpeg', '.tif', '.TIF', 'PSD'])
find_all = True
pil = True

#path = os.getcwd()
#path = os.getcwd()+"/images"
path = '/Volumes/Hafnium/'
#path= '/Volumes/Photo work/'
#path = '/Volumes/home/Photos/recovered'

total_files = 0
for rpath, dirlist, filelist in os.walk(path):
    '''
 walk the directory getting file names.
 Walk returs lists of file in each directory
 '''
    for afile in filelist:
        if os.path.splitext(afile)[1] in test_image_types or find_all==True: #check if file type is to be tested'
            ifile = os.path.join(rpath, afile) #get full file path
            total_files += 1 #keep a count of the files
            #print('file number ' + str(total_files) + ' is ' + afile)
            if pil == True: #Check pil option
                def piltest(ifile):
                    try:
                        im = Image.open(ifile)
                        try:
                            print(im.verify())
                            return True
                        except:
                            print('Pil.Image.verify() failed: ' + afile + 'File number ' + str(total_files))
                            return False
                    except OverflowError:
                        print('Python int too large to convert to C long: Is this a PSD file: ' + afile)                            
                        return False
                    except IOError:
                        #print('PIL cannot identify image file: ' + afile + 'File number ' + str(total_files))
                        #testlog.write('> PIL cannot identify image file \n')
                        #testlog.write('>' + ifile + '\n')
                        return None
                    except:
                        print(ifile)
                        print("Unexpected error doing PIL.Image.open():", sys.exc_info()[0]  + 'File number ' + str(total_files))
                        raise
                result = piltest(ifile)
                if result==False: print(str(result) + ' Pil Fail ' + ifile + ' : ' + str(total_files))
            #EXIF test
            def exiftest(ifile):
                try:
                    im = open(ifile, 'rb')
                    tags = EXIF.process_file(im)
                    tag_count = len(tags)
                    try:
                        anydate = any([True for i in tags if 'Date' in i])
                    except:
                        anydate = None 
                    return (True, tag_count, anydate) 
                except:
                    return (False, None, None)                         
            result = exiftest(ifile)
            if (total_files%50)==0: print(str(result), total_files, ifile)
            if not(result[0]): print(result[0], ifile)
            
print('Done!')