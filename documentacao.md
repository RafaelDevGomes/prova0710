# comandos do DJANGO
# usuario: root, senha: 12345
# C - Create (Criar): Adiciona ou insere novos dados no sistema. Exemplo: cadastrar um novo usuário em um site.
# R - Read (Ler): Consulta ou recupera os dados que já estão armazenados. Exemplo: pesquisar o perfil de um cliente ou ver a lista de produtos de uma loja.
# U - Update (Atualizar): Modifica informações que já existem sem precisar criar um novo registro. Exemplo: alterar o endereço de e-mail em um cadastro.          # D - Delete (Excluir): Remove um registro do sistema quando ele não é mais necessário. Exemplo: apagar uma foto ou cancelar uma conta de usuário.

1. ``pip install django`` -> instala o django no projeto.
2. ``django-admin startproject nome_do_projeto .(evita criar duas pastas iguais)`` -> criando um novo projeto em django. 
3. ``python manage.py runserver`` -> subindo o servidor.
4. ``python manage.py startapp nome_do_app`` -> criando um novo app.
5. ``python manage.py migrate`` -> aplicar "admin, auth, contenttypes e sessions." (CTRL + C -> pyt mata o servidor)
6. ``python manage.py createsuperuser`` -> criar um novo super usuário.
7. ``python manage.py changepassword nomedousuario`` -> altera a senha, caso esqueça.
8. ``python manage.py makemigrations`` -> cria/gera um novo pacote de migração (util para novo app e alteração do DB) 