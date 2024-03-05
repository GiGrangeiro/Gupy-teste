import urllib.request
import json

url = 'https://drive.google.com/uc?id=1qXvCPjEL4jerElN-hnScoKkEVmSQ8A2L&export=download'

urllib.request.urlretrieve(url, 'faturamento.json')

with open('faturamento.json') as arquivo:
    dados_faturamento = json.load(arquivo)

faturamento_diario = [dia['valor'] for dia in dados_faturamento if dia['valor'] != 0]

menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

media_mensal = sum(faturamento_diario) / len(faturamento_diario)

dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

print("Menor valor de faturamento diário:", menor_valor)
print("Maior valor de faturamento diário:", maior_valor)
print("Número de dias com faturamento acima da média mensal:", dias_acima_media)
