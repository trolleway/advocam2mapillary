#!/usr/bin/python
# -*- coding: utf8 -*-

import os


#process video file from Advocam dashcam for extract gpx file
#process one video file


def lat_dms2lat_dec(src):
    return '37.666'

def lon_dms2lon_dec(src):
    return '55.666'
    
def video2gpx(filename='~/Videos/CarDV_20190427_170108A.MP4'):
    cmd = 'exiftool --ee {filename}'.format(filename=filename)
    print cmd
    print 'exiftool should be newer version'
    #os.system(cmd)
    
    #get subtitles stream to variable
    
    subtitles='''
    ---- Doc1 ----
Sample Time                     : 0 s
Sample Duration                 : 1.00 s
Text                            : -21.1014.14.$GPRMC,130919.00,V,,,,,,,190119,,,N*61...
---- Doc2 ----
Sample Time                     : 1.00 s
Sample Duration                 : 1.00 s
Text                            : -144.970.65.$GPRMC,130920.00,V,,,,,,,190119,,,N*6B...
---- Doc3 ----
Sample Time                     : 2.00 s
Sample Duration                 : 1.00 s
Text                            : -33.1017.6.$GPRMC,130921.00,V,,,,,,,190119,,,N*6A...
---- Doc4 ----
Sample Time                     : 3.00 s
Sample Duration                 : 1.00 s
Text                            : -140.983.82.$GPRMC,130922.00,A,5533.90640,N,03733.59611,E,0.496,,190119,,,A*6A...
---- Doc5 ----
Sample Time                     : 4.00 s
Sample Duration                 : 1.00 s
Text                            : -51.1015.32.$GPRMC,130922.00,A,5533.90640,N,03733.59611,E,0.496,,190119,,,A*6A...
---- Doc6 ----
Sample Time                     : 5.00 s
Sample Duration                 : 1.00 s
Text                            : -88.1005.35.$GPRMC,130924.00,A,5533.90715,N,03733.60372,E,0.428,,190119,,,A*62...
---- Doc7 ----
Sample Time                     : 6.00 s
Sample Duration                 : 1.00 s
Text                            : -63.1023.69.$GPRMC,130924.00,A,5533.90715,N,03733.60372,E,0.428,,190119,,,A*62...
---- Doc8 ----
Sample Time                     : 7.00 s
Sample Duration                 : 1.00 s
Text                            : -63.1023.69.$GPRMC,130926.02,V,,,,,,,190119,,,N*6F..341,E,0.492,,190119,,,A*64...
---- Doc9 ----
Sample Time                     : 8.00 s
Sample Duration                 : 1.00 s
Text                            : -63.1023.69.$GPRMC,130926.02,V,,,,,,,190119,,,N*6F..341,E,0.492,,190119,,,A*64...
---- Doc10 ----
Sample Time                     : 9.00 s
Sample Duration                 : 1.00 s
Text                            : -63.1023.69.$GPRMC,130927.00,A,5533.90487,N,03733.60395,E,0.881,,190119,,,A*6F...
---- Doc11 ----
Sample Time                     : 10.00 s
Sample Duration                 : 1.00 s
Text                            : -17.1003.20.$GPRMC,130929.00,A,5533.90185,N,03733.60609,E,0.906,,190119,,,A*68...
---- Doc12 ----
Sample Time                     : 11.00 s
Sample Duration                 : 1.00 s
Text                            : -17.1003.20.$GPRMC,130930.00,A,5533.90071,N,03733.60636,E,2.057,82.47,190119,,,A*4E...
---- Doc13 ----
Sample Time                     : 12.00 s
Sample Duration                 : 1.00 s
Text                            : -62.1022.62.$GPRMC,130931.00,A,5533.90030,N,03733.60765,E,2.334,82.29,190119,,,A*43...
---- Doc14 ----
Sample Time                     : 13.00 s
Sample Duration                 : 1.00 s
Text                            : 36.1000.-10.$GPRMC,130932.00,A,5533.90060,N,03733.60858,E,1.829,,190119,,,A*6F..*43...
---- Doc15 ----
Sample Time                     : 14.00 s
Sample Duration                 : 1.00 s
Text                            : -34.1004.99.$GPRMC,130933.00,A,5533.90075,N,03733.60902,E,0.448,,190119,,,A*6E..*43...
'''
    for line in subtitles.splitlines():
        location_info = {}
        gpx_trkpt = {}
        #print line
        if '$GPRMC' in line:
            position = line.find('$GPRMC')
            line = line[position:]
            GPRMC_record = line.split(',')
            #print GPRMC_record
            location_info['time'] = GPRMC_record[1]
            location_info['navigation_reciver_warning'] = GPRMC_record[2]
            location_info['lat'] = GPRMC_record[3]
            location_info['lat_hemisphere'] = GPRMC_record[4]
            location_info['lon'] = GPRMC_record[5]
            location_info['lon_hemisphere'] = GPRMC_record[6]
            location_info['speed_knots'] = GPRMC_record[7]
            location_info['true_course'] = GPRMC_record[8]
            location_info['date'] = GPRMC_record[9]
            
            gpx_trkpt['lat'] = lat_dms2lat_dec(location_info['lat'])
            gpx_trkpt['lon'] = lon_dms2lon_dec(location_info['lon'])
            print line
            print location_info
    
    
    



video2gpx()

