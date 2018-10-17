from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cor(models.Model):
    descricao = models.CharField(max_length=120, unique=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descricao


class Montadora(models.Model):
    descricao = models.CharField(max_length=120, unique=True)
    sigla = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.sigla


class Item(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    # 99999999.99
    def __str__(self):
        return self.descricao


class Modelo(models.Model):
    montadora = models.ForeignKey(Montadora, on_delete=models.PROTECT)
    nome = models.CharField(max_length=200, unique=True, verbose_name="Nome completo do modelo do veículo")
    cores_disponiveis = models.ManyToManyField(Cor)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.montadora.sigla + " - " + self.nome


class ItemModelo(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    item_serie = models.BooleanField(default=False, verbose_name="Item de série")

    def __str__(self):
        return self.item.descricao + " | " + self.modelo.montadora.sigla + " - " + self.modelo.nome


class Carro(models.Model):
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    placa = models.CharField(max_length=20, unique=True)
    chassi = models.CharField(max_length=40, unique=True)
    km_rodado = models.PositiveIntegerField()
    itens_escolhidos = models.ManyToManyField(ItemModelo, verbose_name="Itens de série escolhidos no veículo",
                                              related_name='itens_carro')

    def __str__(self):
        return self.placa
