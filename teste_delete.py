import requests

headers = {'Authorization': 'Token 7dc9f9e28797dab7c5c8a6625b59c41c8b0fc6d5'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}9/', headers=headers)

# Testando o código HTTP
assert resultado.status_code == 204

# Testando se o tamanho do conteúdo retorna é 0
assert len(resultado.text) == 0