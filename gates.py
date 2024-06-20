def AND(a,b):
    if a==1 and b==1:
        return True
    return False


#print(AND(1,1))
print("A=True | B=True | A and B="+str(AND(1,1)))
print("A=True | B=False | A and B="+str(AND(1,0)))
print("A=False | B=True | A and B="+str(AND(0,1)))
print("A=False | B=False | A and B="+str(AND(0,0)))