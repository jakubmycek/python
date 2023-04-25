
import random
i=0
wyrazy=["ala","kot","auto","pies"]
wyraz = random.choice(wyrazy)
listawyrazu=wyraz.split()
długość=len(listawyrazu)
wyrazgracz=[]
for g in range(długość):
    wyrazgracz.append(_ )
while i != 10:
    print(listawyrazu)
    litera=str(input("podaj literę"))
    for j in range(len):
        if litera==listawyrazu[j]:
            wyrazgracz[j]=litera

    i=10

print("  ______")
print(" | /   |")
print(" |/    0")
print(" |    /|\ ")
print(" |    / \ ")
print(" | ")