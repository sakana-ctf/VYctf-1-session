P = 487
# D = ?
E1 = 31
# E2 = pow(E1, D, P)
E2 = 168
R = 11

def enc(PT, E1, E2, R, P):
    C1 = pow(E1, R, P)
    C2 = ""
    for i in PT:
        data = (i * pow(E2, R)) % P
        C2 += chr(data)
    return C1,C2

with open("./flag.pt","rb") as PT:
    C1,C2 = enc(PT.read(), E1, E2, R, P)

with open("./flag.ct","w") as CT:
    CT.write("C1 is:"+str(C1)+"\nC2 is:"+C2)

print("C1 is:"+str(C1)+"\nC2 is:"+C2)

