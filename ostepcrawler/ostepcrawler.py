# -*- coding: utf-8 -*-

from urllib.request import urlopen, urlretrieve

url = 'http://pages.cs.wisc.edu/~remzi/OSTEP/Chinese/'

def pdf_urls():
    pdf_urls = []
    for i in range(1, 50):
        pdf_urls.append(url + str(i).zfill(2) + '.pdf')
    return pdf_urls

def pdf_download():
    urls = pdf_urls()
    i = 0
    for url in urls:
        urlretrieve(url, str(i).zfill(2) + '.pdf')
        i += 1

if __name__ == '__main__':
    pdf_download()