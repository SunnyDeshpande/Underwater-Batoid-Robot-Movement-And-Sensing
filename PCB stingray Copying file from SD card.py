import serial
import numpy

OutVoltage=[]


arduinoData = serial.Serial('COM5', 9600) #creating our serial object called arduinoData
filepath = r"C:\Users\sunny\OneDrive\Desktop\My Folder\Singapore University of Technology and Design\Year 1\Term 2\Honours Session 2\Project\Bio-Inspired Batoid Underwater Robot\Data\sd_card_data.txt"
file = open(filepath, 'a', errors='ignore')

while True: #while loop that loops forever
    while (arduinoData.inWaiting()==0): #Wait untill there is data
       pass
        
    #arduinoString = arduinoData.readline() #Read the line of text from serial port
    arduino_data = arduinoData.readline()
    dataline = str(arduino_data[0:len(arduino_data)].decode())
    
    #dataline = arduinoData.readline().split(';')   #Split it into an array called dataArray
    print(dataline)
    file.write(dataline)
             
file.close()