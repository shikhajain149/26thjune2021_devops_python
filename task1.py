import time
import psutil 
from psutil._common import bytes2human
import platform
import os
from getmac import get_mac_address
import subprocess

description = '''
Press 1 to Check current time and Date :- 
Press 2 to Check RAM Size of Your current OS  :- 
Press 3 to KNow Name of YOur current OS :- 
Press 4 to Check What is MAc Address of YOur lapTOP/PC/VM/CLoudVM :- 
Press 5 to create one directory IN your Desktop :- 
Press 6 to Restart Your current OS :- 
Press 7 to Print list of all available Wifi in your laptop Range :-
Press 8 to RUn another code in Your current folder  :-  
'''


user_input = eval(input('Enter number between 1 to 8:'))
if user_input==1:
  mytime=time.ctime()
  print("current date and time IS ",mytime)

elif user_input==2:
 mem_usage = psutil.virtual_memory()
 total_in_human_format = bytes2human(mem_usage[0])
 print("Size of RAM is ",total_in_human_format)

elif user_input==3:
    print(platform.system())
elif user_input==4:
    mac = get_mac_address()
    print("MAC address is",mac)
elif user_input==5:
    a=input('Enter the name of Directory:')
    path = os.path.join("C:/Users/32/Desktop/",a)
    os.mkdir(path)
    print("Directory '% s' created" % a)
elif user_input==6:
    os.system("shutdown /r /t 1")
elif user_input==7:
    devices = subprocess.check_output(['netsh','wlan','show','network'])
    devices = devices.decode('ascii')
    devices= devices.replace("\r","")
    print(devices)
elif user_input==8:
    os.system('practice.py
else 
   print("Check your input")
