from django.shortcuts import render, redirect, get_object_or_404
from app.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.forms import *
from django.core.mail import mail_admins


def home(request):
    objetos = OA.objects.all()
    return render(request, 'accounts/index.html', {'objetos': objetos})


def pesquisa(request):
    pesq = FormPesquisa()
    q = ''
    results = []
    if 'q' in request.GET:
        pesq = FormPesquisa(request.GET)
        if pesq.is_valid():
            q = pesq.cleaned_data['q']
            results = OA.objects.filter(titulo__contains=q) or OA.objects.filter(tags__nametag__contains=q)
    return render(request, 'accounts/pesquisa.html', {'pesq': pesq, 'q': q, 'results': results})


def view(request, pk):
    data = {'db': OA.objects.get(pk=pk)}
    return render(request, 'accounts/view.html', data)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Conta foi criada para ' + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Usuário ou Senha Incorretos')
        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def fav(request, pk):
    OAFav = get_object_or_404(OA, pk=pk)
    if OAFav.favoritos.filter(id=request.user.id).exists():
        OAFav.favoritos.remove(request.user)
    else:
        OAFav.favoritos.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def favoritos(request):
    new = OA.objects.filter(favoritos=request.user)
    return render(request, 'accounts/favoritos.html', {'new': new})


def report(request, pk):
    resposta = mail_admins('Reporte OA' + pk, 'O objeto de endereço: /view/' + pk + '/  Foi reportado.',
                           fail_silently=False, connection=None, html_message=None)
    messages.info(request, 'Reporte de OA: o objeto foi reportado.')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])