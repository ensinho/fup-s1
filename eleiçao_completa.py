cand1 = cand2 = cand3 = cand4 = vn = vb = 0
# vn -> voto nulo e vb -> voto em branco.
eleit = int(input("Quantos eleitores têm? "))
while eleit <= 0:
    print("Número de eleitores inválidos! Tente novamente. ")
    eleit = int(input("Quantos eleitores têm? "))
print("--- UTILIZE 1,2,3,4  PARA CANDIDATOS 1,2,3,4 RESPECTIVAMENTE --- 5 PARA VOTO NULO E 6 PARA VOTO EM BRANCO ---")
for i in range(eleit):
    voto = int(input("Qual será o voto? "))
    while voto <= 0 or voto > 6:
        print("Voto inválido! Tente novamente. ")
        voto = int(input("Qual será o voto? "))
    if voto == 1:
        cand1 += + 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += + 1
    elif voto == 4:
        cand4 += 1
    elif voto == 5:
        vn += 1
    elif voto == 6:
        vb += 1
    else:
        print("Número de candidato inválido!!")
        exit()
total = cand1+cand2+cand3+cand4+vn+vb
tot_c1 = cand1/total
tot_c2 = cand2/total
tot_c3 = cand3/total
tot_c4 = cand4/total
tot_vn = vn/total
tot_vb = vb/total
# total de votos para cada candidato e para votos em branco/ votos nulos.
print(" %d voto(s) para Candidato 1 e o seu percentual de votos %.2f . \n %d voto(s) para Candidato 2 e seu percentual %.2f . \n %d voto(s) para Candidato 3 e seu percentual %.2f . \n %d voto(s) para o canditato 4 e seu percentual %.2f . \n O total de voto(s) nulo: %d e seu percentual sobre o total: %.2f . \n O total de voto(s) em branco: %d e seu percentual sobre o total: %.2f .  " %
      (cand1, tot_c1, cand2, tot_c2, cand3, tot_c3, cand4, tot_c4, vn, tot_vn, vb, tot_vb))
