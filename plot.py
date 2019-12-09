import numpy as np
from chainconsumer import ChainConsumer

def sevenchain_multi_plot(filename, out, chainnames, paranames,plotrange):
	fid = np.array([-1.0,0.0])

	d1read = np.genfromtxt(filename[0])
	d2read = np.genfromtxt(filename[1])
	d3read = np.genfromtxt(filename[2])
	d4read = np.genfromtxt(filename[3])
	d5read = np.genfromtxt(filename[4])	
	d6read = np.genfromtxt(filename[5])
	d7read = np.genfromtxt(filename[6])	
	
	d1=d1read[:,(3,4)]-fid
	d2=d2read[:,(3,4)]-fid
	d3=d3read[:,(3,4)]-fid
	d4=d4read[:,(3,4)]-fid
	d5=d5read[:,(3,4)]-fid
	d6=d6read[:,(3,4)]-fid
	d7=d7read[:,(3,4)]-fid
	
	c = ChainConsumer()
	c.add_chain(d1,parameters=paranames, name =chainnames[0])
	c.add_chain(d2,name =chainnames[1])
	c.add_chain(d3,name =chainnames[2])
	c.add_chain(d4,name =chainnames[3])
	c.add_chain(d5,name =chainnames[4])
	c.add_chain(d6,name =chainnames[5])
	c.add_chain(d7,name =chainnames[6])
	#c.configure(kde=[2,2],colors=['c','y'], sigmas=[1,2],shade=True,shade_alpha=0.2,shade_gradient=0.0)
	c.configure(colors=['c','y','r','g','b','k','brown'], sigmas=[1],shade=True,shade_alpha=0.2,shade_gradient=0.0)
	fig = c.plotter.plot(figsize=2.0,extents=plotrange,filename="plots/"+out,truth=[0.0,0.0])


def sixchain_multi_plot(filename, out, chainnames, paranames,plotrange):
	fid = np.array([-1.0,0.0])

	d1read = np.genfromtxt(filename[0])
	d2read = np.genfromtxt(filename[1])
	d3read = np.genfromtxt(filename[2])
	d4read = np.genfromtxt(filename[3])
	d5read = np.genfromtxt(filename[4])	
	d6read = np.genfromtxt(filename[5])	
	
	d1=d1read[:,(3,4)]-fid
	d2=d2read[:,(3,4)]-fid
	d3=d3read[:,(3,4)]-fid
	d4=d4read[:,(3,4)]-fid
	d5=d5read[:,(3,4)]-fid
	d6=d6read[:,(3,4)]-fid
	
	c = ChainConsumer()
	c.add_chain(d1,parameters=paranames, name =chainnames[0])
	c.add_chain(d2,name =chainnames[1])
	c.add_chain(d3,name =chainnames[2])
	c.add_chain(d4,name =chainnames[3])
	c.add_chain(d5,name =chainnames[4])
	c.add_chain(d6,name =chainnames[5])
	#c.configure(kde=[2,2],colors=['c','y'], sigmas=[1,2],shade=True,shade_alpha=0.2,shade_gradient=0.0)
	c.configure(colors=['c','y','r','g','b','k'], sigmas=[1],shade=True,shade_alpha=0.2,shade_gradient=0.0)
	fig = c.plotter.plot(figsize=2.0,extents=plotrange,filename="plots/"+out,truth=[0.0,0.0])
	


def threechain_single_plot(filename, out, chainnames, paranames,fid,stepstart,stepstop):
	d1 = np.genfromtxt(filename[0])
	d2 = np.genfromtxt(filename[1])
	d3 = np.genfromtxt(filename[2])
	c = ChainConsumer()
	c.add_chain(d1[stepstart:stepstop,(3,4)],parameters=paranames, name =chainnames[0])
	c.add_chain(d2[stepstart:stepstop,(3,4)], name =chainnames[1])
	c.add_chain(d3[stepstart:stepstop,(3,4)], name =chainnames[2])
	c.configure(kde=[2,2,2],shade=True,shade_alpha=0.2, bar_shade=True)
	#c.configure(shade=[True,False,False],shade_alpha=[0.2,0.2,0.2],linestyles=["--", "-", "-."],linewidths=[0.5,1.,1.])	
	fig = c.plotter.plot(truth=fid,figsize=2.0,filename="/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/plots/"+out)
	

def threechain_multi_plot(filename, out, chainnames, paranames,fid, start, stop):
	d1 = np.genfromtxt(filename[0])
	d2 = np.genfromtxt(filename[1])
	d3 = np.genfromtxt(filename[2])
	c = ChainConsumer()
	c.add_chain(d1[1570000:,start:stop],parameters=paranames, name =chainnames[0])
	c.add_chain(d2[1570000:,start:stop], name =chainnames[1])
	c.add_chain(d3[1570000:,start:stop], name =chainnames[2])
	c.configure(shade=[True,False,False],shade_alpha=[0.2,0.2,0.2],linestyles=["--", "-", "-"],linewidths=[0.5,1.,1.])	
	fig = c.plotter.plot(truth=fid,filename="/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/plots/"+out)


# filename=["/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=2.000000e+03_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_LSST_Y10_area=1.800000e+04_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=1.800000e+04_dmo"]
# chainnames=[r"WFIRST std",r"LSST Y10",r"WFIRST wide"]
# stepstart=700000
# stepstop=900000
# fid=[-1.,0.]
# paranames=[r"$w_0$", r"$w_a$"]
# threechain_single_plot(filename,"WF_LSST"+str(stepstart)+".pdf",chainnames,paranames,fid,stepstart,stepstop)

