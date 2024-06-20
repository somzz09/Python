fp=open("word.txt","w")
if fp:
    print("Successfully Opened")
fp.write("i")
fp.write("a")
fp.write(" ")
fp.write("Silence above all")
fp.close()