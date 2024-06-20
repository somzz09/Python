'''
open()
read()
readline()
write()
writeline()
close()
fseek()
ftell()
'''
fp=open("csa.txt","w")
if fp:
    print("file is created successfully")

fp.write("hi students welcome to cmrec\ntoday smart interviews session is cancelled")

fp.close()
