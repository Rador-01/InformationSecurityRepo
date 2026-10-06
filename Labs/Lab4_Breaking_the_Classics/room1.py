"""
plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = "QMJZTGFKPWLSBOXNCRYEVHIADU"

def substitute(text, source,target):
    result = ""
    for c in text:
        if c in source:
            result += target[source.index(c)]
        else:
            result += c  
    return result

print(substitute("KEEP THE SECRET SAFE", plain,cipher))
print(substitute("ERVYE DXVR SXFPJ", cipher,plain))
"""


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = """EKT YTJRTE BTYYQFT PY KPZZTO PO EKPY NQRQFRQNK.
STEETR GRTCVTOJD ZXTY OXE RTHTQS EKT IKXST LTD,
MVE PE FPHTY Q FXXZ YEQRE.
SXXL GXR JXBBXO IXRZY, RTNTQETZ NQEETROY,
QOZ YKXRE IXRZY.
IKTO DXV RTJXHTR EKT BTYYQFT,
EKT HPFTOTRT LTD KQY GXVR STEETRY."""

counts = {}
total = 0
for c in text:
    if c in alphabet:
        counts[c] = counts.get(c,0) + 1
        total += 1
"""
for c in sorted(counts, key=counts.get, reverse=True):
    print(c, counts[c], round(100*counts[c]/total,2), "%")
"""

letters = sorted(counts, key=counts.get, reverse=True)
english = "ETRSOAHNDIGL"  #order from hint

mapping = {}
for i in range(len(english)):
    mapping[letters[i]] = english[i]

print("Guessed pairs:", mapping)

#fill gaps using word patterns
mapping.update({
    'J': 'C', 'B': 'M', 'N': 'P', 'G': 'F',
    'C': 'Q', 'V': 'U', 'D': 'Y', 'H': 'V',
    'I': 'W', 'L': 'K', 'M': 'B'
})

result = ""
for c in text:
    if c in alphabet:
        result += mapping.get(c, "?")
    else:
        result += c

print(result)