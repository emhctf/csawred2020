orig = "prsprtpprrrtprpsptprspptpppsrtpprrstpspptprsrrtpssrtprppstprrrptsssstprrrstprppstpprsptprssstpspptpprrrtpprrrtppppstpppsst"
def getintarr(text, p, r, s):
    return [int(q, 3) for q in text.replace("p", p).replace("r", r).replace("s", s)[:-1].split("t")]
print(''.join([chr(a) for a in getintarr(orig, '1', '0', '2')]))
