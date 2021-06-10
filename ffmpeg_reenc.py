import argparse
import os

parser=argparse.ArgumentParser()
parser.add_argument('-f','--files', nargs='+',help="files to combine and reencode",type=str)
parser.add_argument('-r',"--reencode",nargs="+",help="indicate whether to skip (s) or re-encode(r) for each file",type=str)
parser.add_argument('-o','--output',type=str,help="output file name")
args=parser.parse_args()
print(args.files)
renc_flag=args.reencode[0].split(",")
output=args.output
#create ffmpeg command
c1="ffmpeg "
s=" -i "
ofiles=""
print(args.files)
try:
    files=args.files[0].split(",")
except:
    files=args.files
for i in files:
    print(i)
    ofiles=ofiles+" -i '"+i.strip()+"'"
file=c1+ofiles
print(file)
c2=' -filter_complex "'
c4=""
k=0
for r in renc_flag:
    if r=="r":
        c2=c2+"[#:v:0]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2[v#]; ".replace("#",str(k))
        c4=c4+"[v#][#:a:0]".replace('#',str(k))
        k=k+1
    else:
        c4=c4+"[#:v:0][#:a:0]".replace("#",str(k))
        k=k+1
c3="concat=n="+str(k)+':v=1:a=1[outv][outa]" -map "[outv]" -map "[outa]" '+output

#put it all together
cmd=file+c2+c4+c3
print('executing {}'.format(cmd))
input('execute command?')
os.system(cmd)