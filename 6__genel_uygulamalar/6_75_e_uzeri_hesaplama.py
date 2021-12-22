# e üzeri hesaplama binom açılımı
print("exp(x)=Lim(1+x/n)^n\n")
x=eval(input("x: ")); n=eval(input("n: "))
sonuc=(1+x)**n ; print("\nexp(%f)=%f"%(x,sonuc))
