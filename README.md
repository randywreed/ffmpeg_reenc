## This is a python script to use ffmpeg to concatenate files and re-encode them
## It is particularly useful for merging downloaded videos with videos created in obs
##
```
python -m ffmpeg-reenc.py -f [input file names (comma separate)] \
 -r [reencode flag for each file, r=reencode s=skip] \
 -o [ouput file name]
```