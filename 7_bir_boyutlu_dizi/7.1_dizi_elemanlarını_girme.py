# Dizi Elemanlarını Girme
A=[]
N=int(input("Dizinin eleman giriniz: "))
for i in range (0,N):
  print("A(%d)= "%(i+1),end='')
  A.append(int(input()))
