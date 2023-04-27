
import random
i=0
wyrazy=["ala","kot","auto","pies"]
wyraz = random.choice(wyrazy)
listawyrazu=list(wyraz)
długość=len(listawyrazu)
wyrazgracz=[]
długość2=len(wyrazgracz)
while długość > długość2:
    wyrazgracz.append("_")
    długość2=len(wyrazgracz)
while i <= 10:
    print(listawyrazu)
    print(wyrazgracz)
    litera=str(input("podaj literę"))
    for j in range(długość):
        c=0
        if litera==listawyrazu[j] and litera!=wyrazgracz[j]:
            wyrazgracz[j]=litera
            c=c+1
    if listawyrazu==wyrazgracz:
        print("wygrana")
    if i==1:
        print("  ")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
    if i==2:
        print("  ______")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
    if i==3:
        print("  ______")
        print(" | /")
        print(" |/")
        print(" |")
        print(" |")
        print(" |")
    if i==4:
        print("  ______")
        print(" | /   |")
        print(" |/")
        print(" |")
        print(" |")
        print(" |")
    if i==5:
        print("  ______")
        print(" | /   |")
        print(" |/    0")
        print(" |")
        print(" |")
        print(" |")
    if i==6:
        print("  ______")
        print(" | /   |")
        print(" |/    0")
        print(" |     |")
        print(" |")
        print(" |")
    if i==7:
        print("  ______")
        print(" | /   |")
        print(" |/    0")
        print(" |    /|")
        print(" |")
        print(" |")
    if i==8:
        print("  ______")
        print(" | /   |")
        print(" |/    0")
        print(" |    /|\ ")
        print(" |")
        print(" |")
    if i==9:
        print("  ______")
        print(" | /   |")
        print(" |/    0")
        print(" |    /|\ ")
        print(" |    /")
        print(" |")
    if i==10:
        print("  ______")
        print(" | /   |")
        print(" |/    0")
        print(" |    /|\ ")
        print(" |    / \ ")
        print(" | ")
        print("przegrana")
    if c==0:
            i=i+1
'''
    print("  ______")
    print(" | /   |")
    print(" |/    0")
    print(" |    /|\ ")
    print(" |    / \ ")
    print(" | ")
'''