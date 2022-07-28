from ntpath import join
import os
import re
import glob


new_name_pattern = "S\d{2}E\d{2}"
extension_pattern = "\.\w*$"

path = input("folder path: ")

files = glob.glob(path+ "/*")








for file in files:
    print(file)
    new_name = re.findall(new_name_pattern, file)
    print(new_name)
    extension = re.findall(extension_pattern, file)
    print(extension)
    full_name = path + "/" + new_name[0] + extension[0]
    print(full_name)
    os.rename(file, full_name)