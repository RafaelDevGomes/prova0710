from django.db import models
from django.utils import timezone
# ERRO ENCONTRADO: as classes de professor, aluno e aula não estavam conseguindo usar o timezone ja que ele não tinha sido definido.
# CORREÇÃO: Nós importamos a timezone para o models.py.

# ERRO ENCONTRADO: Django não estava instalado no projeto.
# CORREÇÃO:        Instalar o django no projeto(utilizamos o pip install pillow).

# ERRO ENCONTRADO: Matricula com integerfield() vazio.
# CORREÇÃO:        Adicionar um max_lenght.


class Professor(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    criacao_data = models.DateTimeField(default=timezone.now)
    telefone = models.CharField(max_length=15)
    registro = models.CharField(max_length=10)
    disciplina = models.CharField(max_length=30)
    ativo = models.BooleanField(default=True)
    observacao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='img/%Y/%m', blank=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    matricula = models.IntegerField(max_length=15)
    criacao_data = models.DateTimeField(default=timezone.now)
    observacao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='img/%Y/%m', blank=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Aula(models.Model):
    aluno_id = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE)
    horario = models.DateTimeField(default=timezone.now)
    observacao = models.TextField(blank=True)
    status = models.CharField(
        default='A',
        max_length=1,
        choices=(
            ('A', 'Agendada'),
            ('X', 'Cancelada'),
            ('C', 'Confirmada'),
            ('R', 'Realizada')
        )
    )

    def __str__(self):
        return f'Aula {self.status} com sucesso.'
