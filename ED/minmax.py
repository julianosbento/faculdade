
def recr(se,c,mini,maxi):
    miniA=mini
    maxiA=maxi
    if c==len(se):
        return miniA,maxiA
    else:
        if se[c]<miniA:
            miniA=se[c]
        if se[c]>maxiA:
            maxiA=se[c]
        return recr(se,c+1,miniA,maxiA)

def maxmin(se):
    if len(se)==0:
        return None,None
    elif len(se)==1:
        return se[0],se[0]
    else:
        return recr(se,1,se[0],se[0])



'''
o código demora O(n) pois vai percorrer o vetor inteiro,
até que a variável cursor se igualar ao tamanho.
memória O(n)
'''
