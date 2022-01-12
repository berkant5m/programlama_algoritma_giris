# Tek Basamak
r=["sıfır","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
x=int(input("Tek basamaklı tamsayı giriniz: "))
print("\nGirdiğiniz sayı => ",end='')
if (x<0):
   print("eksi ",end='')
print(r[abs(x)])
