import json

with open("C:\Users\Cauã Vitor\Documents\GitHub\dados.json") as file:
    data = json.load(file)
    data_dict = 0
    dias = []
    fats = []
    med = 0
    tot = 0
    for dado in data:
        med += dado['valor']
        if dado['valor'] != 0:
            dias.append(dado['dia'])
            fats.append(dado['valor'])
            tot+=1
    max_day = max(fats)
    min_day = min(fats)
    med/=tot
    tot = 0
    print("Maior faturamento: " + str(max_day))
    print("Menor faturamento: " + str(min_day))
    for dado in data:
        if dado['valor'] >= med:
            tot+=1
    print("Dias acima da media: "+str(tot))