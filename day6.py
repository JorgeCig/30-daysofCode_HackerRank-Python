n = int(input())

for i in range(n):
    ar =input()
    areven =[ar[iseven] for iseven in range(len(ar)) if iseven%2 == 0]
    arodd = [ar[isodd] for isodd in range(len(ar)) if isodd%2 != 0 ]
    arevenn = ''.join(areven)
    aroddn = ''.join(arodd)
    print(areven, arodd)
        