import random
wkp=["papier","kamień","nozyce"]
z=0
wyg=0
wyk=0
w = int(input("ileś gier(1)   czy    do iluś punktów(2)"))
if w==1:
    ileg=int(input("ile gier?"))
    for i in range(ileg):
        z=0
        while z==0:
            g=str(input("Papier, kamień, noyce!(p,k,n)"))
            if g!="p":
                Z=1
            if g!="k":
                z=1
            if g!="n":
                z=1
        k=random.choice(wkp)
        print(k)
        if g=="p":
            if k=="kamień":
                wyg=wyg+1
            if k=="nozyce":
                wyk=wyk+1
        if g=="k":
            if k=="papier":
                wyk=wyk+1
            if k=="nozyce":
                wyg=wyg+1
        if g=="n":
            if k=="kamień":
                wyk=wyk+1
            if k=="papier":
                wyg=wyg+1
else:
    ilep=int(input("do ilu punktów?"))
    while wyg!=ilep and wyk!=ilep:
        z=0
        while z==0:
            g=str(input("Papier, kamień, noyce!(p,k,n)"))
            if g!="p":
                Z=1
            if g!="k":
                z=1
            if g!="n":
                z=1
        k=random.choice(wkp)
        print(k)
        if g=="p":
            if k=="kamień":
                wyg=wyg+1
            if k=="nozyce":
                wyk=wyk+1
        if g=="k":
            if k=="papier":
                wyk=wyk+1
            if k=="nozyce":
                wyg=wyg+1
        if g=="n":
            if k=="kamień":
                wyk=wyk+1
            if k=="papier":
                wyg=wyg+1
if wyg>wyk:
    print("Wygrałeś!!!")
if wyg<wyg:
    print("Przegrałeś!!!")
if wyg==wyk:
    print("Remis!!!")
print(f"komputer   {wyk}  :  {wyg}    gracz")