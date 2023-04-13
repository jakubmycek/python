import random
'''
print("hello world") #komentarz jedno linijkowy

komentarz wielo linijkowy


zmienna=178
a=3
zmienna2=12.67

tekst="essa"
tekst2='eiklen'
print(zmienna)

print("wartość zmiennej a to:", a , "ta liczba jest fajna")
print(f"wartość zmiennej tekst to {tekst}")
print("warrtość zmiennj zmnienna to :" +str(zmienna))
print('%.20f'%zmienna2)


imię=input("jak masz na imię?")
wiek=int(input('ile masz lat?'))
print(f'hello {imię}')
print(f'masz {wiek} lat')

ciag="napis" *20
print(ciag)

 
liczba=random.randint(-5, 5)

if liczba>0:
    print(f"liczba {liczba} jest większa od 0")
elif liczba==0:
    print(f"liczba {liczba} jest równa 0")
else:
    print(f"liczba {liczba} jest mniejza od 0")



a = int(input("podaj liczbę"))
if a%2==0:
    print(f"liczba {a} jest podzielna przez 2")
else:
    print (f"liczba {a}jest niepodzielna przez 2")
if a<0:
    a=a*-1
print(a)


for i in range(4):
    print(i)

for i in range(1,100):
    print(i)

for i in range(1,101,2):
    print(i)
for i in range(100,0,-1):
    print(i)

for a in "string":
    if a=="i":
        break
    print(a)
print("koniec")

for a in "string":
    if a=="i":
        continue
    print(a)
print("koniec")

for i in range(6):
    los=random.randint(1,50)
    print(f"wyl;osowana liczba {i+1} to {los}")

liczba1=0
while liczba1<10:
    print(liczba1)
    liczba1+=1
    


liczba2=int(input("podaj liczbę mniejszą od 0"))

while liczba2<=0:
    liczba2=int(input("podaj liczbę mniejszą od 0"))


def powitanie():
    print("czesć")

powitanie()
 
def powitanie_imienne(imię):
    print(f"cześć {imię}")

powitanie_imienne("kuba")

def dzielenie(a,b):
    if b==0:
        return
    else:
        return a/b
wynik=dzielenie(10,2)
print(wynik)

lista=[]
lista.append(10)


lista1=[1,2,3,4,5]
lista2=["a",2,"gdf"]
print(lista1[0])

for x in lista1:
    print(x)
print(*lista2)

print(set("jego imię to Eryk i Eryk jest jego imieniem".split()))

A=set(["anna","jan"])
B=set(["anna","grześ"])
print(A.intersection(B))
print(A.difference(B))
print(A.union(B))
'''

tupla=()
tupla1=(1,"de",45,6,"hg",3.14)
tupla2=("kot", [1,3,2,5], (36,4))
print(tupla2)

print(tupla1[0])
print(tupla2[0][2])
print(tupla1[:3])

# tupla1[1]=5    nie da sie zmieniać
# del tupla1[2]  nie da się zrobić

słownik={
    "kot":"cat",
    "pies":"dog"
    }
kontakty={
    "jaś": 123456789,
    "grześ": 213456798
}
print(kontakty["jaś"])

for imie, numer in kontakty.items():
    print(imie, numer)

if "jaś" in kontakty:
    print("jaś znajduje się w słowniku")