import os
from lbdict import LetterBitmapDictionary


def makeLibrary():
    script_dir = os.path.dirname(__file__)
    rel_path = ".idea/kongtext.ttf"
    rel_path_save = "shouldntexist/"
    abs_font_path = os.path.join(script_dir, rel_path)
    abs_save_dir = os.path.join(script_dir, rel_path_save)
    return LetterBitmapDictionary(abs_font_path, 8, abs_save_dir, transposed=True, use_save=False)

LIBRARY = makeLibrary()
print(LIBRARY)
