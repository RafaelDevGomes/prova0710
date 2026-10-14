# prova0710

Sistema Escolar Django

📚 Sobre o projeto

O Sistema Escolar Django é um projeto desenvolvido em Python utilizando o framework Django, com o objetivo de estruturar um sistema de gerenciamento escolar.

O projeto possui três modelos principais: Professor, Aluno e Aula, responsáveis por representar os professores cadastrados, os alunos e as aulas vinculadas a ambos.

A aplicação utiliza SQLite como banco de dados e conta com uma área administrativa para visualizar e gerenciar os registros. Também possui uma estrutura inicial de páginas e rotas para navegação e cadastro.

🛠️ Tecnologias utilizadas

Python: linguagem de programação utilizada no desenvolvimento.

Django: framework responsável pela estrutura da aplicação web.

SQLite: banco de dados utilizado para armazenar as informações.

HTML e CSS: tecnologias destinadas à estruturação e à estilização das páginas.

Pillow: biblioteca utilizada para dar suporte ao gerenciamento de imagens pelo Django.

📂 Estrutura do projeto

manage.py: arquivo utilizado para executar comandos de gerenciamento do Django.

sistema/: contém as configurações gerais, as rotas principais e os arquivos de inicialização da aplicação.

portal/: contém os modelos, formulários, visualizações, rotas e configurações administrativas.

portal/models.py: define as estruturas de Professor, Aluno e Aula.

portal/forms.py: contém o formulário de cadastro de professores.

portal/views.py: define as visualizações e as respostas das páginas.

portal/admin.py: configura a exibição dos modelos no painel administrativo.

portal/templates/: diretório destinado aos templates HTML.

portal/static/: diretório destinado aos arquivos estáticos, como CSS.

portal/migrations/: contém os arquivos de migração do banco de dados.

db.sqlite3: arquivo do banco de dados SQLite.

🐛 Erros encontrados e correções realizadas

Durante o desenvolvimento, foram identificados problemas relacionados à configuração do Django, à importação de módulos, aos modelos e às visualizações. Os registros abaixo correspondem aos erros documentados nos comentários do próprio código.

1. Problemas no painel administrativo — portal/admin.py

Erro encontrado: mais da metade dos campos definidos em list_display não correspondia às variáveis existentes nos modelos.

Correção realizada: os campos de exibição foram ajustados para corresponder aos atributos definidos nas classes Professor, Aluno e Aula, permitindo configurar corretamente as informações exibidas no painel administrativo.

2. Problema de importação no formulário — portal/forms.py

Erro encontrado: havia um problema na importação do modelo Professor.

Correção realizada: foi utilizada a importação relativa from .models import Professor, permitindo que o formulário reconheça o modelo localizado no mesmo aplicativo.

3. Problema com o timezone — portal/models.py

Erro encontrado: as classes Professor, Aluno e Aula precisavam utilizar timezone, mas o recurso não havia sido importado.

Correção realizada: foi adicionada a importação from django.utils import timezone, possibilitando utilizar timezone.now como valor padrão para os campos de data e hora.

4. Problema com a instalação das dependências

Erro encontrado: o Django não estava instalado no ambiente do projeto.

Correção registrada: foi realizada a instalação de dependências por meio do pip, com menção ao comando pip install pillow.

5. Problema no campo de matrícula — portal/models.py

Erro encontrado: o campo de matrícula foi definido como IntegerField sem uma configuração adequada para o tamanho desejado.

Correção registrada: foi adicionada a configuração max_length=15 ao campo de matrícula.

6. Problema nas rotas e visualizações de cadastro — portal/urls.py e portal/views.py

Erro encontrado: havia um conflito na organização das rotas e das visualizações, e a função cadastro_view não estava devidamente configurada.

Correção realizada: foi criada a função cadastro_view em views.py e adicionada uma rota correspondente para acessar a página de cadastro.

7. Problema na configuração dos aplicativos — sistema/settings.py

Erro encontrado: o Django não estava reconhecendo os módulos portal e sistema como aplicativos instalados.

Correção registrada: os nomes portal e sistema foram adicionados à lista INSTALLED_APPS para que fossem reconhecidos pela configuração do projeto.

🎯 Objetivo do desenvolvimento

O desenvolvimento teve como objetivo estruturar uma aplicação web escolar, organizar os modelos de dados, configurar o painel administrativo e implementar as primeiras rotas de navegação e cadastro.

A identificação e a correção dos problemas documentados também fizeram parte do processo de aprendizagem, contribuindo para a compreensão da organização de projetos Django, da importação de módulos e da integração entre modelos, formulários, visualizações e rotas.
