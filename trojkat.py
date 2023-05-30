import random
A6=" "
B6=" "
B5=" "
C6=" "
C5=" "
C4=" "
D6=" "
D5=" "
D4=" "
D3=" "
E6=" "
E5=" "
E4=" "
E3=" "
E2=" "
F6=" "
F5=" "
F4=" "
F3=" "
F2=" "
F1=" "
G6=" "
G5=" "
G4=" "
G3=" "
G2=" "
H6=" "
H5=" "
H4=" "
H3=" "
I6=" "
I5=" "
I4=" "
J6=" "
J5=" "
K6=" "
listakordów=["A6","B6","B5","C6","C5","C4","D6","D5","D4","D3","E6","E5","E4","E3","E2","F6","F5","F4","F3","F2","F1","G6","G5","G4","G3","G2","H6","H5","H4","H3","I6","I5","I4","J6","J5","K6"]

for i in range(36):
    print("        A   B   C   D   E   F   G   H   I   J   K")
    print("                           ___")
    print(f"1                         | {F1} |")
    print("                       -----------")
    print(f"2                     | {E2} | {F2} | {G2} |")
    print("                   -------------------")
    print(f"3                 | {D3} | {E3} | {F3} | {G3} | {H3} |")
    print("               ---------------------------")
    print(f"4             | {C4} | {D4} | {E4} | {F4} | {G4} | {H4} | {I4} |")
    print("           -----------------------------------")
    print(f"5         | {B5} | {C5} | {D5} | {E5} | {F5} | {G5} | {H5} | {I5} | {J5} |")
    print("       -------------------------------------------")
    print(f"6     | {A6} | {B6} | {C6} | {D6} | {E6} | {F6} | {G6} | {H6} | {I6} | {J6} | {K6} |")
    print("     -----------------------------------------------")
    wkmp=0
    while wkmp==0:
        gracz=str(input("podaj kordy"))
        if gracz in listakordów:
            wkmp=1
    z=0
    while z==0:
        for i in range(36):
            if gracz==listakordów[i]:
                listakordów[i]=0
                z=1
    if gracz=="A6":
        A6="●"
    if gracz=="B6":
        B6="●"
    if gracz=="B5":
        B5="●"
    if gracz=="C6":
        C6="●"
    if gracz=="C5":
        C5="●"
    if gracz=="C4":
        C4="●"
    if gracz=="D6":
        D6="●"
    if gracz=="D5":
        D5="●"
    if gracz=="D4":
        D4="●"
    if gracz=="D3":
        D3="●"
    if gracz=="E6":
        E6="●"
    if gracz=="E5":
        E5="●"
    if gracz=="E4":
        E4="●"
    if gracz=="E3":
        E3="●"
    if gracz=="E2":
        E2="●"
    if gracz=="F6":
        F6="●"
    if gracz=="F5":
        F5="●"
    if gracz=="F4":
        F4="●"
    if gracz=="F3":
        F3="●"
    if gracz=="F2":
        F2="●"
    if gracz=="F1":
        F1="●"
    if gracz=="G6":
        G6="●"
    if gracz=="G5":
        G5="●"
    if gracz=="G4":
        G4="●"
    if gracz=="G3":
        G3="●"
    if gracz=="G2":
        G2="●"
    if gracz=="H6":
        H6="●"
    if gracz=="H5":
        H5="●"
    if gracz=="H4":
        H4="●"
    if gracz=="H3":
        H3="●"
    if gracz=="I6":
        I6="●"
    if gracz=="I5":
        I5="●"
    if gracz=="I4":
        I4="●"
    if gracz=="J6":
        J6="●"
    if gracz=="J5":
        J5="●"
    if gracz=="K6":
        K6="●"
    wkmp2=0
    while wkmp2==0:
        komputer=random.choice(listakordów)
        if komputer!=0:
            wkmp2=1
    if komputer=="A6":
        A6="○"
    if komputer=="B6":
        B6="○"
    if komputer=="B5":
        B5="○"
    if komputer=="C6":
        C6="○"
    if komputer=="C5":
        C5="○"
    if komputer=="C4":
        C4="○"
    if komputer=="D6":
        D6="○"
    if komputer=="D5":
        D5="○"
    if komputer=="D4":
        D4="○"
    if komputer=="D3":
        D3="○"
    if komputer=="E6":
        E6="○"
    if komputer=="E5":
        E5="○"
    if komputer=="E4":
        E4="○"
    if komputer=="E3":
        E3="○"
    if komputer=="E2":
        E2="○"
    if komputer=="F6":
        F6="○"
    if komputer=="F5":
        F5="○"
    if komputer=="F4":
        F4="○"
    if komputer=="F3":
        F3="○"
    if komputer=="F2":
        F2="○"
    if komputer=="F1":
        F1="○"
    if komputer=="G6":
        G6="○"
    if komputer=="G5":
        G5="○"
    if komputer=="G4":
        G4="○"
    if komputer=="G3":
        G3="○"
    if komputer=="G2":
        G2="○"
    if komputer=="H6":
        H6="○"
    if komputer=="H5":
        H5="○"
    if komputer=="H4":
        H4="○"
    if komputer=="H3":
        H3="○"
    if komputer=="I6":
        I6="○"
    if komputer=="I5":
        I5="○"
    if komputer=="I4":
        I4="○"
    if komputer=="J6":
        J6="○"
    if komputer=="J5":
        J5="○"
    if komputer=="K6":
        K6="○"
'''
print("        A   B   C   D   E   F   G   H   I   J   K")
print("                           ___")
print(f"1                         | {F1} |")
print("                       -----------")
print(f"2                     | {E2} | {F2} | {G2} |")
print("                   -------------------")
print(f"3                 | {D3} | {E3} | {F3} | {G3} | {H3} |")
print("               ---------------------------")
print(f"4             | {C4} | {D4} | {E4} | {F4} | {G4} | {H4} | {I4} |")
print("           -----------------------------------")
print(f"5         | {B5} | {C5} | {D5} | {E5} | {F5} | {G5} | {H5} | {I5} | {J5} |")
print("       -------------------------------------------")
print(f"6     | {A6} | {B6} | {C6} | {D6} | {E6} | {F6} | {G6} | {H6} | {I6} | {J6} | {K6} |")
print("     -----------------------------------------------")
'''
#   ●    ○