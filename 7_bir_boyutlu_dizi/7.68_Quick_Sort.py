# Quick Sort
import math
def hizli_siralama(a,sol,sag):
  i=sol; j=sag; pivot=a[math.floor((sol+sag)/2)]
  while (i<=j):
      while (a[i]<pivot):
          i+=1
      while (a[j]>pivot):
          j-=1
      if (i<=j):
