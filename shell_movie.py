#####################################
#  Shell Slice Frames
from rayleigh_diagnostics import Shell_Slices
import numpy
import matplotlib.pyplot as plt
from matplotlib import ticker, font_manager

def new_file_list(fdir,imin,imax):
    import os
    files = os.listdir(fdir)
    files.sort()
    subfiles=[]
    nf = len(files)
    if (nf > 0):
        for i in range(nf):
            ival = int(files[i])
            if ( (ival >= imin) and (ival <= imax) ):
                subfiles.append(files[i])
    return subfiles
    

def shell_frames_multi(shell_files,odir,rinds,qind,cscale=1.5,shell_dir='',sizetuple=(8,8),fcode="{:0>8d}",verbose=False,cmap="RdYlBu_r",titles=None, units = '',cshrink=1.0,latlines=None):
    nf = len(shell_files)
    
    if (shell_dir != ''):
        shell_dir = shell_dir+'/'
    
    if (verbose):
        print(len(shell_files))
    
    ##################################################
    # First, create a common color saturation scale
    f1 = shell_files[0]
    f2 = shell_files[nf//2]
    f3 = shell_files[nf-1]
    fcheck = [f1,f2,f3]
    nr = len(rinds)
    rms_mean = [0.0]*nr
    vmin = [0.0]*nr
    vmax = [0.0]*nr
    for f in fcheck:
        ss = Shell_Slices(shell_dir+f,path='')
        for k in range(nr):
            val = ss.vals[:,:,rinds[k],ss.lut[qind],0]
            rms = numpy.sqrt(numpy.mean(val**2))
            rms_mean[k]+=rms
    for k in range(nr):
        rms_mean[k] = rms_mean[k]/3.0
        vmin[k] = -cscale*rms_mean[k]
        vmax[k] = cscale*rms_mean[k]
    
    ##############################################################
    # Now, iterate over all files and save numbered images to odir
    
    ind = 0
    for i in range(nf):
        ss = Shell_Slices(shell_dir+shell_files[i],path='')
        niter = ss.niter
        ntheta = ss.ntheta
        nphi = ss.nphi
        costheta = ss.costheta
        theta = numpy.arccos(costheta)
        for j in range(niter):
            print(ind+1,nf*niter)
            fig, ax = plt.subplots(figsize=sizetuple, nrows=nr)
            for k, rind in enumerate(rinds):
                val = ss.vals[:,:,rind,ss.lut[qind],j]
               

                img = ax[k].imshow(numpy.transpose(val), extent=[0,360,-90,90],cmap=cmap, vmin = vmin[k], vmax = vmax[k])

                ax[k].set_xlabel( 'Longitude')
                ax[k].set_ylabel( 'Latitude')
                if (titles != None):
                    ax[k].set_title(  titles[k])

                cbar = fig.colorbar(img,ax=ax[k],shrink=cshrink)
                cbar.ax.set_ylabel(units, rotation=0)
                if (latlines != None):
                    for l in latlines:
                        ax[k].plot([l,l],[-90,90],color='gray')
            plt.tight_layout()

            ofile = odir+'/'+fcode.format(ind)+'.jpg'
            plt.savefig(ofile)
            plt.close()

            ind+=1  
