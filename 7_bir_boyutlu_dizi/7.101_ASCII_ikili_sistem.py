# Mesaj-Binary (ASCII)
m=input("Mesaj: "); print("\nİkili (ASCII) kodlama: ",end='')
for i in range(0,len(m)):
  print("%s"%bin(ord(m[i]))[2:],end='')
