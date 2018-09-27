from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import pdb;


# Create your views here.
def listar_cores(request):
    carros = Carro.objects.all()
    string = ''
    for carro in carros:
        string += "Placa: " + carro.placa + "<br>"
        string += "Modelo: " + carro.modelo.montadora.sigla + " - " + carro.modelo.nome + "<br>"
        string += "Valor do veículo: R$" + str(carro.modelo.valor) + "<br>"
        valor_total = carro.modelo.valor
        string += "Itens:<br>"
        for linha in carro.itens_escolhidos.all():
            string += " &emsp; - " + linha.item.descricao

            if (linha.item_serie):
                string += " [Item de série]"
            else:
                string += " [R$ " + str(linha.item.valor) + "]"
                valor_total += linha.item.valor
            string += "<br>"

        string += "Valor <b>TOTAL</b> veículo: R$" + str(valor_total) + "<br>"
        string += "<hr>"

    return HttpResponse(string)
