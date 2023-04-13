import random
lista=[1,2,3,4,5,6,7,8,9]
wkp=0
i=0
A1=" "
A2=" "
A3=" "
B1=" "
B2=" "
B3=" "
C1=" "
C2=" "
C3=" "
print("   1   2   3")
print(f"A  {A1} | {A2} | {A3} ")
print("  -----------")
print(f"B  {B1} | {B2} | {B3} ")
print("  -----------")
print(f"C  {C1} | {C2} | {C3} ")
while(wkp==0):
    i=i+1
    kordyG=input("podaj kordy")
    if kordyG=="A1":
        A1="x"
        lista[0]=0
    elif kordyG=="A2":
        A2="x"
        lista[1]=0
    elif kordyG=="A3":
        A3="x"
        lista[2]=0
    elif kordyG=="B1":
        B1="x"
        lista[3]=0
    elif kordyG=="B2":
        B2="x"
        lista[4]=0
    elif kordyG=="B3":
        B3="x"
        lista[5]=0
    elif kordyG=="C1":
        C1="x"
        lista[6]=0
    elif kordyG=="C2":
        C2="x"
        lista[7]=0
    elif kordyG=="C3":
        C3="x"
        lista[8]=0
    kordyK=0
    if lista[0]!=0 or lista[1]!=0 or lista[2]!=0 or lista[3]!=0 or lista[4]!=0 or lista[5]!=0 or lista[6]!=0 or lista[7]!=0 or lista[8]!=0:
        while kordyK==0:
            kordyK=int(random.choice(lista))
        if kordyK==1:
            A1="o"
            lista[0]=0
        elif kordyK==2:
            A2="o"
            lista[1]=0
        elif kordyK==3:
            A3="o"
            lista[2]=0
        elif kordyK==4:
            B1="o"
            lista[3]=0
        elif kordyK==5:
            B2="o"
            lista[4]=0
        elif kordyK==6:
            B3="o"
            lista[5]=0
        elif kordyK==7:
            C1="o"
            lista[6]=0
        elif kordyK==8:
            C2="o"
            lista[7]=0
        elif kordyK==9:
            C3="o"
            lista[8]=0
    print("   1   2   3")
    print(f"A  {A1} | {A2} | {A3} ")
    print("  -----------")
    print(f"B  {B1} | {B2} | {B3} ")
    print("  -----------")
    print(f"C  {C1} | {C2} | {C3} ")
    if i>=3:
        if A1=="x" and A2=="x" and A3=="x":
            print("Wygrałeś!!!")
            wkp=1
        if A1=="o" and A2=="o" and A3=="o":
            print("Przegarłeś!!!")
            wkp=1
        if B1=="x" and B2=="x" and B3=="x":
            print("Wygrałeś!!!")
            wkp=1
        if B1=="o" and B2=="o" and B3=="o":
            print("Przegarłeś!!!")
            wkp=1
        if C1=="x" and C2=="x" and C3=="x":
            print("Wygrałeś!!!")
            wkp=1
        if C1=="o" and C2=="o" and C3=="o":
            print("Przegarłeś!!!")
            wkp=1
        if A1=="x" and B1=="x" and C1=="x":
            print("Wygrałeś!!!")
            wkp=1
        if A1=="o" and B1=="o" and C1=="o":
            print("Przegarłeś!!!")
            wkp=1
        if A2=="x" and B2=="x" and C2=="x":
            print("Wygrałeś!!!")
            wkp=1
        if A2=="o" and B2=="o" and C2=="o":
            print("Przegarłeś!!!")
            wkp=1
        if A3=="x" and B3=="x" and C3=="x":
            print("Wygrałeś!!!")
            wkp=1
        if A3=="o" and B3=="o" and C3=="o":
            print("Przegarłeś!!!")
            wkp=1
        if A1=="x" and B2=="x" and C3=="x":
            print("Wygrałeś!!!")
            wkp=1
        if A1=="o" and B2=="o" and C3=="o":
            print("Przegarłeś!!!")
            wkp=1
        if A3=="x" and B2=="x" and C1=="x":
            print("Wygrałeś!!!")
            wkp=1
        if A3=="o" and B2=="o" and C1=="o":
            print("Przegarłeś!!!")
            wkp=1
        if lista[0]==0 and lista[1]==0 and lista[2]==0 and lista[3]==0 and lista[4]==0 and lista[5]==0 and lista[6]==0 and lista[7]==0 and lista[8]==0:
            print("remis")
            wkp=1