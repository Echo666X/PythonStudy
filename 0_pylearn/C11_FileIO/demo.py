import struct 
filename = "D:\\pylearn\\C11_FileIO\\ergcurve.dat"
f = open(filename,"rb")  #read binary 
rawData = f.read()
f.close()

f = open("garbage.dat","wb")
f.write(rawData)
f.close()


iSampleCount = len(rawData) // 4
curveData = []
for i in range(iSampleCount):
    fvalue, = struct.unpack("<f",rawData[i*4:i*4+4])   
    curveData.append(fvalue)

print(curveData)

import matplotlib.pyplot as plt 
plt.plot(curveData)
plt.show()


