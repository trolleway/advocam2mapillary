## Install

```

go get github.com/mlouielu/gopro-utils
go get github.com/mlouielu/gpxgo
```

## Run
```
FILE=GH011088.MP4

ffmpeg -y -i $FILE -codec copy -map 0:2 -f rawvideo _currentgopro.bin
go run bin/gopro2gpx/gopro2gpx.go -i /media/trolleway/WDBlue_2GB/GOPRO/20190708/_currentgopro.bin -o /media/trolleway/WDBlue_2GB/GOPRO/20190708/_currentgopro.gpx

```
