from rayleigh_diagnostics import Shell_Slices
import os
from shell_movie import new_file_list, shell_frames_multi
import matplotlib


#Simple python script that illustrates how to create a series of frames from shell-slice data
#that can then be used to make a movie.

#After running this script, modify ffmpeg_script.sh as appropriate to compile the frames into an animation.

matplotlib.rcParams.update({'font.size': 12})
mdir = '/home/nfeatherstone/runs/cig_vis/bvis'
odir = '/home/nfeatherstone/runs/cig_vis/bvis'
shell_dir = mdir+'/Shell_Slices/'

imin = 0
imax = 500000

rind = 0
qind = 1
#qind=1

odir=odir+'/q'+str(qind)+'_r'+str(rind)

print(odir)
shell_files = new_file_list(shell_dir,imin,imax)
shell_files = shell_files[0:10]
print(shell_files)

#shell_frames(shell_files,odir,rind,qind,shell_dir=shell_dir,cscale=2.5)
rinds = [0,0,1]
qstr = r'V$_r$'
titles = []
titles.append(qstr+'      upper CZ')
titles.append('middle CZ')
titles.append('lower CZ')
matplotlib.rcParams.update({'font.size': 16})
latlines = [90,180,270]
shell_frames_multi(shell_files,odir,rinds,qind,shell_dir=shell_dir,cscale=2.5, 
                   sizetuple=(15,15), units='G', titles=titles,cshrink=0.75,latlines=latlines)
