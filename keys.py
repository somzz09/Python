def invert_content(dic):
    invert_dic={}
    invert_dic={k:v for v,k in dic.items()}
    return invert.dic
n=int(input("Enter no.of values"))
dic={}
for i in range(n):
    key=input("Enter key")
    value=input("Enter value")
    dic[key]=value
print(dic)
print("After Inversion")
print(invert_content(dic))