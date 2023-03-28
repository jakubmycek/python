
print("podaj liczbę do przekonwertowania")
liczba1=float(input())
print("podaj jednostkę tej liczby")
jednostka1=input()
print("podaj jednostkę w której chcesz otrzymać wynik")
jednostka2=input()
if jednostka1=="mm":
    if jednostka2=="cm":
        liczba1=liczba1/10
    elif jednostka2=="dm":
        liczba1=liczba1/100
    elif jednostka2=="m":
        liczba1=liczba1/1000
    elif jednostka2=="km":
        liczba1=liczba1/1000000
elif jednostka1=="cm":
    if jednostka2=="mm":
        liczba1=liczba1*10
    elif jednostka2=="dm":
        liczba1=liczba1/10
    elif jednostka2=="m":
        liczba1=liczba1/100
    elif jednostka2=="km":
        liczba1=liczba1/100000
elif jednostka1=="dm":
    if jednostka2=="mm":
       liczba1=liczba1*100
    elif jednostka2=="cm":
        liczba1=liczba1*10
    elif jednostka2=="m":
        liczba1=liczba1/1000
    elif jednostka2=="km":
        liczba1=liczba1/1000000
elif jednostka1=="m":
    if jednostka2=="mm":
        liczba1=liczba1*1000
    elif jednostka2=="cm":
        liczba1=liczba1*100
    elif jednostka2=="dm":
        liczba1=liczba1*10
    elif jednostka2=="km":
        liczba1=liczba1/1000
elif jednostka1=="km":
    if jednostka2=="mm":
        liczba1=liczba1*1000
    elif jednostka2=="cm":
        liczba1=liczba1*100
    elif jednostka2=="dm":
        liczba1=liczba1*10
    elif jednostka2=="m":
        liczba1=liczba1*1000
elif jednostka1=="a":
    if jednostka2=="ha":
        liczba1=liczba1/100
    elif jednostka2=="cm2":
        liczba1=liczba1*1000000
    elif jednostka2=="m2":
        liczba1=liczba1*100
elif jednostka1=="ha":
    if jednostka2=="a":
        liczba1=liczba1*100
    elif jednostka2=="cm2":
        liczba1=liczba1*100000000
    elif jednostka2=="m2":
        liczba1=liczba1*10000
elif jednostka1=="cm2":
    if jednostka2=="a":
        liczba1=liczba1/1000000
    elif jednostka2=="ha":
        liczba1=liczba1/100000000
    elif jednostka2=="m2":
        liczba1=liczba1/10000
elif jednostka1=="m2":
    if jednostka2=="a":
        liczba1=liczba1/100
    elif jednostka2=="ha":
        liczba1=liczba1/10000
    elif jednostka2=="cm2":
        liczba1=liczba1*10000
elif jednostka1=="g":
    if jednostka2=="kg":
        liczba1=liczba1/1000
    elif jednostka2=="t":
        liczba1=liczba1*1000000
elif jednostka1=="kg":
    if jednostka2=="g":
        liczba1=liczba1*1000
    elif jednostka2=="t":
        liczba1=liczba1*1000
elif jednostka1=="t":
    if jednostka2=="g":
        liczba1=liczba1*100000
    elif jednostka2=="kg":
        liczba1=liczba1*1000    
elif jednostka1=="s":
    if jednostka2=="m":
        liczba1=liczba1/60
    elif jednostka2=="h":
        liczba1=liczba1/3600  
    elif jednostka2=="d":
        liczba1=liczba1/86400          
elif jednostka1=="m":
    if jednostka2=="s":
        liczba1=liczba1*60
    elif jednostka2=="h":
        liczba1=liczba1/60 
    elif jednostka2=="d":
        liczba1=liczba1/1440 
elif jednostka1=="h":
    if jednostka2=="s":
        liczba1=liczba1*3600
    elif jednostka2=="m":
        liczba1=liczba1*60  
    elif jednostka2=="d":
        liczba1=liczba1/24 
elif jednostka1=="d":
    if jednostka2=="s":
        liczba1=liczba1*86400
    elif jednostka2=="m":
        liczba1=liczba1*1440  
    elif jednostka2=="d":
        liczba1=liczba1*24  
elif jednostka1=="B":
    if jednostka2=="KB":
        liczba1=liczba1/1024
    elif jednostka2=="MB":
        liczba1=liczba1/1048576
    elif jednostka2=="GB":
        liczba1=liczba1/1073741824
    elif jednostka2=="TB":
        liczba1=liczba1/1099511627776   
elif jednostka1=="KB":
    if jednostka2=="B":
        liczba1=liczba1*1024
    elif jednostka2=="MB":
        liczba1=liczba1/1024
    elif jednostka2=="GB":
        liczba1=liczba1/1048576
    elif jednostka2=="TB":
        liczba1=liczba1/1073741824 
elif jednostka1=="B":
    if jednostka2=="KB":
        liczba1=liczba1/1024
    elif jednostka2=="MB":
        liczba1=liczba1/1048576
    elif jednostka2=="GB":
        liczba1=liczba1/1073741824
    elif jednostka2=="TB":
        liczba1=liczba1/1099511627776   


print(liczba1)