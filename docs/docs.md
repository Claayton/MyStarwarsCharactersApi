# 📋 Documentação da API

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
