run:
	meep holey-wvg-cavity.ctl componentThing=Ez | tee holey-wvg-cavity.out
	meep N=0 holey-wvg-cavity.ctl | tee holey-wvg-cavity.out0

	grep flux1: holey-wvg-cavity.out > flux.dat
	grep flux1: holey-wvg-cavity.out0 > flux0.dat

# For 3d models
	h5tovtk holey-wvg-cavity-eps-000000.00.h5	

# For 2d models
#	h5topng holey-wvg-cavity-eps-000000.00.h5	
#	h5topng -Zc dkbluered holey-wvg-cavity-hz-slice.h5				

compute-mode:
	meep compute-mode?=true holey-wvg-cavity.ctl
	h5topng -RZc dkbluered -C holey-wvg-cavity-eps-000000.00.h5 holey-wvg-cavity-hz-*.h5
	convert holey-wvg-cavity-hz-*.png holey-wvg-cavity-hz.gif
	feh holey-wvg-cavity-hz.gif

graph:
	python2.7 grapher.py sampleName

clean:
	rm -f *.out *.h5 *~ *.dat *.out0 *.vtk
