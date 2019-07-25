import csv
import os
import pyqrcode
import sys
import time


print('Johnson Controls Inc.')
print('QRCode Generator V.1.0')

#print ("This is the first ", sys.argv[0])
#print ("Number of arguments: ", len(sys.argv))
PNGScale=5
if len(sys.argv) > 1 :
    PNGScale=sys.argv[0]

currentDirectory = os.getcwd()
print('Looking for Qrcode.csv file')
time.sleep(1)
filepath=(currentDirectory + '\\Qrcodes.csv')
if not os.path.exists(filepath):
    print('Qrcode.csv file not found')
    time.sleep(5)
    sys.exit(0)

time.sleep(2)
print('Qrcode.csv file found. Verifying QrCodes directory and creating it if does not exist')
if not os.path.exists(currentDirectory+'\\Qrcodes'):
    print('Creating QRCodes directory')
    os.makedirs(currentDirectory+'\\Qrcodes')

time.sleep(2)
print('Generating QRCodes')
with open('Qrcodes.csv', "rt", encoding='ascii') as infile:
    read = csv.reader(infile, delimiter=';')
    #csvheading = next(read)
    i=0
    for row in read :

        i=i+1
        QRcode = pyqrcode.create(row[1])
        strTemp=currentDirectory+'\\Qrcodes\\'+str(i)+'-'+row[0]+'.png'
        print (strTemp)
        QRcode.png(strTemp,scale=PNGScale)
time.sleep(2)
print('Job Completed')
time.sleep(2)