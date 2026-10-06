alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar(text,k):
    result = ""
    for c in text:
        if c in alphabet:
            position = alphabet.index(c)
            result += alphabet[(position+k)%26]
        else:
            result += c   
    return result


print("1:", caesar("CRYPTO IS FUN UNTIL THE PROFESSOR SAYS QUIZ",4))

print("2:", caesar("GWCL JMBBMZ VWB JM CAQVO BWWTA BW AWTDM BPQA", -8))

cipher = "ESP VPJ TD FYVYZHY ECJ MCFEP QZCNP"
for k in range(26):
    print(k, caesar(cipher,-k))