# e üzeri
import math
N=int(input("Terim sayısını giriniz: "))
x=eval(input("Hesaplanacak x değerini giriniz: ")); T=1; F=1
for i in range(1,N):
    F*=i; T+=x**i/F
print("\nSeri açılımı ile e üzeri x değeri: %0.5f"%T)
print("Komutla e üzeri x değeri: %0.5f"%math.exp(x))
