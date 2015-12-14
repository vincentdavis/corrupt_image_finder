
import exifread
from PIL import Image


def pil_verify(ifile):
    try:
        with Image.open(ifile) as im:
            try:
                im.verify()
                return True
            except Exception as e:
                print(e)
                print('Pil.Image.verify() failed: ' + ifile)
                return False
#    except OverflowError as e:
#         print(e)
#         print('Python int too large to convert to C long: Is this a PSD file: ' + afile)
#         return False
    except IOError:
        print('PIL cannot identify image file: ' + ifile)
#         #testlog.write('> PIL cannot identify image file \n')
#         #testlog.write('>' + ifile + '\n')
        return None
#     except Exception as e:
#         print(e)
#         print(ifile)
#         print("Unexpected error doing PIL.Image.open():", sys.exc_info()[0]  + 'File number ' + str(total_files))
#         raise


def exif_test(ifile):
    # test, tagscount, anydate
        try:
            with open(ifile, 'rb') as im:
                tags = exifread.process_file(im, strict=True)
                tag_count = len(tags)
            try:
                anydate = any([True for i in tags if 'Date' in i])
            except:
                anydate = None
            return True, tag_count, anydate
        except Exception as e:
            print(e)
            print('Failed exif: ' + ifile)
            return False, None, None
