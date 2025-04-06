from django.shortcuts import render, redirect
from .models import Defeito
from django.db.models import Q
from django.core.paginator import Paginator


def base_conhecimento (request):
    if request.method == 'GET':
        return render(request, 'base_conhecimento.html')
    
    if request.method == "POST":
        maquina = request.POST.get("maquina","").strip()
        descricao = request.POST.get("descricao","").strip()
        solucao = request.POST.get("solucao","").strip()
        causa_possivel = request.POST.get('causa_possivel')
        
        if maquina and descricao and solucao:
            Defeito.objects.create(maquina=maquina, descricao=descricao, solucao=solucao,causa_possivel=causa_possivel)
            
    defeitos = Defeito.objects.all() 
    return render(request, "base_conhecimento.html", {"defeitos": defeitos})
    
def buscar_defeito(request):
    query = request.GET.get('q', '').strip()
    resultados = Defeito.objects.none()
    page = request.GET.get('page', 1)

    if query:
        # Busca em múltiplos campos
        resultados = Defeito.objects.filter(
            Q(maquina__icontains=query) | 
            Q(descricao__icontains=query) |
            Q(solucao__icontains=query)
        ).distinct()
    paginator = Paginator(resultados, 10)  # 10 itens por página
    resultados_paginados = paginator.get_page(page)
    
    return render(request, "base_conhecimento.html", {'resultados': resultados_paginados, 'query': query})