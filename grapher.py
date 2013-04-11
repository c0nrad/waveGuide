

import matplotlib.pyplot as plt

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



plt.plot(x, y, "r", linestyle='solid', marker='.')
plt.xlabel("Frequency")
plt.ylabel("Transmission")
plt.title("Title")
plt.show()
