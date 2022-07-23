#!/usr/bin/env python
# -*- coding: utf-8 -*-

#This code convert each pdf in a path to a JPEG image, if the pdf has more than 1 page it will create a file .jpg for each page

__author__ = "Mario Fernández Gómez"
__version__ = "1.0.1"
__contact__ = "https://github.com/mariofg92"

#import module 
import glob, os
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

path = input("Enter path of pdfs or drag the folder into this window to get its path: ").replace("'","")
os.chdir(path)
print("Converting PDF to JPEG:")

for pdf in glob.glob("*.pdf"):
    name_no_extension = pdf.replace(".pdf","")
    images = convert_from_path(pdf, dpi=300, timeout=600)
    print(pdf)

    for iteration, page in enumerate(images):
        out_file = name_no_extension + "_" + str(iteration + 1) + ".jpg"
        print("    ---> " + out_file)
        page.save(out_file, 'JPEG')
