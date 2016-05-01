p=[0.2,0.2,0.2,0.2,0.2]
pHit =0.6
pMiss = 0.2
i=0
while i< 5:
    if( i==1) or (i==2):
        p[i] = p[i] * pHit
    else:
        p[i] = p[i] * pMiss

    i = i + 1

print p