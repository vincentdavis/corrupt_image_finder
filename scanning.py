from .image_tests import pil_verify, exif_test
from .data import Images
import os
import shutil
#import .EXIF
import exifread

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

##############################################################

imagetracker = dict()


def image_sorter(keepfolder = '', discardfolder = '', dryrun = True):
    """
    sorts photos into keepfolder or discard folder.
    Images place in keepfolder id duplicate are placed in keepfolder/dup2
    :param dryrun:
    :param discardfolder:
    :param keepfolder:
    :return: True (success), False (failed)
    """
    total_files = 0
    flist = []
    for rpath, dirlist, filelist in os.walk(keepfolder):
        # scan folder first
        for i in filelist:
            flist.append(i)
    print(len(flist))

    for i in Images.select().where(Images.Exif_Test==True, Images.Pil_Test==True, Images.DestinationFolder == None):
        #print(i.Exif_Test, i.Pil_Test,i.FullPath, i.DestinationFolder)
        if i.File_Name not in flist:
            try:
                i.DestinationFolder = shutil.move(i.FullPath, keepfolder)
                flist.append(i.File_Name)
                if total_files % 250 == 0:
                    print(total_files)
                    print(i.Exif_Test, i.Pil_Test,i.FullPath)
                total_files += 1
            except Exception as e:
                i.DestinationFolder = e



def image_scanner(path, types={'.jpg', '.jpeg', '.tif'}):
    total_files = 0
    for rpath, dirlist, filelist in os.walk(path):
        '''
        walk the directory getting file names.
        Walk returns a lists of file in each directory
        '''
        for afile in filelist:
            if os.path.splitext(afile)[1].lower() in types and not afile.startswith('.') and ('/Masters/' in rpath or '/Originals' in rpath or '/Recovered Photos' in rpath):
                ifile = os.path.join(rpath, afile) #get full file path
                total_files += 1 #keep a count of the files
                #Pil Test
                pil_result = pil_verify(ifile)
                # if pil_result==False:
                #     print('Fail Pil_verify:\n' + ifile)
                #EXIF test
                exif_result = exif_test(ifile)
                # if exif_result[0] == False:
                #     print('Fail exif_test:\n' + ifile)
                if total_files % 250 == 0:
                    print(total_files)
                try:
                    Images.create(FullPath=ifile, Path=rpath, File_Name=afile, Exif_Test=exif_result[0], ExifDate=exif_result[2],
                              ExifTags=exif_result[1], Pil_Test=pil_result)
                except:
                    pass
    print('Done!')

    # FullPath = CharField(unique=True)
    # Path = CharField()
    # File_Name = CharField()
    # Exif_Test = Bool()
    # ExifDate = CharField()
    # ExifTags = CharField()
    # Pil_Test = Bool()
    # Timestamp = DateTimeField(default=datetime.datetime.now)


def delete_faces(path, definition, kbsize=150):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            fname = os.path.splitext(name)[0].lower()
            if definition in fname:
                fpath = os.path.join(root, name)
                fsize = os.path.getsize(fpath)
                if fsize <= kbsize * 1000:
                    #print(name, fsize)
                    try:
                        shutil.move(fpath, "/Volumes/Drobo/FACES/")
                    except Exception as e:
                        if "already exists" in str(e):
                            os.remove(fpath)


def flatten_files(search_path, to_path, move=True):
    moved = 0
    discard = 0
    for root, dirs, files in os.walk(search_path, topdown=False):
        for name in files:
            fpath = os.path.join(root, name)
            if move:
                try:
                    shutil.move(fpath, to_path)
                    moved += 1
                except Exception as e:
                    if "already exists" in str(e):
                        os.remove(fpath)
                        discard += 1
                    else:
                        print('Error {}'.format(fpath))
            if not move:
                try:
                    shutil.copy(fpath, to_path)
                    moved += 1
                except Exception as e:
                    if "already exists" in str(e):
                        discard += 1
                    else:
                        print('Error {}'.format(fpath))
    print('Moved: {}. Discarded: {}'.format(moved, discard))


def delete_small(path, kbsize, match):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            fname = os.path.splitext(name)[1].lower()
            fpath = os.path.join(root, name)
            fsize = os.path.getsize(fpath)

            if fname in match and fsize <= kbsize * 1000:
                #print(fname, fsize)
                os.remove(fpath)



