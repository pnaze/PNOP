from pylab import plot, show, xlim, ylim, xlabel, ylabel, legend, fill_between, text, arrow, xticks, yticks, title, figtext, savefig, xscale, yscale
from numpy import loadtxt, linspace, sin, cos, exp, abs

data1 = loadtxt("/home/pnaze/Research/ongoing/PNOP/data/data_rel_psi3.dat", float)

x1 = data1[:,0]
y1 = data1[:,1]

plot(x1,y1,"k-", label=r"$\epsilon$",linewidth="3")

title(r"$(c)\, \Psi_3(t)$",fontsize="20")

legend(loc='upper right',fontsize="18")

xlabel(r"$\tau/\tau_w$",fontsize="18")

xscale('log')

xlim(0.001,100)
ylim(-0.02,0.3)

savefig("/home/pnaze/Research/ongoing/PNOP/figures/psi3.eps")
