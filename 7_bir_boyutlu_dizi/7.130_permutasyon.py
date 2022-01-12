# Permütasyon
import itertools
k=input("Kelime: "); print("\nPermütasyonlar:")
p=itertools.permutations(k)
for i in list(p):
  print(i)
