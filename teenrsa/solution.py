
e = 3
c = 21054947296948912186250291623999881612177917867294620912940663265128767538390407246183135081940602148334924270226808672133409885425114817372307202073496919198495962536909357503213718449515958555968598380737125

from Crypto.Util.number import long_to_bytes

def iroot(k, n):
    hi = 1
    while pow(hi, k) < n:
        hi *= 2
    lo = hi // 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        midToK = pow(mid, k)
        if midToK < n:
            lo = mid
        elif n < midToK:
            hi = mid
        else:
            return mid
    if pow(hi, k) == n:
        return hi
    else:
        return lo


print(long_to_bytes(iroot(e, c)))
