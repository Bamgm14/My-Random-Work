import os
import time
a=os.getlogin()
b=os.getcwd()
os.system('echo Hello User:'+str(a)+'& echo Have You Heard Of The Pews? & ping -n 5 127.0.0.1 >nul')
c=open('HelpPews.vbs','w+')
c.write('x = msgbox ("Pews Is Waiting For You.",64,"Pewdiepie")\nx = msgbox ("Please Help Us Out",32,"Pewdiepie")')
c.close()
os.startfile(str(b)+'\\HelpPews.vbs')
time.sleep(5)
os.remove(str(b)+'\\HelpPews.vbs')
try:
    os.system('ping -n 7 127.0.0.1>nul & cd "C:\Program Files (x86)\Google\Chrome\Application" & chrome.exe https://www.youtube.com/watch?v=6Dh-RL__uN4 & chrome.exe https://www.youtube.com/subscription_center?add_user=PewDiePie')
except:
    os.system('ping -n 7 127.0.0.1>nul & cd "C:\Program Files\Mozilla Firefox" & firefox.exe https://www.youtube.com/watch?v=6Dh-RL__uN4 & firefox.exe https://www.youtube.com/subscription_center?add_user=PewDiePie')
os.system('echo Thank You, '+str(a)+' & ping -n 10 127.0.0.1>nul')
