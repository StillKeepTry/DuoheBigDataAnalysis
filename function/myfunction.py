'''
Created on 2015-5-7

@author: skt
'''

import csv

def filewrite(samples, filename):
    csvfile = file(filename, 'wb')
    f = csv.writer(csvfile)
    for i in samples:
        f.writerow(i)
    csvfile.close()
    
