# space-flight-news-20210823
Coodesh - Back-end Challenge 🏅 2021 - Space Flight News

API para acesso as matérias que esão publicadas no site Space Flight News, que condensa matérias sobre viagens espaciais de diversas fontes na internet, e também a outras matérias cadastaradas pelos usuários.

Desafio para vaga de Backend Developer no Coodesh: [Desafio no Coodesh](https://lab.coodesh.com/hgf777/space-flight-news-20210823)

# Linguagens, Framework e Tecnologias

• Linguagem: Python v 3.9.8<BR>
• Framework: FastAPI v 0.73.0<BR>
• Tecnologias: Git, Heroku, Heroku Postgres, Heroku Scheduler<BR>
• Testes Automaticos: Pytest e Github Actions

# Instruções

## Instalação

1) Possuir/Criar uma conta no [Github](https://github.com/).
2) Possuir/Criar uma conta no [Heroku](https://id.heroku.com/login).
3) Clonar este respositorio do projeto para a sua máquina local.
4) Criar um novo aplicativo no Heroku
5) Adicionar um banco de dados Postgres ao seu app do Heroku. Isso é possível na aba "Resources" procurando a opção "Heroku Postgres". Na instalação você pode usar a versão FREE mas se quiser usar a API por mais de 7 dias precisará instalar a versão BASIC que custa USD 9,00/mês.
6) Após adicionar o Postgres copie as credenciais do banco de dados na aba "Settings" e cole-as no arquivo "src\db\connection.py" nas respectivas CONSTANTES logo no início do arquivo.
7) Após inserir as credenciais do seu banco de dados suba o repostotório para a sua conta no Github.
8) Na aba "Actions" verifique se os testes de Integração contínua passam OK. Em caso de problema delete o Repositório e começe o processo de novo, conferindo as credenciais do seu banco de dados.
9) Se tudo estiver ok, ainda na aba "Actions", inicie o processo "Carregar Artigos do Space" para trazer os artigos do site SpaceFlightNews para o seu banco de dados. Este processo deve demorar mais de 30 minutos, se quiser acompanhar o andamento entre no processo depois de iniciado, ou espere o "Actions" marcar ele como terminado (ok verde).
10) Voltando ao Heroku vamos adicionar o "Heroku Scheduler". Vá na aba "Resources", procure e instale o "Heroku Scheduler". Crie um novo "Job" para rodar as 09:00 UTC o comando "python ./src/atualizar_artigos_do_space.py". Com isto todo dia as 9 horas da manhã o nosso sistema irá procurar por novos artigos no site SpaceFlightNews e atualizar o nosso banco de dados.
11) Vamos indicar ao Heroku que o nosso código está em Python. Vá a aba "Settings" e na opção "Buildpacks" adiconar a opção "Python".
12) Agora vamos conectar o Heroku ao nosso Repositório do Github. Na aba "Deploy" vá em "deployment method" e escolha o botão do Github. Ele vai tedirecionar ao Github para login e pedir permissões de acesso. Após este passo precisará escolher o repositório aonde subiu o código da API.
13) Para verificar se tudo está ok vá na aba "Activity" e confira se tem um "Build succeeded".
14) Neste momento o sistema já deve estar funcional. Para ir ao ponto de entrada da API podemos clicar no botão "Open app" na página do seu app no Heroku. Isso irá abrir uma nova aba do browser já apresentando a frase indicando que acessamos a API.

## Utilização

1)  Para buscar um artigo específico pelo seu ID basta ir ao caminho "/articles/{id}" e indicar o ID do artigo, por exemplo, "/articles/3198" vai apresentar o artigo de ID 3198.
2)  Para buscar uma lista de artigos basta ir ao caminho "/articles/". Neste modo ele irá mostrar os 10 primeiros artigos, para não sobrecarregar as buscas.
3)  Para buscar artigos começando em outro valor de ID pode usar o filtro "offset={id}" fornecendo o número do ID do artigo, por exemplo, "/articles/?offset=1267, irá trazer 10 artigos a partir do artigo de ID 1267.
4)  Se precisar de mais de 10 artigos pode usar o filtro "limit={qtd}". Nele você vai fornecer a quantidade de artigos que deseja retornar, por exemplo, "/articles/?offset=864&limit=200", vai trazer 200 artigos a aprtir do artigo de ID 864.
5)  Para testar as outras funções de POST, PUT e DELETE você deve acessar a nossa página de documentação. Ela pode ser acessada colocando o caminho "/docs" na raiz da nossa API. Nesta documentação você vai ter todas as informações sobre a API e também formas de testar ela.