import os
a=open("JPG.txt",'w')
for root, dirs, files in os.walk(r"C:\Users\Bamgm14"):
    for file in files:
        if file.endswith(".jpg"):
            print(os.path.join(root, file))
            a.write(os.path.join(root, file)+'\n')
a.close()
