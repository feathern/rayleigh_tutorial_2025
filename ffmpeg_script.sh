FRAMERATE=30
idir=bvis/q1_r0
suffix=jpg
winsizex=800
winsize=800
mfile=${idir}.mp4

ffmpegcmd="ffmpeg -y -framerate $FRAMERATE -i $idir/%*.${suffix} -s:v ${winsize}x${winsize} -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p $mfile"
$ffmpegcmd

