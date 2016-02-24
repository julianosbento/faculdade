
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
        return null
    elif len(se)==1:
        return se,se
    else:
        return recr(se,1,se[0],se[0])



'''
o código demora O(n) pois vai percorrer o vetor inteiro,
até que a variável cursor se igualar ao tamanho.
e usa n pilhas de memória, pois por ser recursiva, cada vez ele vai se chamar
até que pare no último.
'''
