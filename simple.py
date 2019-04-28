#!/usr/bin/python
# -*- coding: utf8 -*-

import os


#process video file from Advocam dashcam for extract gpx file
#process one video file



def video2gpx(filename='~/Videos/CarDV_20190427_170108A.MP4'):
    cmd = 'exiftool --ee {filename}'.format(filename=filename)
    print cmd
    print 'exiftool should be newer version'
    os.system(cmd)
    
    
    



video2gpx()

