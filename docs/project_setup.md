# 🚀 Configurando o ambiente

## **📋 Pré-requisitos**:

[#Pular essa babozeira e rodar logo o projeto.](install.md)

O projeto foi desenvolvido em um sistema operacional linux mint 20.03, essas instruções devem funcionar na maioria dos casos, mas pode ter alguma diferença dependendo do sistema.

Uma das ferramentas exenciais para rodar o programa é o git, mas você provavelmente já tem ele na tua maquina.
Outro detalhe importando é que estou utilizando a versão mais recente do python no momento, a versão 3.10.2, e é recomendado que utilize a mesma versão para evitar problemas, mas provavelmente deve funcionar em qualquer versão acima da 3.8. 

Eu utilizei pyenv para instalar na minha maquina, mas vocẽ pode utilizar o [site oficial](https://www.python.org/downloads/) se preferir.

## **Ambiente virtual**:

É uma boa prática criar um ambiente virtual para isolar o projeto da sua maquina e evitar conflitos, utilize o comando a seguir para instalar o **virtualenv** caso ainda não tenha instalado:
```
 sudo pip3 install virtualenv
```
Agora configure seu ambiente virtual para evitar possiveis conflitos:
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
*Você vai precisar de um arquivo para **alocar suas variáveis de ambiente**, use o comando abaixo para criá-lo e exportar as variáveis (Você pode/deve substituir a secret_key por uma de sua escolha, mas para teste não vai fazer diferença):*
```
Aqui vão as variaveis, ainda nao configurei isso...
secret_key=aquivoceescreveumachavesupersecreta" > .env
```


*O projeto ja está configurado e pronto para ser testado em modo de desenvolvedor:*
