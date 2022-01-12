# Insertion sort
print("Diziyi [a b c d] şeklinde giriniz!")
a=[int(i) for i in input().split()] ; n=len(a)
for i in range(1,n):
  g=a[i]; j=i-1
  while ((j>-1) & (a[j]>g)):
      a[j+1]=a[j]; j=j-1; a[j+1]=g
print("\nSıralı dizi:\n------------")
for i in range(n):
  print("%d\t"%a[i],end='')
