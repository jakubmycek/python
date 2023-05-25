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
listakordów=[A6,B6,B5,C6,C5,C4,D6,D5,D4,D3,E6,E5,E4,E3,E2,F6,F5,F4,F3,F2,F1,G6,G5,G4,G3,G2,H6,H5,H4,H3,I6,I5,I4,J6,J5,K6]


print("        A   B   C   D   E   F   G   H   I   J   K")
print("                           ___")
print(f"1                         | {F1} |")
print("                       -----------")
print(f"2                     | {E2} | {F2} | {G2} |")
print("                   ------------------")
print(f"3                 | {D3} | {E3} | {F3} | {G3} | {H3} |")
print("               -------------------------")
print(f"4             | {C4} | {D4} | {E4} | {F4} | {G4} | {H4} | {I4} |")
print("           ---------------------------------")
print(f"5         | {B5} | {C5} | {D5} | {E5} | {F5} | {G5} | {H5} | {I5} | {J5} |")
print("       ------------------------------------------")
print(f"6     | {A6} | {B6} | {C6} | {D6} | {E6} | {F6} | {G6} | {H6} | {I6} | {J6} | {K6} |")
print("     -----------------------------------------------")
gracz=str(input("podaj kordy"))
z=0
while(z==0):
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
if gracz=="I%":
    I5="●"
if gracz=="I4":
    I4="●"
if gracz=="J6":
    J6="●"
if gracz=="J5":
    J5="●"
if gracz=="K6":
    k6="●"
print("        A   B   C   D   E   F   G   H   I   J   K")
print("                           ___")
print(f"1                         | {F1} |")
print("                       -----------")
print(f"2                     | {E2} | {F2} | {G2} |")
print("                   ------------------")
print(f"3                 | {D3} | {E3} | {F3} | {G3} | {H3} |")
print("               -------------------------")
print(f"4             | {C4} | {D4} | {E4} | {F4} | {G4} | {H4} | {I4} |")
print("           ---------------------------------")
print(f"5         | {B5} | {C5} | {D5} | {E5} | {F5} | {G5} | {H5} | {I5} | {J5} |")
print("       ------------------------------------------")
print(f"6     | {A6} | {B6} | {C6} | {D6} | {E6} | {F6} | {G6} | {H6} | {I6} | {J6} | {K6} |")
print("     -----------------------------------------------")

#   ●    ○