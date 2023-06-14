<h1 align="center"> Projeto Cursos API</h1>

<h2 align="center"> Prévia <h2>

![DRF](https://github.com/pedro-hnrq/Python_-_Django/assets/74242717/c7dff0fd-c827-4755-87f7-71350d6d9c6d)

  
  
<h3>Objetivo</h3>

<h5 align="justify">Este é um projeto de API desenvolvido em Django REST Framework para gerenciar cursos e avaliações. A API permite a criação, atualização, recuperação e exclusão de cursos, bem como a adição de avaliações para cada curso. É possível consumir as informações da API em outras aplicações através dos endpoints disponíveis.</h5>
<br>
<h4>Recursos Principais</h4>
<ul>
<h6 align="justify"><li>Cursos: Criação, recuperação, atualização e exclusão de cursos. Cada curso possui título e URL única.</li></h6>
<h6 align="justify"><li>Avaliações: Adição de avaliações para cada curso. Cada avaliação possui o nome do avaliador, comentário, avaliação numérica e status de ativação.</li></h6>
</ul>

<h4>Endpoints Disponíveis</h4>
<ul>
<h6><li>Versão 1 da API: http://localhost:8000/api/v1/</li></h6>
<h6><li>Versão 2 da API: http://localhost:8000/api/v2/</li></h6>
</ul>

<h4>Autenticação</h4>
<h6 align="justify">A partir da versão 2 da API, é necessário autenticar-se para realizar operações nos cursos. É fornecido um token de autenticação para cada usuário autorizado.</h6>

<h4>Métodos HTTP suportados</h4>
<ul>
<h6><li>GET: Recuperar informações de cursos ou avaliações.</li></h6>
<h6><li>POST: Criar um novo curso ou avaliação.</li></h6>
<h6><li>PUT: Atualizar informações de um curso existente.</li></h6>
<h6><li>DELETE: Excluir um curso ou avaliação existente pelo o ID.</li></h6>

</ul>

<h4>Testes e Verificação</h4>

<h6>A API foi testada com os métodos HTTP suportados (GET, POST, PUT e DELETE) para garantir o correto funcionamento de todas as requisições. Utilizou-se a biblioteca Pytet para executar os testes e verificar os status do HTTP.</h6>

<h4>Consulta Avançada</h4>

<h6 align="justify">Para realizar consultas avançadas nos dados da API, foi utilizada a biblioteca Jsonpath. Com ela, é possível extrair informações específicas dos resultados das requisições, permitindo maior flexibilidade na manipulação dos dados retornados.</h6>



<h4>Configuração do Ambiente</h4>
  <h5>Para que o usuário execute o DRF na sua máquina, siga os seguintes passos:</h5>
  
<ol>
<h6><li>Clone este repositório em sua máquina utilizando o seguinte comando no terminal: 
 
```
git clone git@github.com:pedro-hnrq/Python_-_Django.git
```  
</li></h6>   
 <h6><li>Vá ao diretório do Django REST Framework na pasta Proj_Cursos_API.</li></h6>
    
 <h6 align="justify"><li>Verifique se na sua máquina tenha o Python instalado, se já estiver crie ambiente virtual e logo em seguida ative. </li></h6>
  
<h6><li>Instale as dependências do projeto através do arquivo requirements.txt: 
  
```
pip install -r requirements.txt
```
</li></h6>
<h6><li>Crie um superusuário para acessar a área administrativa:
  
```
python3 manage.py createsuperuser
```
</li></h6>  
<h6><li>Execute as migrações do banco de dados:
  
```
python3 manage.py migrate
```
</li></h6>  
<h6><li>Execute servidor:  
  
```
python3 manage.py runserver
```
</li></h6>  
<h6><li>Acesse o endereço http://localhost:8000/admin e faça login com as credenciais do superusuário criado anteriormente.</li></h6>
  
<h6><li>Para acessar a API, utilize o endereço http://localhost:8000/api/v1/ para a versão 1 da API e http://localhost:8000/api/v2/ para a versão 2 da API. As rotas disponíveis podem ser encontradas nos arquivos cursos/urls.py e escola/urls.py.</li></h6> 
  
<h6><li>Observação: usei o IDE do Pycharm juntamente com o Programa Insomnia para realiza as requisição HTTP (GET, POST, PUT, DELETE e Token), mas poderá utilizar o IDE do Visual Studio Code com a extensão Thunder Client ou programa do Postman.</li></h6>
</ol>


<h4>Contribuição</h4>

<h6>Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, fique à vontade para abrir uma issue ou enviar um pull request.</h6>

<h4>Licença</h4>

<h6>Este projeto está licenciado sob a MIT License.</h6>