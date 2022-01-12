# Sayısal Loto
import random
s=0; ks=[]; bs=[]
for i in range(6):
  bs.append(random.randint(1,49))
for i in range(6):
  print("%d. tahmininiz. "%(i+1),end=''); ks.append(int(input()))
for i in range(6):
    if (ks[i] in bs):
        s+=1
print("\n%d tane doğru tahminde bulundunuz."%s)
