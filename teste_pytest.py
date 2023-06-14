import requests

class TestCursos:
    headers = {'Authorization': 'Token 7dc9f9e28797dab7c5c8a6625b59c41c8b0fc6d5'}
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert cursos.status_code == 200

    def test_get_cursos(self):
        curso = requests.get(url=f'{self.url_base_cursos}12/', headers=self.headers)

        assert curso.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de Programação com Ruby",
            "url": "https://www.ruby-lang.org/dad/klk"
        }

        resultado = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resultado.status_code == 201
        assert resultado.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Web com Django REST Framework",
            "url": "https://www.django-rest-framework.org/api-guide/serializers/"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}6/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200
        # assert resposta.json()['titulo'] == atualizado['titulo']

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Django REST Framework - DRF = Routers",
            "url": "https://www.django-rest-framework.org/api-guide/routers/"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}6/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}17/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0
