import numpy as np
import matplotlib.pyplot as plot
import math


# Get x values of the sine wave
time        = np.arange(0, 10, 0.01);
# Amplitude of the sine wave is sine of a variable like time
# amplitude   = np.sin(2*math.pi*frequency*time)

y = np.zeros(time.size)
print(y.size)



higher_amp = 40
lower_amp = 10
higher_freq = 1.5
lower_freq = 0.1
freqR = lower_freq
amplitudeR = 0
frequency_Sum = 0 

for i in range(1,y.size):
	my_time = time[i]
	frequency_Sum = freqR+frequency_Sum
	theta = 2.0 * math.pi * frequency_Sum*(my_time-time[i-1])
	if math.cos(theta)<0:
		freqR = higher_freq
		if math.sin(theta)<0:
			amplitudeR = higher_amp
		else:
			amplitudeR = lower_amp
	else:
		freqR = lower_freq;
		if math.sin(theta)>0:
			amplitudeR = lower_amp
		else:
			amplitudeR = higher_amp
	y[i] = (amplitudeR / 2) * math.sin(theta)

# Plot a sine wave using time and amplitude obtained for the sine wave

plot.plot(time, y)

 
# Give a title for the sine wave plot

plot.title('Sine wave')


# Give x axis label for the sine wave plot

plot.xlabel('Time')

# Give y axis label for the sine wave plot

plot.ylabel('Amplitude = sin(time)')

plot.grid(True, which='both')

plot.axhline(y=0, color='k')

plot.show()

# Display the sine wave

plot.show()