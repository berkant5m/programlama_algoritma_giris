# Basamaklara Ayrıştırma
s=input("Tamsayı: "); print("\nBasamaklar\n----------"); n=len(s)
for i in range(n-1,-1,-1):
  print("%d -> %c"%(10**(n-i-1),s[i]))
