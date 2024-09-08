import json
import numpy as np

#Carregar o arquivo JSON
file_path = 'dados.json'
with open(file_path, 'r') as file:
    dados = json.load(file)

#Dias com faturamento maior que zero
valores = [dado['valor'] for dado in dados if dado['valor'] > 0]

#Menor valor de faturamento
menor_valor = min(valores)

#Maior valor de faturamento
maior_valor = max(valores)

#Média mensal
media_mensal = np.mean(valores)

#Dias com faturamento superior à média mensal
acima_da_media = sum(1 for valor in valores if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_valor:.2f}")
print(f"Maior valor de faturamento: {maior_valor:.2f}")
print(f"Dias com faturamento superior à média: {acima_da_media}")