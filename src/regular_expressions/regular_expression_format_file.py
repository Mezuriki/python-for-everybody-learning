#app_slidfjiowejfieowfj.jpg -> app.jpg
import re
a = 'app_slidfjiowejfieowfj.jpg'
b = re.split(r'([\S]+)_.*([.].*)',a)
c = re.findall(r'([\S]+)_.*([.].*)',a)
d = re.split(r'[._]',a)
print(b[1]+b[2])
print(c)
print(d[0]+'.'+d[2])