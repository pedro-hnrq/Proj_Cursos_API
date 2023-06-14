import requests

# GET Avalições

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTP
# print(avaliacoes.status_code)
""""
print(avaliacoes.json())
print(type(avaliacoes.json()))
"""

# Acessando a quantidade de registros
# print(avaliacoes.json()['count'])

# Acessando a próxima página de resultado
# print(avaliacoes.json()['next'])

# Acessando os resultados desta página
# print(avaliacoes.json()['results'])
# print(type(avaliacoes.json()['results']))

# Acessando o primeiro e último elemento da lista de resultados
# print(avaliacoes.json()['results'][0])
# print(avaliacoes.json()['results'][-1])

# Acessando somente o nome da pessoa que fez a última avaliacão
# print(avaliacoes.json()['results'][-1]['nome'])


# GET Avaliacao

avaliacao = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/7/')

# print(avaliacao.json())

# GET Cursos

headers = {'Authorization': 'Token 296c53ddbd3f201469fc47fbe4adb985676df8ab'}

cursos = requests.get('http://127.0.0.1:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())
print(type(cursos.json()))
