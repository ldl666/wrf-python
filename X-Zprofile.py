import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc 

ds = nc.Dataset('I:\WRFOUT1020\WRF1019\wrfout_d01_0001-01-01_00_00_00')
# print(ds.variables)

ph = ds.variables["PH"][:,:,:,:]
phb = ds.variables['PHB'][:,:,:,:]
h = (ph+phb)/9.81

t=24
h_5 = h[t,:,0,:]
u = ds.variables["U"][t,:,0,:]
w = ds.variables["W"][t,:,0,:]
tem = ds.variables["T"][t,:,0,:]
tem = tem+300

x = np.linspace(0, 6000, 59)
z = np.linspace(0, 2000, 39)

xx,zz = np.meshgrid(x,z)

ht=[]
for i in range(0,59):
    for k in range(0,39):
        h_5_i = h_5[:,i]
        h1 = 0.5*(h_5_i[k]+h_5_i[k+1])
        ht.append(h1)
ht = np.array(ht).reshape(59,39).T


U = []
for k in range(0,39):
    for i in range(0,59):
        u_k = u[k,:]
        u1 = 0.5*(u_k[i]+u_k[i+1])
        U.append(u1)
U = np.array(U).reshape(59,39).T

W = []
for i in range(0,59):
    for k in range(0,39):
        w_i = w[:,i]
        w1 = 0.5*(w_i[k]+w_i[k+1])
        W.append(w1)
W = np.array(W).reshape(59,39).T
wer = W[1,:]-w[1,:]

fig=plt.figure(figsize=(10,8),dpi=150)
fig_ax =fig.add_axes([0.1,0.1,0.4,0.3])
fig_ax=plt.subplot(1,1,1)
fig_ax.set_title("Time="+str(int(t/6))+'h',y=1.03,loc="left")
fig_ax.set_xlabel("X-Direction(m)")
fig_ax.set_ylabel("Autitude(m)")
fig_ax.set_xlim(0,6000)
fig_ax.set_ylim(0,2000)
levels = np.linspace(308,311,20)
levels = np.round(levels,2)
cmap = cmap=plt.cm.bwr
f1 = fig_ax.contourf(xx,ht,tem,levels=levels,extend='both',cmap=cmap)
cb=fig.colorbar(f1)
cb.set_label('Potential Temperature (K)')
qv = fig_ax.quiver(xx,ht,U,W,scale=120)
fig_ax.quiverkey(qv,0.95,1.02,2,"2m s$^-$$^1$")
plt.show()
plt.close()
