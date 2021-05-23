import os
import shutil
## partha added comments
src = r'E:\Python'
dst = r'C:\Users\partha\Documents\newPython'
fnames = os.listdir(src)
print(os.path)
for eachf in fnames:

    print(eachf)
    try:
        (f,e) = eachf.split('.')
        if (e == 'py'):
            shutil.copy(eachf,dst)
    except:
        pass
