from django.shortcuts import render


def uno(request):
    return render(request, 'uno.html', {})
def dos(request):
    return render(request, 'dos.html', {})
def gijonGastos(request):
    return render(request, 'gijonGastos.html', {})
def cuatrocuatro(request):
    return render(request, 'cuatrocuatro.html', {})
