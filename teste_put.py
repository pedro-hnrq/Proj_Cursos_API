import requests

headers = {'Authorization': 'Token 7dc9f9e28797dab7c5c8a6625b59c41c8b0fc6d5'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Novo Curso de Scrum 3",
    "url": "http://www.geekuniversity.com.br/nsc3"
}

# Buscando o curso com ID 9
# curso = requests.get(url=f'{url_base_cursos}9/', headers=headers)
# print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}9/', headers=headers, data=curso_atualizado)

# Testando o código de status HTTP
assert resultado.status_code == 200

# Testando o título
assert resultado.json()['titulo'] == curso_atualizado['titulo']