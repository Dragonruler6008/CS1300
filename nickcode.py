

def checkdivisor(divisor):
    """
    Args:
        divisor (Int): number taken in to be the divisor.
    """
    data = []
    loopnumber = 1
    while loopnumber <= divisor:
        if (divisor % loopnumber) == 0:
            data.append(loopnumber)
        loopnumber += 1
    return data


mdivisorinpt = int(input("Enter value of M: "))
ndivisorinpt = int(input("Enter value of N: "))
mDivisors = checkdivisor(mdivisorinpt)
print(mDivisors)
nDivisors = checkdivisor(ndivisorinpt)
print(nDivisors)
finals = []
for m in enumerate(mDivisors):
    for n in enumerate(nDivisors):
        if nDivisors == mDivisors:
            finals.append(nDivisors)

print(finals)
