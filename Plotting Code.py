import numpy as np
import os
import pylab as plt
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.signal
#from scipy import asarray as ar,exp

from scipy.signal import butter,filtfilt
# Filter requirements.
T = 5.0         # Sample Period
fs = 30.0       # sample rate, Hz
cutoff = 1      # desired cutoff frequency of the filter, Hz ,      slightly higher than actual 1.2 Hz
nyq = 0.5 * fs  # Nyquist Frequency
order = 2       # sin wave can be approx represented as quadratic
n = int(T * fs) # total number of samples

fs2 = 30.0       # sample rate, Hz
cutoff2 = 0.5      # desired cutoff frequency of the filter, Hz ,      slightly higher than actual 1.2 Hz
order2 = 2       # sin wave can be approx represented as quadratic




path = (r"C:\Users\sunny\OneDrive\Desktop\My Folder\Singapore University of Technology and Design\Year 1\Term 2\Honours Session 2\Project\Bio-Inspired Batoid Underwater Robot\Data\Data Storage\sd_card_data1.txt")
a=np.genfromtxt(path, delimiter=';')
#head, tail = os.path.split(path)
#print (tail)
#speed = tail[0:3]
#run = tail[4:5]

n=len(a)

print(n)
print(a)

#start=0
#stop=20000
#time_steps = np.linspace(0,n*0.001, n)
#x = time_steps
#print (x)
#offset = np.mean(a[:2000,1])
#print ('........')
#print (offset)
#aft_offset=[]
#aft_offset = (a[:, 1] - offset)*1000

print ('........')

#plt.figure()
#plt.plot(a[:,0]/1000, a[:,1]*3.9/1024,'r', label='L1 (left side)')
#plt.plot(a[:,0]/1000, a[:,2]*3.9/1024,'b', label='L2 (left back)')
#plt.plot(a[:,0]/1000, a[:,3]*3.9/1024,'g', label='R1 (right side)')
#plt.plot(a[:,0]/1000, a[:,4]*3.9/1024,'k', label='R2 (right back)')
#plt.plot(a[:,0]/1000, a[:,5]*3.7/1024,'r', label='Peak L1 (left side)')
#plt.plot(a[:,0]/1000, a[:,6]*3.7/1024,'b', label='Peak L2 (left back)')
#plt.plot(a[:,0]/1000, a[:,7]*3.7/1024,'g', label='Peak L1 (right side)')
#plt.plot(a[:,0]/1000, a[:,8]*3.7/1024,'k', label='Peak L2 (right back)')
#plt.plot(a[:,0]/1000, a[:,5]*3.7/1024,'g', label='posL')
#plt.plot(a[:,0]/1000, a[:,6]*3.7/1024,'k', label='posR')
b = []

a[:,5] = a[:,5]-90
a[:,6] = a[:,6]-90
a[:,4] = a[:,4]

for i in range(len(a)):
    b.append(a[i,4] - 2*max(a[i,5], a[i,6]))
    
def butter_lowpass_filter(data, cutoff, fs, order):
    normal_cutoff = cutoff / nyq
    # Get the filter coefficients 
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y
    
b = butter_lowpass_filter(a[:,4], cutoff, fs, order)
c = butter_lowpass_filter(a[:,2], cutoff2, fs2, order2)
    
plt.figure()
#plt.plot(a[:,0]/1000, a[:,1]*3.9/1024,'r', label='L1 (left side)')
plt.plot(a[:,0]/1000, a[:,2],'b', label='L2 (left back)')
#plt.plot(a[:,0]/1000, c,'c', label='Corrected L2 (left back)')
#plt.plot(a[:,0]/1000, a[:,2] - 0.5*a[:,5],'c', label='Corrected L2 (left back)2')
#plt.plot(a[:,0]/1000, a[:,3]*3.9/1024,'g', label='R1 (right side)')
plt.plot(a[:,0]/1000, a[:,4],'y', label='R2 (right back)')
#plt.plot(a[:,0]/1000, b,'r', label='Corrected R2 (right back)')
plt.plot(a[:,0]/1000, 20*np.sin(1.*(np.arcsin(a[:,6]/21))+0.3),'r', label='Corrected R2 (right back)2')
#plt.plot(a[:,0]/1000, a[:,5]*3.7/1024,'r', label='Peak L1 (left side)')
#plt.plot(a[:,0]/1000, a[:,6]*3.7/1024,'b', label='Peak L2 (left back)')
#plt.plot(a[:,0]/1000, a[:,7]*3.7/1024,'g', label='Peak L1 (right side)')
#plt.plot(a[:,0]/1000, a[:,8]*3.7/1024,'k', label='Peak L2 (right back)')
plt.plot(a[:,0]/1000, a[:,5],'g', label='posL')
plt.plot(a[:,0]/1000, a[:,6],'k', label='posR')

"""
plt.plot(a[:,0]/1000, a[:,4]*5.0/1024,'g', label='R2')No do
plt.plot(a[:,0]/1000, a[:,5]*5.0/1024,'k', label='peakL1')
plt.plot(a[:,0]/1000, a[:,6]*5.0/1024,'b', label='peakL2')
plt.plot(a[:,0]/1000, a[:,7]*5.0/1024,'r', label='peakR1')
plt.plot(a[:,0]/1000, a[:,8]*5.0/1024,'g', label='peakR2')
"""

plt.xlabel('Time (s)', fontsize = 30)
plt.ylabel('Output voltage (V)', fontsize = 30)
plt.legend(loc = (0.8,0.9), fontsize = 15)
#plt.figure()
#plt.plot(a[:,0], scipy.signal.savgol_filter(aft_offset, 101, 2), 'k')

plt.title('Title', fontsize = 30) 
plt.tick_params(axis='both', direction= 'in', which='major', length=5, width = 2, color='red', pad=10, labelsize = 25, labelcolor='k')
