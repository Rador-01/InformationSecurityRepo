alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = (
    "VVHWGQUIVYHIRSUPGTWXJSVIPCWIUPHGCIVIVVHPGHWITSDTRSDVUSYITMZL"
    "GFHIXSUCVSDQOSPFGFVLQIOHEVHGMSDGJQRPWAQWGSNXJSPSUHIVGEXIPHVC"
    "OPRPCBGYUSLXVCUIECYITHKIMSBAJSQXJSPIUGDKGPHGQAHWEZHETSQXGFWL"
    "GOFGGGVAQFGIEZLTUS"
)

key = ""
shifts = []

for i in range(4):
    group = text[i::4]
    counts = {}
    for c in group:
        counts[c] = counts.get(c, 0) + 1

    print("\nGroup", i+1)
    for c in sorted(counts, key=counts.get, reverse=True):
        print(c, round(100*counts[c]/len(group), 2), "%")

    frequent = max(counts, key=counts.get)
    shift = (alphabet.index(frequent) - alphabet.index("E")) % 26
    shifts.append(shift)
    key += alphabet[shift]

print("\nKey:", key)

result = ""
for i in range(len(text)):
    position = alphabet.index(text[i])
    result += alphabet[(position-shifts[i % 4]) % 26]

print("Plaintext:", result)