import csv
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean

# IMPORT SIGNAL A #

tA = [] # column 0
data1A = [] # column 1
# data2A = [] # column 2

with open('sigA.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        tA.append(float(row[0])) # leftmost column
        data1A.append(float(row[1])) # second column
        # data2A.append(float(row[2])) # third column

# for i in range(tA):
#     # print the data to verify it was read
#     # print(str(tA[i]) + ", " + str(data1A[i]) + ", " + str(data2A[i]))
#     print(str(tA[i]) + ", " + str(data1A[i]))

freqA = len(tA)/tA[-1]

# IMPORT SIGNAL B # 

tB = [] # column 0
data1B = [] # column 1
# data2B = [] # column 2

with open('sigB.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        tB.append(float(row[0])) # leftmost column
        data1B.append(float(row[1])) # second column
        # data2B.append(float(row[2])) # third column

# for i in range(tB):
#     # print the data to verify it was read
#     # print(str(tB[i]) + ", " + str(data1B[i]) + ", " + str(data2B[i]))
#     print(str(tB[i]) + ", " + str(data1B[i]))

freqB = len(tB)/tB[-1]

# IMPORT SIGNAL C #

tC = [] # column 0
data1C = [] # column 1
# data2C = [] # column 2

with open('sigC.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        tC.append(float(row[0])) # leftmost column
        data1C.append(float(row[1])) # second column
        # data2C.append(float(row[2])) # third column

# for i in range(tC):
#     # print the data to verify it was read
#     # print(str(tC[i]) + ", " + str(data1C[i]) + ", " + str(data2C[i]))
#     print(str(tC[i]) + ", " + str(data1C[i]))

freqC = len(tC)/tC[-1]

# IMPORT SIGNAL D #

tD = [] # column 0
data1D = [] # column 1
# data2D = [] # column 2

with open('sigD.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        tD.append(float(row[0])) # leftmost column
        data1D.append(float(row[1])) # second column
        # data2D.append(float(row[2])) # third column

# for i in range(tD):
#     # print the data to verify it was read
#     # print(str(tD[i]) + ", " + str(data1D[i]) + ", " + str(data2D[i]))
#     print(str(tD[i]) + ", " + str(data1D[i]))

freqD = len(tD)/tD[-1]

# analyze signal A

Fs = freqA # sample rate
Ts = 1.0/Fs; # sampling interval
ts = np.arange(0,tA[-1],Ts) # time vector
yA = data1A # the data to make the fft from
nA = len(yA) # length of the signal
kA = np.arange(nA)
TA = nA/Fs
frqA = kA/TA # two sides frequency range
frqA = frqA[range(int(nA/2))] # one side frequency range
YA = np.fft.fft(yA)/nA # fft computing and normalization
YA = YA[range(int(nA/2))]

# analyze signal B

Fs = freqB # sample rate
Ts = 1.0/Fs; # sampling interval
ts = np.arange(0,tB[-1],Ts) # time vector
yB = data1B # the data to make the fft from
nB = len(yB) # length of the signal
kB = np.arange(nB)
TB = nB/Fs
frqB = kB/TB # two sides frequency range
frqB = frqB[range(int(nB/2))] # one side frequency range
YB = np.fft.fft(yB)/nB # fft computing and normalization
YB = YB[range(int(nB/2))]

# analyze signal C

Fs = freqC # sample rate
Ts = 1.0/Fs; # sampling interval
ts = np.arange(0,tC[-1],Ts) # time vector
yC = data1C # the data to make the fft from
nC = len(yC) # length of the signal
kC = np.arange(nC)
TC = nC/Fs
frqC = kC/TC # two sides frequency range
frqC = frqC[range(int(nC/2))] # one side frequency range
YC = np.fft.fft(yC)/nC # fft computing and normalization
YC = YA[range(int(nC/2))]

# analyze signal D

Fs = freqD # sample rate
Ts = 1.0/Fs; # sampling interval
ts = np.arange(0,tD[-1],Ts) # time vector
yD = data1D # the data to make the fft from
nD = len(yD) # length of the signal
kD = np.arange(nD)
TD = nD/Fs
frqD = kD/TD # two sides frequency range
frqD = frqD[range(int(nD/2))] # one side frequency range
YD = np.fft.fft(yD)/nD # fft computing and normalization
YD = YD[range(int(nD/2))]

# IIR FILTER 

filtered = []
for index, data in enumerate(data1D):
    if index == 0:
        filtered.append(data)
    else:
        Acoeff = 0.95
        Bcoeff = 0.05
        filtered.append(Acoeff*filtered[index-1] + Bcoeff*data)

# FFT of filtered

Fs = freqD # sample rate
Ts = 1.0/Fs; # sampling interval
# ts = np.arange(0,tD[-1],Ts) # time vector
yF = filtered # the data to make the fft from
nF = len(yF) # length of the signal
kF = np.arange(nF)
TF = nF/Fs
frqF = kF/TF # two sides frequency range
frqF = frqF[range(int(nF/2))] # one side frequency range
YF = np.fft.fft(yF)/nF # fft computing and normalization
YF = YF[range(int(nF/2))]

plt.figure()
plt.loglog(frqD,abs(YD),'black')
plt.loglog(frqF,abs(YF),'red')
plt.xlabel('Freq (Hz)')
plt.ylabel('|Y(freq)|')
plt.title("Signal D FFT Before and After Filtering (A=0.95,B=0.05)")
plt.legend(["Unfiltered", "Filtered"])

plt.show()