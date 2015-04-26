## Clarify ##

Clarify helps you OCR 'image-only' PDFs. Your input is a PDF that you normally cannot extract text from. The output is text.

So far this project is a messy hack.

Clarify is a python module that wraps up tesseract-ocr, xpdf and netpbm

It would be nice to add some threading or concurrency to speed things up. I am also looking for some input and help in wrapping tesseract with swig, ctypes or pyrex.


## ROADMAP: ##

clean up existing module

add tests

concurrency and threading?? is tesseract thread safe?


REST interface:

send url of PDF or JSON dictionary of PDF urls to Web interface (Django)

add PDFs to queue, process

put resulting text into database

notify user when jobs are complete via RSS or Email


## Would this design be cleaner? ##

ctypes/pyrex/swig wrapping pf Tesseract-ocr, xPDF, and NetPBM bins?