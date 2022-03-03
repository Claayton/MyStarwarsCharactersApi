# 📦 Desenvolvimento


* **Framework**: FastApi foi minha escolha para framework, apesar de o flask ser mais antigo e provavelmente mais estável, gosto muito da forma que o FastApi funciona, inicialmente muito semelhante ao Flask na implementação, porém ao longo do desenvolvimento da sua aplicação você vai percebendo que diferente do flask, ele entrega muita coisa pronta e facilita a vida do desenvolvedor, além de ter uma implementação mais moderna.


* **Arquitetura**: Resolvi utilizar nesse projeto a clean architecture, esse modelo de arquitetura garante uma grande independência qualquer figura externa. As regras de negócios e casos de uso simplesmente ficam isoladas na sua camada e não conhecem nada das camadas externas da aplicação.
Dessa forma fica significativamente muito simples a substituição do framework web, banco de dados, ou interface do usuario.


* **Banco de dados**: Para a apresentação do projeto inicialmente preferi utilizar o SQLite, apesar de estar estudadndo bastante docker e utilizar imagens na minha maquina local, não me sinto confiante, e ainda não adquiri os conhecimentos necessários para repassar uma imagem da minha maquina para outro usuário. Além disso com o prazo curto preferi priorizar a implementação do projeto em si.
