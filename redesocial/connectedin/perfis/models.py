from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    nome = models.CharField(max_length = 255 , null = False)
    telefone = models.CharField(max_length = 15 , null = False)
    nome_empresa = models.CharField(max_length = 255 , null = False)
    contatos = models.ManyToManyField('self')
    usuarios = models.OneToOneField(User, on_delete=models.PROTECT , related_name = "perfil+")
    
    @property
    def email(self):
        return self.usuarios.email

    def convidar(self , perfil_convidado):
        Convite(solicitante = self, convidado = perfil_convidado).save()

class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, on_delete=models.PROTECT , related_name = 'convites feitos+')
    convidado = models.ForeignKey(Perfil, on_delete=models.PROTECT , related_name = 'convites recebidos+')

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.delete(_)
