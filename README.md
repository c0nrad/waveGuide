WaveGuide
============

The idea is to build a waveguide model to be used to build quantum logic gates. The model is being built using [MEEP](http://ab-initio.mit.edu/wiki/index.php/Meep), with minor scripts written in python2.7 and modeling done in mayavi2.

The current design of the waveguide is as follows:
![Figure](https://raw.github.com/c0nrad/waveGuide/master/doc/waveGuideDesign.png)

Usage
-

The package includes a Makefile for ease of development. To run the simulation, type the command _make run_ into a terminal inside of the waveGuide directory, and the simulation will run. The useful data values (flux) will also be grep'd to an outside file. To see a plot of the values recently calculated type _make graph_. This will graph the values using the python library matlibplot. To view the model in 3d, type in _mayavi2_ (it may need to be installed sudo apt-get install mayavi2). 

Notes
-

The current .ctl file (meep file), does not match that of the image shown above. Currently it is 3d extrapolation of the waveguide tutorial [here](http://ab-initio.mit.edu/wiki/index.php/Meep_Tutorial/Band_diagram%2C_resonant_modes%2C_and_transmission_in_a_holey_waveguide).

