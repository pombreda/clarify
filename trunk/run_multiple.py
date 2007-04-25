#!/usr/bin/python
"""
Author: David Dahl
Copyright 2007, David L Dahl
http://www.ddahl.com
Created: 2007-04-20

'Clarify' is the opposite of 'obfuscate'

Licensed under Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0


"""
from time import sleep
import os
import sys
import re
from optparse import OptionParser

from clarify import *

#
#fixme: source pdf's need to have spaces and non [a-z][0-9] chars removed
#

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-v", "--verbose", dest="verbose",
                      help="Toggles verbosity")
    parser.add_option("-i", "--inputdir", dest="inputdir",
                      help="PDF document to process")
    parser.add_option("-o", "--outputdir", dest="outputdir",
                      help="Path to output text file")
    parser.add_option("-s", "--scratchdir", dest="scratchdir",
                      help="Scratch/tmp directory")

    opt_args = parser.parse_args()
    cfg = opt_args[0]

    if not cfg.scratchdir:
        cfg.scratchdir = '/tmp/pdf_ocr'

    #fixme:
    #check for required libs/bins:
    #*xpdf
    #*pnm2tiff
    #*tesseract
    
    count = 1

    pdf_lst = dir_to_lst(cfg.inputdir)

    ocr_cache = cfg.scratchdir
    output = cfg.outputdir

    if not os.path.exists(ocr_cache):
        os.system('mkdir %s' % ocr_cache)

    if not os.path.exists(output):
        os.system('mkdir %s' % output)

    for pdf in pdf_lst:
        working_dir = "%s/%s" % (ocr_cache,count,)

        if not os.path.exists(working_dir):
            os.system('mkdir %s' % working_dir)

        c = Clarify(pdf,working_dir)
        info = c.pdf_info()
        
        if cfg.verbose:
            print info

        c.rip_images(working_dir)
        
        if cfg.verbose:
            print "sleeping...b right back."
        sleep_secs = int(info['Pages'])

        sleep(sleep_secs)

        lst = c.dir_to_lst(working_dir)
        tiff_lst = c.convert_all_pnms(lst)
        lst = c.dir_to_lst(working_dir)
        c.ocr_all(lst)

        sleep((sleep_secs / 2))

        lst = c.dir_to_lst(working_dir)
        c.scrape_all(lst)

        sleep((sleep_secs / 2))

        txt_lst = []
        pages = c.txt_dct.keys()
        pages.sort()

        for p in pages:
            txt_lst.append(c.txt_dct[p])

        txt = '\n\n'.join(txt_lst)
        output_file = "%s/%s" % (output,count,)
        if cfg.verbose:
            print txt
        f = open(output_file,'w')
        f.writelines(txt)
        f.close()
        count = count +1
        c = None
        f = None
        txt = None
