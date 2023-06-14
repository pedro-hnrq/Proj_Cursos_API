import requests
import jsonpath

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')

# for result in resultados:
#     print(result)

print(type(resultados))

nome = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
email = jsonpath.jsonpath(avaliacoes.json(), 'results[*].email')
nota_data = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
print(f'Nome: {nome}\nEmail: {email}\nNota: {nota_data}')