P = 487
# D = ?
E1 = 31
#E2 = pow(E1, D, P)
E2 = 168
R = 11

def enc(PT, E1, E2, R, P):
    C1 = pow(E1, R, P)
    C2 = ""
    for i in PT:
        data = (i * pow(E2, R)) % P
        C2 += chr(data)
    return C1,C2

def dec(C1, C2, D, P):
    PT = ""
    for i in C2:
        data = (ord(i) * pow(C1 ** D, -1, P)) % P
        PT += chr(data)
    return PT

C1,C2 = open("./flag.ct","r").readlines()
C1 = int(C1[6:])
C2 = C2[6:]

D = 1
while dec(C1,C2,D,P)[0] != "V":
    D += 1
print(dec(C1,C2,D,P))
