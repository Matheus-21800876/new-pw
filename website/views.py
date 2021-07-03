from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import Http404
from django.http.response import JsonResponse

from .forms import QuizzForm, ContatoForm, ComentarioForm
from .models import Quizz, Contato

'''API + SINGLE PAGE'''


def index(request):
    return render(request, "website/singlepage/index_new.html")


colorPalettes = [
    {
        "name": "Paleta - 0001",
        "autor": "Cristopher",
        "color01": "#EEEBDD",
        "color02": "#811515",
        "color03": "#630000",
        "color04": "#1B1717"
    },
    {
        "name": "Paleta - 0002",
        "autor": "Mike",
        "color01": "#151515",
        "color02": "#301B3F",
        "color03": "#3C415C",
        "color04": "#B4A5A5"
    },
    {
        "name": "Paleta - 0003",
        "autor": "Jason",
        "color01": "#8C0000",
        "color02": "#BD2000",
        "color03": "#FA1E0E",
        "color04": "#FFBE0F"
    },
    {
        "name": "Paleta - 0004",
        "autor": "Trevor",
        "color01": "#C5D7BD",
        "color02": "#9FB8AD",
        "color03": "#383E56",
        "color04": "#FB743E"
    },
    {
        "name": "Paleta - 0005",
        "autor": "Maria",
        "color01": "#E3FDFD",
        "color02": "#CBF1F5",
        "color03": "#A6E3E9",
        "color04": "#71C9CE"
    },
    {
        "name": "Paleta - 0006",
        "autor": "Trevor",
        "color01": "#2B2E4A",
        "color02": "#E84545",
        "color03": "#903749",
        "color04": "#53354A"
    },
    {
        "name": "Paleta - 0007",
        "autor": "Jon",
        "color01": "#212121",
        "color02": "#323232",
        "color03": "#0D7377",
        "color04": "#14FFEC"
    },
    {
        "name": "Paleta - 0008",
        "autor": "Dave",
        "color01": "#6FE7DD",
        "color02": "#3490DE",
        "color03": "#6639A6",
        "color04": "#521262"
    },
    {
        "name": "Paleta - 0009",
        "autor": "Liana",
        "color01": "#3EC1D3",
        "color02": "#F6F7D7",
        "color03": "#FF9A00",
        "color04": "#FF165D"
    },
    {
        "name": "Paleta - 0010",
        "autor": "Max",
        "color01": "#233142",
        "color02": "#455D7A",
        "color03": "#F95959",
        "color04": "#E3E3E3"
    },
    {
        "name": "Paleta - 0011",
        "autor": "Alex",
        "color01": "#303841",
        "color02": "#3A4750",
        "color03": "#D72323",
        "color04": "#EEEEEE"
    },
    {
        "name": "Paleta - 0012",
        "autor": "Lucas",
        "color01": "#F3F4ED",
        "color02": "#536162",
        "color03": "#424642",
        "color04": "#C06014"
    }

]


def section(request, num):
    if 1 <= num <= 3:
        return JsonResponse({"paletas": colorPalettes})
    else:
        raise Http404("No such section")


'''END'''


'''def home_page_view(request):
    return render(request, 'website/index.html')'''


def teoria_page_view(request):
    return render(request, 'website/about_colors.html')


def about_site_page_view(request):
    return render(request, 'website/about_site.html')


def form_page_view(request):
    return render(request, 'website/form.html')


def new_quizz_view(request):
    form = QuizzForm(request.POST or None)
    if form.is_valid():
        form.save()
        nota = grade(form)
        return render(request, 'website/show_quizz.html', {'nota': nota})

    context = {'form': form}

    return render(request, 'website/quizz.html', context)


def grade(form):
    acertos = 0

    if form.cleaned_data['pergunta1'] == 'Branco' or form.cleaned_data['pergunta1'] == 'branco':
        acertos += 1

    if form.cleaned_data['pergunta2'] == 'Preto' or form.cleaned_data['pergunta2'] == 'preto':
        acertos += 1

    if form.cleaned_data['pergunta3'] == '3':
        acertos += 1

    if form.cleaned_data['pergunta4'] == '2':
        acertos += 1

    if form.cleaned_data['pergunta5'] == '2':
        acertos += 1

    if form.cleaned_data['pergunta6'] == '4':
        acertos += 1

    if form.cleaned_data['pergunta7'] == 4:
        acertos += 1

    if form.cleaned_data['pergunta8'] == '1':
        acertos += 1

    if form.cleaned_data['pergunta9'] == '2':
        acertos += 1

    return acertos


def show_quizz_page_view(request):
    context = {'quizzs': Quizz.objects.all()}
    return render(request, 'website/show_quizz.html', context)


def new_contato_view(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:show_contato'))

    context = {'form': form}

    return render(request, 'website/contatos.html', context)


def show_contato_page_view(request):
    context = {'contatos': Contato.objects.all()}
    return render(request, 'website/show_contato.html', context)


def edita_contato_view(request, contato_id):
    contato = Contato.objects.get(id=contato_id)
    form = ContatoForm(request.POST or None, instance=contato)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:show_contato'))

    context = {'form': form, 'contato_id': contato_id}
    return render(request, 'website/edita_contato.html', context)


def apaga_contato_view(request, contato_id):
    Contato.objects.get(id=contato_id).delete()
    return HttpResponseRedirect(reverse('website:show_contato'))


def new_comentario_view(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:index'))

    context = {'form': form}

    return render(request, 'website/comentarios.html', context)


def color_page_001(request):
    return render(request, 'website/color-pages/color-page-001.html')


def color_page_002(request):
    return render(request, 'website/color-pages/color-page-002.html')


'''def color_page_003(request):
    return render(request, 'website/color-pages/color-page-003.html')'''


def color_page_004(request):
    return render(request, 'website/color-pages/color-page-004.html')


'''def color_page_005(request):
    return render(request, 'website/color-pages/color-page-005.html')'''


'''def color_page_006(request):
    return render(request, 'website/color-pages/color-page-006.html')'''


'''def color_page_007(request):
    return render(request, 'website/color-pages/color-page-007.html')'''


def color_page_008(request):
    return render(request, 'website/color-pages/color-page-008.html')


'''def color_page_009(request):
    return render(request, 'website/color-pages/color-page-009.html')'''


def color_page_010(request):
    return render(request, 'website/color-pages/color-page-010.html')


'''def color_page_011(request):
    return render(request, 'website/color-pages/color-page-011.html')'''


'''def color_page_012(request):
    return render(request, 'website/color-pages/color-page-012.html')'''
