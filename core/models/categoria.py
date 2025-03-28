from django.db import models

from django.template.defaultfilters import upper

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f'({self.id}) {self.descricao.upper()}'
