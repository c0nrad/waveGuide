# grapher.py
#    Plots transmission as a function of frequency off of the meep
#    output files flux.dat and flux0.dat, and saves the result to a file
#
# Arguments:
#    PLOTNAME - Name of the plot to be saved
import sys
import matplotlib.pyplot as plt

if len(sys.argv) <= 1:
    print "Usage: python2.7 grapher.py PLOTNAME \nalso, flux.dat and flux0.dat must exist in the same directory"
    sys.exit()

x = []
y = []
for (a, b) in zip(open("flux.dat"), open("flux0.dat")):
    a = a.split(',')[1:]
    b = b.split(',')[1:]

    x0 = float(a[0]) 
    x1 = float(b[0])
    y0 = float(a[1])
    y1 = float(b[1])
    
    y.append(y0 / y1)
    x.append(x0)

print "Generating plot for: ", sys.argv[1]
plt.plot(x, y, "r", linestyle='solid', marker='.')
plt.xlabel("Frequency")
plt.ylabel("Transmission")
plt.title(sys.argv[1])
plt.savefig("plot" + sys.argv[1])

plt.show()
