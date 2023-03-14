#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
import webbrowser
import os
import re
import sys
#import urllib
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # +++your code here+++
    listed_logs = []
    screened_list = []
    with open(filename, 'r') as lines:
        for line in lines:
            if 'python' in line:
                parts = line.split()
                listed_logs.append(r'https://data.'+filename.split('.')[1]+'.'+filename.split('.')[2]+'.'+filename.split('.')[3] + parts[6])
    if filename == 'message_data.cyber.org.il':
        listed_logs.sort(key=lambda a: a.split('-')[2])
        temp = listed_logs[0]
        for fgg in listed_logs:
            if fgg == temp and fgg is not listed_logs[0]:
                continue
            screened_list.append(fgg)
            temp = fgg
        return screened_list
    listed_logs.sort()
    temp = listed_logs[0]
    for fgg in listed_logs:
        if fgg == temp and fgg is not listed_logs[0]:
            continue
        screened_list.append(fgg)
        temp = fgg

    return screened_list


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # +++your code here+++
    html_file = open(r'index.html','w')
    html_file.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <title>Title</title>\n</head>\n<body>\n')
    html_file.close()
    html_file = open(r'index.html','a')
    html_append_file = "<img src=\"C:\\Users\\HP\\PycharmProjects\\python_book\\aad\\image{}.jpg\">"
    i=1
    directory1 =dest_dir
    if not directory1 in os.listdir(r'C:\Users\HP\PycharmProjects\python_book'):
        os.mkdir(directory1)

    for url in img_urls:
        FILENAME = directory1 + r'\image'+str(i)+r'.jpg'
        with urllib.request.urlopen(url) as response:
            image = response.read()
            with open(FILENAME, 'wb') as output_file:
                output_file.write(image)
            html_file.write(html_append_file.format(str(i)))
        i+=1
    html_file.close()


def main():
    """FILENAME1 = 'logo_data.cyber.org.il'
    FILENAME11 = 'message_data.cyber.org.il'
    logs1 = read_urls(FILENAME1)
    logs11 = read_urls(FILENAME11)
    for a in logs1:
        print(a)
    for a in logs11:
        print(a)"""




    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))
    webbrowser.open_new_tab('index.html')

if __name__ == '__main__':
    main()
