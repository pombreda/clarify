## Dependencies ##

You have several dependencies to fulfill to use Clarify.

**Linux (so far - I have only tested on Ubuntu Edgy)**

**xPDF - I used the Ubuntu package**

**libtiff - I used the Ubuntu package**

**NetPBM - I used the Ubuntu package**

**tesseract-ocr - you have to build this one! easy easy: ./configure make make install**


http://code.google.com/p/tesseract-ocr/


 **NOTE** you have to manually `cp -r ./tessdata /usr/local/bin` after building tesseract


## Usage ##


See test.py and test\_multi.py for usage details:


This needs some clean up and simplification.



## FAQ ##

**Q.** Why would I ever want to use Clarify?

**A.** You have a PDF file or a Bunch of Tiffs that you want to perform OCR on in an automated/batch-process way.