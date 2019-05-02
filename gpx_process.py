#!/usr/bin/python
# -*- coding: utf8 -*-

#from datetime import datetime, timedelta
import datetime
import time
import os

mapillary_tools = 'c:\gis\pano_heading\mapillary_tools.exe'
CROPPED_FOLDER = 'cropped'

path = 'g:/VIDEO/2019_04_reg/stage1/'
files = []
for dirpath, dnames, fnames in os.walk(path):
    for f in fnames:
        if f.upper().endswith(".MP4"):
             files.append(os.path.join(dirpath, f))

for filepath in files:


 #create dir if not exists
    cropped_folder_path = os.path.join(os.path.dirname(filepath),CROPPED_FOLDER)
    if not os.path.exists(cropped_folder_path):
        os.makedirs(cropped_folder_path)
        
    cropped_filepath = os.path.join(os.path.dirname(filepath),CROPPED_FOLDER,os.path.basename(filepath))
        
    cmd = '''ffmpeg -i "'''+os.path.normpath(filepath)+'''" -vf fps=fps=30 -vf crop=iw:ih-140:0:0 -c:a copy "'''+os.path.normpath(cropped_filepath)+'''"'''
    print cmd
    os.system(cmd)
    
    
    
path = os.path.join(path,CROPPED_FOLDER)
files = []
for dirpath, dnames, fnames in os.walk(path):
    for f in fnames:
        if f.upper().endswith(".MP4"):
             files.append(os.path.join(dirpath, f))

for filepath in files:

                    
                    

    filename = os.path.basename(filepath)
    filedate_from_name = filename[6:14]
    filetime_from_name = filename[15:21]  


    #print   filedate_from_name, filetime_from_name
    #datetime_object = datetime.strptime(filedate_from_name+'_'+filetime_from_name, '%Y%m%d_%H%M%S')
    #now = datetime.utcnow()
    #print time.mktime(datetime_object)



    timestamp = time.mktime(datetime.datetime.strptime(filedate_from_name+'_'+filetime_from_name, "%Y%m%d_%H%M%S").timetuple())

    unix_timestamp_ms = int(timestamp)*1000
    unix_timestamp_timezone = unix_timestamp_ms+(0*60*60*1000)
    print unix_timestamp_timezone


    cmd = '''{mapillary_tools} sample_video --video_import_path "'''+os.path.normpath(filepath)+'''" --video_sample_interval 0.5 --video_start_time {unix_timestamp_timezone} --advanced'''
    cmd = cmd.format(mapillary_tools=mapillary_tools,unix_timestamp_timezone=unix_timestamp_timezone)
    print cmd
    os.system(cmd)

    sampled_video_frames_path = os.path.join(os.path.dirname(filepath),'mapillary_sampled_video_frames')

    cmd = ''' {mapillary_tools} process --advanced --import_path "'''+os.path.normpath(sampled_video_frames_path)+'''" --user_name "trolleway" --geotag_source "gpx" --geotag_source_path "g:\\VIDEO\\2019_04_reg\\20190427_repair.gpx" --overwrite_all_EXIF_tags '''
    cmd = cmd.format(mapillary_tools=mapillary_tools)
    os.system(cmd)

    #print datetime_object
    #print totimestamp(datetime_object)


    '''
    ffmpeg -y -i sample.mp4 -f lavfi -i color=c=black:s=30x40 -filter_complex "[1:v]scale=w=iw:h=ih[scaled]; [0:v][scaled]overlay=x=0.20*main_w:y=0.10*main_h:eof_action=‌​endall[out]; [0:a]anull[aud]" -map "[out]" -map "[aud]" -strict -2 outputfile.mp4
    '''
    
    '''
    crop video
    ffmpeg -i g:\VIDEO\2019_04_reg\stage2\CarDV_20190427_172205A.MP4 -vf crop=iw:ih-140:0:0 -c:a copy g:\VIDEO\2019_04_reg\stage2\cropped\CarDV_20190427_172205A.MP4
    '''
