#!/usr/bin/python3

import os
import dropbox
import requests
import bs4

def list_dropbox():
    dropbox_access_token = os.environ['DROPBOX_ACCESS_TOKEN']
    dbx = dropbox.Dropbox(dropbox_access_token)
    return [ entry.name for entry in dbx.files_list_folder('').entries ]

def save_to_dropbox(prefix, path, url):
    dropbox_access_token = os.environ['DROPBOX_ACCESS_TOKEN']
    dbx = dropbox.Dropbox(dropbox_access_token)
    dbx.files_save_url('/' + path, url)

def find_pdfs(url, prefix, filenames):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html5lib")
    for link in soup.find_all('a'):
        if link.get('href').endswith('.pdf'):
            filename = prefix + ' : ' + link.text + '.pdf'
            filename = filename.replace('/','-')
            if filename not in filenames:
                save_to_dropbox(prefix, filename, link.get('href'))
                print('saved ' + filename)
            else:
                print('already got ' + filename)

filenames = list_dropbox()

find_pdfs('http://www.wbjs.com/stream/newsletters/full/1/-//', 'JUNIORS', filenames)