# filename=["/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=2.000000e+03_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_LSST_Y10_area=1.800000e+04_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=1.800000e+04_dmo"]
# chainnames=[r"WFIRST std",r"LSST Y10",r"WFIRST wide"]
# stepstart=900000
# stepstop=1100000
# fid=[-1.,0.]
# paranames=[r"$w_0$", r"$w_a$"]
# threechain_single_plot(filename,"WF_LSST"+str(stepstart)+".pdf",chainnames,paranames,fid,stepstart,stepstop)

# filename=["/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=2.000000e+03_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_LSST_Y10_area=1.800000e+04_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=1.800000e+04_dmo"]
# chainnames=[r"WFIRST std",r"LSST Y10",r"WFIRST wide"]
# stepstart=1100000
# stepstop=1300000
# fid=[-1.,0.]
# paranames=[r"$w_0$", r"$w_a$"]
# threechain_single_plot(filename,"WF_LSST"+str(stepstart)+".pdf",chainnames,paranames,fid,stepstart,stepstop)

# filename=["/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=2.000000e+03_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_LSST_Y10_area=1.800000e+04_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=1.800000e+04_dmo"]
# chainnames=[r"WFIRST std",r"LSST Y10",r"WFIRST wide"]
# stepstart=1300000
# stepstop=1500000
# fid=[-1.,0.]
# paranames=[r"$w_0$", r"$w_a$"]
# threechain_single_plot(filename,"WF_LSST"+str(stepstart)+".pdf",chainnames,paranames,fid,stepstart,stepstop)


filename=["/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=2.000000e+03_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_LSST_Y10_area=1.800000e+04_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=1.800000e+04_dmo"]
chainnames=[r"WFIRST std",r"LSST Y10",r"WFIRST wide"]
fid=[0.3156,0.831,0.9645,-1.,0.,0.0491685,0.6727]
paranames=[r"$Omega_m$", r"$\sigma_8$",r"$n_s$", r"$w_0$", r"$w_a$",r"$\Omega_b$", r"$h_0$"]
threechain_multi_plot(filename,"WFIRST_LSST_cosmo.pdf",chainnames,paranames,fid,0,7)

filename=["/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=2.000000e+03_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_LSST_Y10_area=1.800000e+04_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=1.800000e+04_dmo"]
chainnames=[r"WFIRST std",r"LSST Y10",r"WFIRST wide"]
fid=[1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2]
paranames=[r"$b_1$", r"$b_2$", r"$b_3$", r"$b_4$", r"$b_5$", r"$b_6$", r"$b_7$", r"$b_8$", r"$b_9$", r"$b_10$"]
threechain_multi_plot(filename,"WFIRST_LSST_gbias.pdf",chainnames,paranames,fid,7,17)

filename=["/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=2.000000e+03_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_LSST_Y10_area=1.800000e+04_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=1.800000e+04_dmo"]
chainnames=[r"WFIRST std",r"LSST Y10",r"WFIRST wide"]
fid=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.05]
paranames=[r"$sph_1$", r"$sph_2$", r"$sph_3$", r"$sph_4$", r"$sph_5$", r"$sph_6$", r"$sph_7$", r"$sph_8$", r"$sph_9$", r"$sph_10$",r"$\sigma_z source$"]
threechain_multi_plot(filename,"WFIRST_LSST_sourcez.pdf",chainnames,paranames,fid,17,28)

filename=["/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=2.000000e+03_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_LSST_Y10_area=1.800000e+04_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=1.800000e+04_dmo"]
chainnames=[r"WFIRST std",r"LSST Y10",r"WFIRST wide"]
fid=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.03]
paranames=[r"$lph_1$", r"$lph_2$", r"$lph_3$", r"$lph_4$", r"$lph_5$", r"$lph_6$", r"$lph_7$", r"$lph_8$", r"$lph_9$", r"$lph_10$",r"$\sigma_z lens$"]
threechain_multi_plot(filename,"WFIRST_LSST_lensz.pdf",chainnames,paranames,fid,28,39)

filename=["/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=2.000000e+03_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_LSST_Y10_area=1.800000e+04_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=1.800000e+04_dmo"]
chainnames=[r"WFIRST std",r"LSST Y10",r"WFIRST wide"]
fid=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
paranames=[r"$m_1$", r"$m_2$", r"$m_3$", r"$m_4$", r"$m_5$", r"$m_6$", r"$m_7$", r"$m_8$", r"$m_9$", r"$m_10$"]
threechain_multi_plot(filename,"WFIRST_LSST_shearcalib.pdf",chainnames,paranames,fid,39,49)


filename=["/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=2.000000e+03_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_LSST_Y10_area=1.800000e+04_dmo","/Users/timeifler/Dropbox/cosmolike_store/WFIRST_LSST/like/like_3x2pt_WFIRST_area=1.800000e+04_dmo"]
chainnames=[r"WFIRST std",r"LSST Y10",r"WFIRST wide"]
fid=[5.92,1.1,-0.47,0.0,0.0,0.0,0.0]
paranames=[r"$A_IA$",r"$beta$",r"$eta$",r"$eta_{high_z}$",r"$Q_1$",r"$Q_2$",r"$Q_3$"]
threechain_multi_plot(filename,"WFIRST_LSST_IA_Bary.pdf",chainnames,paranames,fid,49,56)


