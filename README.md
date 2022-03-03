# MyStarwarsCharactersApi

API de request para API externa do StarWars para cadastrar seu personagem favorito da saga.

[🚀 Configurando o ambiente](#setup) - Aqui estão algumas instruções que permitirão que vocẽ obtenha uma cópia do projeto em sua máquina local.

[⚙️ Executando os testes](#tests) - Aqui estão alguns passos bem simples para testar o projeto.

[📦 Detalhes do desenvolvimento](#develop) - Aqui estão alguns detalhes do desenvolvimento da aplicação.

[📋 Documentação da API](#docs) - Aqui deixo todos as funcionalidades e detalhes para utilização da API.

## Setup

## 🚀 Configurando o ambiente

### **📋 Pré-requisitos**:

[#Pular essa babozeira e rodar logo o projeto.](install.sh)

O projeto foi desenvolvido em um sistema operacional `linux mint 20.03`, essas instruções devem funcionar na maioria dos casos, mas pode ter alguma diferença dependendo do sistema.

Uma das ferramentas exenciais para rodar o programa é o `git`, mas você provavelmente já tem ele na tua maquina.
Outro detalhe importando é que estou utilizando a versão mais recente do python no momento, a `versão 3.10.2`, e é recomendado que utilize a mesma versão para evitar problemas, mas provavelmente deve funcionar em qualquer versão acima da 3.8. 

Eu utilizei `pyenv` para instalar na minha maquina, mas vocẽ pode utilizar o [site oficial](https://www.python.org/downloads/) se preferir.

### __Ambiente virtual__

É uma boa prática criar um ambiente virtual para isolar o projeto da sua maquina e evitar conflitos, utilize o comando a seguir para instalar o **virtualenv** caso ainda não tenha instalado:
```
 sudo pip3 install virtualenv
```
Agora configure seu `ambiente virtual` para evitar possiveis conflitos:
```
python3 -m venv venv 
```
*Em seguida você deverá **Ativar** esse ambiente:*
```
source venv/bin/activate 
```
*Agora instale as **bibliotecas e pacotes** necessários para rodar o projeto:*
```
pip3 install -r requirements.txt
```
*Você vai precisar de um arquivo para **alocar suas variáveis de ambiente**, use o comando abaixo para criá-lo e exportar as variáveis (Você pode/deve substituir a `secret_key` por uma de sua escolha, mas para teste não vai fazer diferença):*
```
echo "SEARCH_URL=https://swapi.dev/api/people/
CONNECTION_STRING=sqlite:///storage.db
CONNECTION_STRING_TEST=sqlite:///storage_test.db
SECRET_KEY=mecontratapiazada123" > .env
```

*O projeto ja está configurado e pronto para ser testado em modo de desenvolvedor:*
```
python3 run.py
```

## Tests

## ⚙️ Executando os testes

Utilizar para esse projeto o pytest para fazer os testes necessários, e ara executar os testes do projeto é muito simples:

```
  # Rodar o testes da forma padrão:
  pytest

  # Rodar os testes mostrando os detalhes caso ocorra algum erro:
  pytest -v
```

Esse projeto não utiliza coverage.

## Develop

## 📦 Desenvolvimento

* **Framework**: FastApi foi minha escolha para framework, apesar de o flask ser mais antigo e provavelmente mais estável, gosto muito da forma que o FastApi funciona, inicialmente muito semelhante ao Flask na implementação, porém ao longo do desenvolvimento da sua aplicação você vai percebendo que diferente do flask, ele entrega muita coisa pronta e facilita a vida do desenvolvedor, além de ter uma implementação mais moderna.


* **Arquitetura**: Resolvi utilizar nesse projeto a clean architecture, esse modelo de arquitetura garante uma grande independência qualquer figura externa. As regras de negócios e casos de uso simplesmente ficam isoladas na sua camada e não conhecem nada das camadas externas da aplicação.
Dessa forma fica significativamente muito simples a substituição do framework web, banco de dados, ou interface do usuario.


* **Banco de dados**: Para a apresentação do projeto inicialmente preferi utilizar o SQLite, apesar de estar estudadndo bastante docker e utilizar imagens na minha maquina local, não me sinto confiante, e ainda não adquiri os conhecimentos necessários para repassar uma imagem da minha maquina para outro usuário. Além disso com o prazo curto preferi priorizar a implementação do projeto em si.

## Docs

## 📋 Documentação da API

### __Usuários:__

__Action:__ Cadastro de um novo usuário no sistema.  
*__Endpoint__: /api/user/  
__Method__: [ POST ]  
__Body-params__: name: str
                 email: str
                 password: any
__*Não requer Token de acesso__.

```
{
    "message": "Usuario registrado com sucesso!",
    "data": {
        "id": 1,
        "name": "clayton",
        "email": "clayton@test.com",
        "password": "Não mostramos isso aqui!"
    }
}
```
<br>

__Action:__ Busca de informações de um único usuário que esteja cadastrado no sistema.  
*__Endpoint__: /api/user/  
__Method__: [ GET ]  
__Query-string-params__: user_id: int
                         name: str
                         email: str  
__*Requer Token de acesso no header__: "Authorization": "<seu_token>"

```
Resposta:
{
    "message": "Usuario encontrado!",
    "data": {
        "id": 1,
        "name": "clayton",
        "email": "clayton@test.com",
        "password": "Não mostramos isso aqui!"
    }
}

```
<br>


__Action:__ Busca de informações de todos os usuários cadastrados no sistema.  
*__Endpoint__: /api/users/  
__Method__: [ GET ]  
__*Não requer parametros__  
__*Requer Token de acesso no header__: "Authorization": "<seu_token>"

```
{
    "message": "Usuarios encontrados!",
    "data": [
        {
            "id": 1,
            "name": "clayton",
            "email": "clayton@test.com",
            "password": "Não mostramos isso aqui!"
        }
    ]
}

```
<br>

### __Autenticação:__

__Action:__ Realizar login de um usuário cadastrado e retornar um token de acesso e algumas informações sobre o token e o usuário.  
*__Endpoint__: /api/auth/  
__Method__: [ POST ]  
__Body-params__: email: str
                 password: any  
__*Não Token de acesso no header__.

```
Resposta:
{
    "message": "Login efetuado com successo!",
    "data": {
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NDYyOTI3MTcsImlhdCI6MTY0NjI0OTUxNywiZW1haWwiOiJjbGF5dG9uQHRlc3QuY29tIiwibmFtZSI6ImNsYXl0b24ifQ.NRS3dUF7fwh8uQZigjoFFnzBvkfPczI00tcyuobYrg8",
        "exp": "2022-03-03 07:31:57.404042",
        "id": 1,
        "user": {
            "id": 1,
            "name": "clayton",
            "email": "clayton@test.com"
        }
    }
}

```
## __Personagens StarWars__:


__Action:__ Rota para buscar os personagens de starwars, atravez de uma requisição externa (deve demorar um pouco, não cadastra os dados no no banco)..  
*__Endpoint__: /api/characters/external/  
__Method__: [ GET ]  
__*Não requer parametros__  
__*Requer Token de acesso no header__: "Authorization": "<seu_token>"

```
{
    {
    "data": [
        {
            "id": 1,
            "name": "Luke Skywalker",
            "height": "172",
            "mass": "77",
            "hair_color": "blond",
            "skin_color": "fair",
            "eye_color": "blue",
            "birth_year": "19BBY",
            "gender": "male"
        },
        {
            "id": 2,
            "name": "C-3PO",
            "height": "167",
            "mass": "75",
            "hair_color": "n/a",
            "skin_color": "gold",
            "eye_color": "yellow",
            "birth_year": "112BBY",
            "gender": "n/a"
        }
    ]
}

```
<br>

__Action:__ Rota para buscar os personagens de starwars que ja estão cadastrados no banco de dados.
*__Endpoint__: /api/characters/
__Method__: [ GET ]  
__*Não requer parametros__  
__*Requer Token de acesso no header__: "Authorization": "<seu_token>"

```
{
    {
    "data": [
        {
            "id": 1,
            "name": "Luke Skywalker",
            "height": "172",
            "mass": "77",
            "hair_color": "blond",
            "skin_color": "fair",
            "eye_color": "blue",
            "birth_year": "19BBY",
            "gender": "male"
        },
        {
            "id": 2,
            "name": "C-3PO",
            "height": "167",
            "mass": "75",
            "hair_color": "n/a",
            "skin_color": "gold",
            "eye_color": "yellow",
            "birth_year": "112BBY",
            "gender": "n/a"
        }
    ]
}

```
<br>

__Action:__ Rota para registrar os personagens de starwars, realiza uma requisição externa, coleta os dados e registra os dados no banco de dados caso ainda nao esteja registrado.
*__Endpoint__: /api/characters/
__Method__: [ POST ]  
__*Não requer parametros__  
__*Requer Token de acesso no header__: "Authorization": "<seu_token>"

```
{
    "message": "Personagens cadastrados com sucesso!",
    "data": {
        "id": 1,
        "name": "Paulinho Manutenção das Naves",
        "height": "175",
        "mass": "57",
        "hair_color": "colorido",
        "skin_color": "white",
        "eye_color": "black",
        "birth_year": "19BBY",
        "gender": "male"
    }
}

```

