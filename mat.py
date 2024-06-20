def read_mat(A,r,c):
    for i in range(r):
        t=[]
        for j in range(c):
            val=int(input(f"enter the a[{i}][{j}] value"))
            t.append(val)
            A.append(t)
matA=[]
read_mat(matA,2,2)

def display_mat(A,r,c):
  for i in A:
      print(i)
display_mat(matA, 2, 2)