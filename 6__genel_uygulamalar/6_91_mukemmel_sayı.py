# Mükemmel Sayı 
s=int(input("Tamsayı:")); t=0
for i in range (1,s):
    if (s%i==0):
        t+=i
if (s==t):
    print("Mükemmel sayı")
else:
    print("Mükemmel sayı değil")
