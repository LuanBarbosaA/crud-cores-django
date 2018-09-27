from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import TemplateView
import pdb;
from django.shortcuts import render


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


def sobre_carros(request):
    contexto = {
        "nome_aula": "AULA DE TEMPLATESSSSSSSSSS",
        "data_atual": "27/09/2018",
        "carros": Carro.objects.all()
    }
    # dicionario
    # vetor com indices LITERAIS
    return render(request, '../templates/sobre.html', contexto)
