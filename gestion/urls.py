from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns =(
    path('', views.index, name='index'),
    path('autos/', views.auto_list, name='auto_list'),
    path('autos/<int:pk>/', views.auto_detail, name='auto_detail'),
    path('autos/add/', views.auto_add, name='auto_add'),
    path('autos/<int:pk>/edit/', views.auto_edit, name='auto_edit'),
    path('autos/<int:pk>/delete/', views.auto_delete, name='auto_delete'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('logout/', views.logout_view, name='logout'),
    path('autos/<int:auto_id>/comentar/', views.agregar_comentario, name='agregar_comentario'),
    path('comentarios/<int:comentario_id>/editar/', views.editar_comentario, name='editar_comentario'),
    path('comentarios/<int:comentario_id>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
    path('comentarios/<int:comentario_id>/responder/', views.responder_comentario, name='responder_comentario'),
    path('promociones/', views.lista_promociones, name='lista_promociones'),
    path('promociones/gestion/', views.lista_promociones, name='gestion_promociones'),
    path('promociones/agregar/', views.agregar_promocion, name='agregar_promocion'),
    path('promociones/<int:pk>/editar/', views.editar_promocion, name='editar_promocion'),
    path('promociones/<int:pk>/eliminar/', views.eliminar_promocion, name='eliminar_promocion'),
)
