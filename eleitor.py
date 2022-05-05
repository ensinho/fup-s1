cand1 = cand2 = cand3 = 0
eleit = int(input("Quantos eleitores têm? "))
#utilizar while aqui para nao contabilizar votos invalidos. 
if eleit > 0: 
    print("--- UTILIZE 1,2,3 PARA CANDIDATOS 1,2,3 RESPECTIVAMENTE ---")
    for i in range(eleit):
        voto = int(input("Em qual quantidado irá votar? "))
        if voto == 1:
            cand1 += + 1
        elif voto == 2:
            cand2 += 1
        elif voto == 3:
            cand3 += + 1
        else:
            print("Número de candidato inválido!!")
            exit()
    print(" %d voto(s) para Candidato 1 // %d voto(s) para Candidato 2 // %d voto(s) para Candidato 3 " %(cand1,cand2,cand3))
else:
    print("Não tem eleitores, logo sem votos. ")

''' eleit = int(input("Quantos eleitores tem? "))
    while eleit <= 0:
        eleit = int(input("Quantos eleitores tem? "))
    for i in range(eleit):
        ,,,
        ,,,
        ,,,
        '''