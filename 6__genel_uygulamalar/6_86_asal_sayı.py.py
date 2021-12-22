Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Asal Sayılar
print("Belirtilen aralıktaki ASAL sayılar\n"
n=int(input("Üst sınır:"));print("\n+++ ASAL SAYILAR +++\n");
for i in range (2,n+1):
    s=0
    for j in range (1,i+1):
        if (i%j==0):
            s=s+1
    if (s==2):
        print("%d\t"%i,end='')