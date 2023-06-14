import requests

headers = {'Authorization': 'Token 7dc9f9e28797dab7c5c8a6625b59c41c8b0fc6d5'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Gerência Ágil de Projetos com Scrum",
    "url": "http://www.geekuniversity.com.br/scrum"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando o código de status HTTP 201
assert resultado.status_code == 201

# Testando se o títulodo curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']