"""
Author: David Dahl
Copyright 2007, David L Dahl
http://www.ddahl.com
Created: 2007-04-20

'Clarify' is the opposite of 'obfuscate'

Licensed under Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0

"""
import os
import sys

def dir_to_lst(pth):
    """get a list of files with abs path in a directory"""
    lst = os.listdir(pth)
    new_lst = []
    for f in lst:
        if f == 'copy.pdf' or os.path.isdir(f):
            pass
        else:
            new_lst.append(os.path.join(pth, f))
        #fixme: sort this list by filename
    return new_lst
