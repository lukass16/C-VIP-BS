import serial
import csv
from multiprocessing import Process
from threading import Thread
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.animation import FuncAnimation
from itertools import count


class SerialReadProcess:  
    def __init__(self):
        self._running = True

    def terminate(self):  
        self._running = False  

    def run(self):
        arduino_port = "COM16" #o uno runs at 9600 baud
        fileName="C:/Users/lukas/Documents/fc.csv" #name of the CSV file generated
        ser = serial.Serial(arduino_port, 115200)
        ser.flushInput()
        print("Connected to Arduino port:" + arduino_port)
        file = open(fileName, "w")
        print("Created file")
        samples = 100000000 #how many samples to collect
        line = 0 #start at 0 because our header is 0 (not real data)
        with open(fileName, "a", newline='') as csvfile:
            writer = csv.writer(csvfile,delimiter=",")
            writer.writerow("time,lat,long,alt,sats,magx,magy,magz,temp,pres,bar_alt,vert_vel,bat_state,counter".split(sep=","))
            line = line +1

        while self._running and line <= samples:
            getData=ser.readline()
            data = str(getData[0:len(getData)-2].decode("utf-8"))
            data = str(line) + "," + data
            print(data)
            data_list = data.split(sep=",")
            with open(fileName, "a", newline='') as csvfile:
                writer = csv.writer(csvfile,delimiter=",")
                writer.writerow(data_list)
                line = line + 1
        print("Data collection complete!")
        file.close()
        
SerialRead = SerialReadProcess()
#Create 
SerProcess = Process(target=SerialRead.run) 
#Start Thread 
SerProcess.start()

plt.style.use('seaborn')
plt.style.use('dark_background')
 
#mpl.rcParams['font.family'] = 'Avenir'
mpl.rcParams['font.size'] = 18
mpl.rcParams['axes.linewidth'] = 1
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['xtick.major.size'] = 5
mpl.rcParams['xtick.major.width'] = 0.5
mpl.rcParams['ytick.major.size'] = 5
mpl.rcParams['ytick.major.width'] = 0.5
#fig = plt.figure(figsize=(5, 4))
#atrums = fig.add_subplot(111)
 
fig, ([augstums, atrums], [tt, bilde]) = plt.subplots(nrows=2, ncols=2, figsize=(10,12), linewidth=5, edgecolor="#4d7791")
#index = count()
 
def animate(i):
    data = pd.read_csv('C:/Users/lukas/Documents/fc.csv')
    a = data['time']
    b = data['lat']
    c = data['long']
    d = data['alt']  
    e = data['sats']
    f = data['magx']
    g = data['magy']
    h = data['magz']
    i = data['temp']
    j = data['pres']
    k = data['bar_alt']
    l = data['vert_vel']
    m = data['bat_state']
    n = data['counter']
 
    
    aa=pd.DataFrame(data=a)
    bb=pd.DataFrame(data=b)
    cc=pd.DataFrame(data=c)
    dd=pd.DataFrame(data=d)
    ee=pd.DataFrame(data=e)
    ff=pd.DataFrame(data=f)
    gg=pd.DataFrame(data=g)
    hh=pd.DataFrame(data=h)
    ii=pd.DataFrame(data=i)
    jj=pd.DataFrame(data=j)
    kk=pd.DataFrame(data=k)
    ll=pd.DataFrame(data=l)
    mm=pd.DataFrame(data=m)
    nn=pd.DataFrame(data=n)
    
    
 
    aaa = ("%.1f" % (aa['time'].iloc[-1]))
    bbb = ("%.0f" % (bb['lat'].iloc[-1]))
    ccc = ("%.0f" % (cc['long'].iloc[-1]))
    ddd = ("%.1f" % (dd['alt'].iloc[-1]))
    eee = ("%.1f" % (ee['sats'].iloc[-1]))
    fff = ("%.1f" % (ff['magx'].iloc[-1]))
    ggg = ("%.1f" % (gg['magy'].iloc[-1]))
    hhh = ("%.1f" % (hh['magz'].iloc[-1]))
    iii = ("%.1f" % (ii['temp'].iloc[-1]))
    jjj = ("%.1f" % (jj['pres'].iloc[-1]))
    kkk = ("%.1f" % (kk['bar_alt'].iloc[-1]))
    lll = ("%.1f" % (ll['vert_vel'].iloc[-1]))
    mmm = ("%.1f" % (mm['bat_state'].iloc[-1]))
    nnn = ("%.1f" % (nn['counter'].iloc[-1]))
    
 
 
    atrums.cla()
    augstums.cla()
  
    plt.tight_layout() 
    augstums.plot(a, d, color='#a5c6d4', linewidth=2) # #a88ca7 white #f0d5ef black
    augstums.set_title('h= ' + str(ddd) + 'm', fontsize=50)
    augstums.grid(False)
 
    #plotting mag for tests
    plt.tight_layout()
    atrums.plot(a, g, color='#a88ca7', linewidth=2) # #a88ca7 white #f0d5ef black
    atrums.set_title('v= ' + str(ggg) + 'm/s', fontsize=50)
    atrums.grid(False)
 
 
   
    
    #TABULA
    data = [[aaa],[bbb],[ccc],[ddd],[eee],[fff],[ggg],[hhh],[iii],[jjj],[kkk],[lll],[mmm],[nnn]]
    rows = ('Laiks', 'lat', 'lng', 'alt', 'sats', 'magx','magy','magz','temp','pres','bar_alt','vert_vel','bat_state','counter')
    cell_colors = [['tab:grey'],  ['tab:grey'], ['tab:grey'], ['tab:grey'], ['tab:grey'],['tab:grey'], ['tab:grey'], ['tab:grey'],
                   ['tab:grey'], ['tab:grey'], ['tab:grey'], ['tab:grey'], ['tab:grey'], ['tab:grey']]
 
    tt.set_axis_off() 
    table = tt.table( 
        cellText = data, 
        rowLabels = rows,  
        rowColours =["#1b261e"] * 14,
        cellColours = cell_colors,
        cellLoc ='center',
        colWidths = [0.15, 0.25],
        loc ='center') 
 
    #the_table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.set_fontsize(12)
    table.scale(2, 2)
 
    #tt.set_title('Lidojums',fontsize=25) 
    #set_va('top')
    #set_ha('center')
 
#GPS KARTE
    #bilde.set_axis_off()
    #image = cv2.imread("C:/Users/lukas/Untitled Folder/kipsala-karte.png")
    #im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
    #resized_img_1 = cv2.resize(im_rgb, (40,40))
    # x min=0 x max=40 
    # y min=0 y max=40
    # kxmin kxmax
    # kymin kymax
    # kx ky
    # x y
    # xmax/(kxmax-kxmin) * kx == x 
    # ymax/(kymax-kymin) * ky == y
    #bilde.imshow(resized_img_1)
 

ani = FuncAnimation(plt.gcf(), animate, interval=1000)
 
  

