from django.contrib import admin
from portal import models

# ERRO ENCONTRADO: Erro em admin/models.
# CORREÇÃO:        mais da metade do conteudo do list_display nao condizia com as variaveis settadas da classe de cada um.

@admin.register(models.Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','sobrenome','email','criacao_data','telefone','registro','disciplina','ativo','observacao','imagem')

@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'matricula', 'criacao_data', 'observacao', 'ativo', 'imagem')

@admin.register(models.Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('aluno_id', 'professor_id', 'horario', 'observacao', 'status',)
