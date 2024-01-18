# Projeto

Este arquivo descreve um projeto em Python com as seguintes funcionalidades:

- Login em GPO para extração de dados de estoque.
- Login em SAPWEB para extração de dados como:
  - Dados de faturamento do dia anterior.
  - Dados de faturamento do mês.
  - Dados de estoque.
  - Dados de produção.

Os dados extraídos são armazenados e enviados via Microsoft Teams e WhatsApp Web.

# Observações
- O projeto é exclusivo para uso em rede corporativa, algumas funções podem não funcionar fora dessa rede.
- Cada programador pode adaptar o projeto para outras atividades.

> Mensagem em WhatsApp

![WhatsApp](./img/whatsapp.png)

> Mensagem Microsoft Teams

![Teams](./img/teams.PNG)

***Dados privados ocultos***

# RPA-SAPWeb-GPO

Este projeto é um exemplo de automação de processos robóticos para extrair dados do estoque e faturamento do SAPWEB, enviando-os via Microsoft Teams e WhatsApp Web.

## Pré-requisitos

Antes de começar, certifique-se de atender aos seguintes requisitos:

- Versão mais recente do Python.
- Bibliotecas necessárias listadas no arquivo requirements.txt.

## Instalando RPA-SAPWeb-GPO

Para instalar o RPA-SAPWeb-GPO, siga estas etapas:

- Clone o repositório.
- Execute os comandos para criar e ativar o ambiente virtual:
  ```
  pip install virtualenv
  virtualenv venv
  venv/Scripts/activate
  ```
- Instale as bibliotecas necessárias:
  ```
  pip install -r requirements.txt
  ```
- Configure as variáveis no arquivo .env seguindo as orientações [aqui](./controller/variaveis.py).
- Execute o arquivo main.py.

## Contribuindo para RPA-SAPWeb-GPO

Para contribuir com RPA-SAPWeb-GPO, siga estas etapas:

1. Faça um fork deste repositório.
2. Crie um branch: `git checkout -b <nome_do_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_do_commit>'`.
4. Envie para o branch original: `git push origin <nome_do_projeto>/<local>`.
5. Crie uma solicitação pull.

## Contato

Para entrar em contato, envie um e-mail para jbsilva.dev@outlook.com.