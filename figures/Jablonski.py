import numpy as np
import matplotlib.pyplot as plt

width = 3.487
height = width*2
one_col = (width,height)
fig,ax = plt.subplots(figsize=one_col)

ax.spines['top'].set_visible(False)
#ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.plot((0,1),(0,0),lw='2',color='k')
plt.plot((0,1),(2.4,2.4),lw='2',color='k')
plt.plot((0,1),(6.4,6.4),lw='2',color='k')
plt.plot((0,1),(8.9,8.9),lw='2',color='k')
plt.plot((0,1),(10,10),'k--')

#Add vib levels
zero = (0,2.4,6.4,8.9)
for i in range(0,np.size(zero)):
    for j in range(0,5):
        plt.plot((0,1),(zero[i]+j*0.1,zero[i]+j*0.1),lw='0.5',color='k')

#Add arrows
plt.arrow(0.5,0,0,2.4-0.25,width = 0.02,head_width=0.10,head_length=0.22,color='C2')
plt.arrow(0.5,2.4,0,4.0-0.25,width = 0.02,head_width=0.10,head_length=0.22,color='C4')
plt.arrow(0.5,6.4,0,2.5-0.25,width = 0.02,head_width=0.10,head_length=0.22,color='C9')
plt.arrow(0.5,8.9,0,2.5-0.25,width = 0.02,head_width=0.10,head_length=0.22,color='C9')

#Add photon text
plt.annotate(r'$\lambda = 523$ nm',(0.6,1.2),ha='left',fontsize=10,color='C2')
plt.annotate(r'$\lambda = 312$ nm',(0.6,4.4),ha='left',fontsize=10,color='C4')
plt.annotate(r'$\lambda = 495-457$ nm',(0.6,7.45),ha='left',fontsize=10,color='C9')
plt.annotate(r'$\lambda = 495-457$ nm',(0.6,10.55),ha='left',fontsize=10,color='C9')

plt.annotate(r'D$_0$',(1.1,-0.1), ha='left',fontsize='14')
plt.annotate(r'D$_1$',(1.1,2.3), ha='left',fontsize='14')
plt.annotate(r'S$_0$',(1.1,6.3), ha='left',fontsize='14')
plt.annotate(r'S$_1$',(1.1,8.8), ha='left',fontsize='14')
plt.annotate(r'Dissociation',(1.1,9.9), ha='left',fontsize='10')
plt.annotate(r'Limit',(1.1,9.4), ha='left',fontsize='10')

plt.plot((-0.1,-0.1),(0,2.8),lw='0.5',color='k')
plt.plot((-0.1,-0.05),(0,0),lw='0.5',color='k')
plt.plot((-0.1,-0.05),(2.8,2.8),lw='0.5',color='k')
plt.annotate('radical',(-0.15,1.4),va='center',ha='center',rotation=90)

plt.plot((-0.1,-0.1),(6.4,10),lw='0.5',color='k')
plt.plot((-0.1,-0.05),(6.4,6.4),lw='0.5',color='k')
plt.plot((-0.1,-0.05),(10,10),lw='0.5',color='k')
plt.annotate('cation',(-0.15,8.2),va='center',ha='center',rotation=90)

plt.setp(ax.spines.values(), linewidth=1.5)
plt.xticks([])
plt.ylabel('Energy (eV)',fontsize=14)
plt.gcf().subplots_adjust(left=0.18)

plt.xlim(-0.30,1.6)

plt.savefig('Figure7.pdf',dpi=400,bbbox_inches='tight')
plt.show()

