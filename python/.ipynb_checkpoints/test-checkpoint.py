import serial
import csv

arduino_port = "COM16" #o uno runs at 9600 baud
fileName="C:/Users/lukas/Documents/fc.csv" #name of the CSV file generated
 
ser = serial.Serial(arduino_port, 115200)
ser.flushInput()
print("Connected to Arduino port:" + arduino_port)
file = open(fileName, "w")
print("Created file")
 
samples = 100000000 #how many samples to collect
print_labels = False
line = 0 #start at 0 because our header is 0 (not real data)
print(1 + float("   0.5"))
with open(fileName, "a", newline='') as csvfile:
        writer = csv.writer(csvfile,delimiter=",")
        writer.writerow("time,lat,long,alt,sats,magx,magy,magz,temp,pres,bar_alt,vert_vel,bat_state,counter".split(sep=","))
        line = line +1
while line <= samples:
   
    getData=ser.readline()
    data = str(getData[0:len(getData)-2].decode("utf-8"))
    #data=getData[0:][:-2]
    data = str(line) + "," + data
    print(data)
    data_list = data.split(sep=",")
 
    with open(fileName, "a", newline='') as csvfile:
        writer = csv.writer(csvfile,delimiter=",")
        writer.writerow(data_list)
        line = line +1
    
 
print("Data collection complete!")
file.close()