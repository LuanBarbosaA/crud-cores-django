from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import TemplateView
import pdb
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.views.decorators.csrf import csrf_exempt


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


@csrf_exempt
def montadoras(request, opcao=None):
    if opcao == 1:
        opcao_mensagem = 'Montadora editada com sucesso!'
    else:
        if opcao == 2:
            opcao_mensagem = 'Montadora cadastrada com sucesso!'
        else:
            opcao_mensagem = None

    if request.method == 'POST':
        idmontadora = request.POST.get('id')
        temp = Montadora.objects.get(id=idmontadora)
        opcao_mensagem = 'Montadora ' + temp.sigla + ' - ' + temp.descricao + ' removida com sucesso!'
        temp.delete()
        opcao = True


    contexto = {
        "montadoras": Montadora.objects.all(),
        'opcao': opcao,
        'opcao_mensagem': opcao_mensagem
    }
    # dicionario
    # vetor com indices LITERAIS
    return render(request, '../templates/montadora.html', contexto)


def index(request):
    contexto = {
        ""
    }
    return render(request, '../templates/inicial.html')


def montadora_editar(request, id):
    montadora = get_object_or_404(Montadora, id=id)

    # APENAS UM
    if request.method == 'POST':
        montadora.descricao = request.POST.get('descricao')
        montadora.sigla = request.POST.get('sigla')
        montadora.save()
        return redirect('montadoralista', opcao=1)
    else:
        contexto = {
            'montadora': montadora
        }
    return render(request, '../templates/montadora_editar.html', contexto)


def montadora_cadastrar(request):
    form = MontadoraForm(request.POST or None)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('montadoralista', opcao=2)
    contexto = {
        "formMontadora": form,
    }
    return render(request, '../templates/montadora_cadastrar.html', contexto)


def cores(request, id = None, delete = None):
    #criar uma função para editar
    delete = request.POST.get('delete')
    if request.method == "GET" and id != None:
        cor = get_object_or_404(Cor, id=id)
        form = CorForm(initial={'descricao': cor.descricao, 'valor': cor.valor})
        contexto = {
            "formCores": form,
            "cores": Cor.objects.all(),
            "btn": "Editar",
            "opcao": 2
        }
        return render(request, '../templates/cores.html', contexto)
    elif request.method == "POST" and id != None:
        cor = get_object_or_404(Cor, id=id)
        cor.descricao = request.POST.get('descricao')
        cor.valor = request.POST.get('valor')
        cor.save()
        return redirect('cores')
    elif request.method == "POST" and delete:
        id = request.POST.get('id')
        temp = Cor.objects.get(id=id)
        temp.delete()
        return redirect('cores')
    else:
        form = CorForm(request.POST or None)
        if form.is_valid() and request.method == "POST":
            form.save()
            form = CorForm()
            #pdb.set_trace()
        contexto = {
            "formCores": form,
            "cores": Cor.objects.all(),
            "btn": "Salvar",
            "opcao": 1
        }
        return render(request, '../templates/cores.html', contexto)