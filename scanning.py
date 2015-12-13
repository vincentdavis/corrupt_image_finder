from image_tests import pil_verify, exif_test
import os
import EXIF
import sys
from datetime import datetime

def get_file_extensions(path, length):
    ftypes = set([])
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            ext = os.path.splitext(name)[1].lower()
            if len(ext) <= length and not ext in ftypes:
                ftypes.add(ext)
                print(ext)
    print("The number of extensions is: " + str(len(ftypes)))
    print(ftypes)
    return ftypes


def image_scanner(path, types={'.jpg', '.jpeg', '.tif'}):
    total_files = 0
    for rpath, dirlist, filelist in os.walk(path):
        '''
        walk the directory getting file names.
        Walk returns a lists of file in each directory
        '''
        for afile in filelist:
            if os.path.splitext(afile)[1].lower() in types and not afile.startswith('.'):
                ifile = os.path.join(rpath, afile) #get full file path
                total_files += 1 #keep a count of the files
                pil_result = pil_verify(ifile)
                if pil_result==False:
                    print('Fail Pil_verify:\n' + ifile)
                #EXIF test
                exif_result = exif_test(ifile)
                if exif_result[0] == False:
                    print('Fail exif_test:\n' + ifile)
                if total_files % 250 == 0:
                    print(total_files)
    print('Done!')
