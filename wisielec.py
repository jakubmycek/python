
import random
i=0
wyrazy=["mysz","kot","auto","pies","mama","tata","dom","oko","wzrok","telewizor","rower","statek","samolot","deskorolka","rolki","hulajnoga","babcia","dziadek","cocia","wujek","kuzyn","kuzynka","brat","siostra","nos","usta","policzek","brew","włosy","czoło","chomik","papuga","słoń","ryba","rekin","blok","namiot","igloo","telefon","pilot","słuchawki","laptop","konsola","klawiatura","mysz"]
wyraz = random.choice(wyrazy)
listawyrazu=list(wyraz)
długość=len(listawyrazu)
wyrazgracz=[]
długość2=len(wyrazgracz)
listaliter=[]
while długość > długość2:
    wyrazgracz.append("_")
    długość2=len(wyrazgracz)
while i <= 10:
    print(listaliter)
    print(wyrazgracz)
    litera=str(input("podaj literę"))
    if litera in listaliter:
        None
    else:
        listaliter.append(litera)
    j=0
    c=1
    for j in range(długość):
        if litera == listawyrazu[j]:
            wyrazgracz[j]=litera
            c=0
    if listawyrazu==wyrazgracz:
        print(listawyrazu)
        print("wygrana")
        break
    if c!=0:
            i=i+1
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
        print(listawyrazu)
        print("przegrana")
'''
    print("  ______")
    print(" | /   |")
    print(" |/    0")
    print(" |    /|\ ")
    print(" |    / \ ")
    print(" | ")
'''