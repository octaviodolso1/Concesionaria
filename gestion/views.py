from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegistroForm, AutoForm, ComentarioForm, RespuestaForm, PromocionForm
from .models import Auto, Comentario, Respuesta, Promocion
from django.utils import timezone


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = False  
            user.save()
            login(request, user)  
            return redirect('index')  
        form = RegistroForm()
    return render(request, 'gestion/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  
    else:
        form = AuthenticationForm()
    return render(request, 'gestion/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def index(request):
    return render(request, 'gestion/index.html')



@login_required
def perfil_usuario(request):
    return render(request, 'gestion/perfil_usuario.html')

@user_passes_test(lambda u: u.is_staff)
def auto_add(request):
    if request.method == 'POST':
        form = AutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('auto_list')
    else:
        form = AutoForm()
    return render(request, 'gestion/auto_form.html', {'form': form})


@user_passes_test(lambda u: u.is_staff)
def auto_edit(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    if request.method == 'POST':
        form = AutoForm(request.POST, request.FILES, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('auto_detail', pk=auto.pk)
    else:
        form = AutoForm(instance=auto)
    return render(request, 'gestion/auto_form.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def auto_delete(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    if request.method == 'POST':
        auto.delete()
        return redirect('auto_list')
    return render(request, 'gestion/auto_confirm_delete.html', {'auto': auto})

def auto_list(request):
    autos = Auto.objects.all()
    promociones = Promocion.objects.filter(fecha_inicio__lte=timezone.now(), fecha_fin__gte=timezone.now())
    promociones_dict = {promocion.auto.id: promocion for promocion in promociones}
    
    autos_con_promociones = []
    for auto in autos:
        auto_info = {
            'auto': auto,
            'promocion': promociones_dict.get(auto.id) 
        }
        autos_con_promociones.append(auto_info)
    
    return render(request, 'gestion/auto_list.html', {'autos_con_promociones': autos_con_promociones})

def auto_detail(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    promocion = Promocion.objects.filter(auto=auto, fecha_inicio__lte=timezone.now(), fecha_fin__gte=timezone.now()).first()
    return render(request, 'gestion/auto_detail.html', {'auto': auto, 'promocion': promocion})


@login_required
def agregar_comentario(request, auto_id):
    auto = get_object_or_404(Auto, pk=auto_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.auto = auto  
            comentario.cliente = request.user 
            comentario.save()
            return redirect('auto_detail', pk=auto.pk)
    else:
        form = ComentarioForm()
    return render(request, 'gestion/agregar_comentario.html', {'form': form, 'auto': auto})

@login_required
def editar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    
  
    if comentario.cliente != request.user:
        return redirect('auto_detail', pk=comentario.auto.pk) 

    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('auto_detail', pk=comentario.auto.pk)
    else:
        form = ComentarioForm(instance=comentario)
    
    return render(request, 'gestion/editar_comentario.html', {'form': form, 'auto': comentario.auto})

@login_required
def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    auto = comentario.auto

    
    if request.user != comentario.cliente and not request.user.is_staff:
        return redirect('auto_detail', pk=auto.pk) 

    if request.method == 'POST':
        comentario.delete()
        return redirect('auto_detail', pk=auto.pk)
    
    return render(request, 'gestion/eliminar_comentario.html', {'comentario': comentario, 'auto': auto})

@user_passes_test(lambda u: u.is_staff)
def responder_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.comentario = comentario
            respuesta.autor = request.user
            respuesta.save()
            return redirect('auto_detail', pk=comentario.auto.pk)
    else:
        form = RespuestaForm()
    return render(request, 'gestion/responder_comentario.html', {'form': form, 'comentario': comentario})


@user_passes_test(lambda u: u.is_staff)
def agregar_promocion(request):
    if request.method == 'POST':
        form = PromocionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_promociones')
    else:
        form = PromocionForm()
    return render(request, 'gestion/agregar_promocion.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def editar_promocion(request, pk):
    promocion = get_object_or_404(Promocion, pk=pk)
    if request.method == 'POST':
        form = PromocionForm(request.POST, instance=promocion)
        if form.is_valid():
            form.save()
            return redirect('lista_promociones')
    else:
        form = PromocionForm(instance=promocion)
    return render(request, 'gestion/editar_promocion.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def eliminar_promocion(request, pk):
    promocion = get_object_or_404(Promocion, pk=pk)
    if request.method == 'POST':
        promocion.delete()
        return redirect('lista_promociones')
    return render(request, 'gestion/eliminar_promocion.html', {'promocion': promocion})

def lista_promociones(request):
    promociones = Promocion.objects.all()
    return render(request, 'gestion/lista_promociones.html', {'promociones': promociones})

