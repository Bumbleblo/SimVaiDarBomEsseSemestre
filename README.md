# SimVaiDarBomEsseSemestre

Primeira dinâmica com a equipe de MDS.

## Objetivos dessa dinâmica

Nós iremos trabalhar várias atividades cotidianas do fluxo de desenvolvimento "normal" de um engenheiro de software. Algumas atividades que iremos dar atenção é:

* Entender (superficialmente) o conceito de rede de computadores
* Concentrar as dependências do nosso software em uma imagem docker
* Conseguir fazer uma requisição HTTP simples e com autenticação JWT.

## Como subir o servidor localmente

### Instalando as dependências

Primeiramente precisamos instalar as dependências para rodar o nosso sistema. Para essa atividade precisamos de tais softwares instalados em sua maquina.

* docker: [instalação mac](https://docs.docker.com/v17.12/docker-for-mac/install/) ou [instalação ubuntu](https://docs.docker.com/v17.12/install/linux/docker-ce/ubuntu/)
* docker-compose: [manual de instalação](https://docs.docker.com/compose/install/)

**Observação:** Caso você esteja usando o ubuntu basta instalar o pacote docker.io

### Subindo tudo :)

Para subir o servidor precisamos rodar poucos comandos docker (isso mesmo, poucos). Perceba que o legal aqui é que tudo o que vamos subir vai esta separado na sua máquina, ou seja, fora o docker e docker-compose não precisamos instalar mais nada no seu computador.

A partir daqui vamos apenas apresentar os poucos comandos que precisamos

**Compilando a imagem docker**

```bash
sudo docker-compose build dev
```

**Subindo o banco da aplicação**

```bash
sudo docker-compose run dev migrate
```

**Criando um super usuário**
```
sudo docker-compose run dev createsuperuser

> Coloque a senha que quiser e o username que preferir :)
```

**Colocando o nosso servidor para funcionar**

```bash
sudo docker-compose up dev
```


Finalmente o servidor está rodando no seu computador na porta 8080, para acessar basta clicar ou colocar essa url no seu navegador http://localhost:8080.


Agora basta saber os endpoints que vamos trabalhar, para acessar cada endpoint para colocar ele depois do endereço fornecido acima.

* **/auth/token/** -> Esse cara vai fornecer para você uma interface para digitar o usuário e senha e lhe devolverá um token.

* **/take/take/objetivo/** -> Esse é o endpoint que estamos buscando acessar.


## Make yourself

Agora que você tem o servidor em seu computador vamos tentar replicar o que fizemos em nosso encontro em sua máquina. Para isso escreva um script em python que tenha um cabeçalho **Authorization** com um conteúdo no formato **JWT <insira aqui  o token>**.O objetivo deste script é mostrar uma mensagem de sucesso ([código 200 no http](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)).

**Dica:** Em python usem a bibloteca [requests](https://2.python-requests.org//en/master/) (instalem essa dependência em uma [virtualenv](https://virtualenv.pypa.io/en/stable/)).

Fique a vontade para escrever o script em outras linguagens. A história vai ser a mesma: uma requisição HTTP com o cabeçalho do JWT. Todas as linguagens tem suporte para isso!
