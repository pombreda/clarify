#!/usr/bin/python
"""
Author: David Dahl
Copyright 2007, David L Dahl
http://www.ddahl.com
Created: 2007-04-20

'Clarify' is the opposite of 'obfuscate'
"""
from time import sleep
from optparse import OptionParser
import os
import sys
import re
from clarify import *

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-v", "--verbose", dest="verbose",
                      help="Toggles verbosity")
    parser.add_option("-i", "--inputfile", dest="inputfile",
                      help="PDF document to process")
    parser.add_option("-o", "--outputfile", dest="outputfile",
                      help="Path to output text file")
    parser.add_option("-s", "--scratchdir", dest="scratchdir",
                      help="Scratch/tmp directory")
    
    opt_args = parser.parse_args()
    cfg = opt_args[0]

    if not cfg.scratchdir:
        cfg.scratchdir = '/tmp/pdf_ocr'
        
    c = Clarify(cfg.inputfile,cfg.scratchdir)
    info = c.pdf_info()
    if cfg.verbose:
        print info

    c.rip_images(cfg.scratchdir)

    sleep_secs = int(info['Pages'])

    sleep(sleep_secs)

    lst = c.dir_to_lst(cfg.scratchdir)
    tiff_lst = c.convert_all_pnms(lst)
    lst = c.dir_to_lst(cfg.scratchdir)
    c.ocr_all(lst)

    sleep((sleep_secs / 2))

    lst = c.dir_to_lst(cfg.scratchdir)
    c.scrape_all(lst)

    sleep((sleep_secs / 2))

    txt_lst = []
    pages = c.txt_dct.keys()
    pages.sort()

    for p in pages:
        txt_lst.append(c.txt_dct[p])

    txt = '\n\n'.join(txt_lst)
    if cfg.verbose:
        print txt
    f = open(cfg.outputfile,'w')
    f.writelines(txt)
    f.close()
    if cfg.verbose:
        print "All done."
