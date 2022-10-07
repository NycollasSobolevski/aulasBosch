def notas(quantidade, situação=False):
    dicionario= {}
    listaNota = []
    for i in range(quantidade):
        nota = float(input(f"Insira a nota {i+1}"))
        listaNota.append(nota)
    dicionario['Media'] = (sum(listaNota))/(len(listaNota))
    dicionario['Maior'] = max(listaNota)
    dicionario['Menor'] = min(listaNota)
    print(dicionario['Media'])
    if situação ==True:
        if dicionario['Media'] >= 7:
            dicionario['Situação'] = 'Boa'
        elif dicionario['Media'] < 7 and dicionario['Media'] >= 5:
            dicionario['Situação'] = 'Razoável'
        elif dicionario['Media'] < 5:
            dicionario['Situação'] = 'Ruim'
    print(dicionario)


escolha = (int(input("Quantas notas quer adicionar: ")))
notas(escolha,situação=True)
 