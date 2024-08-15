from django.contrib import admin
from .models import Marca, Categoria, Auto, ModeloAuto, Cliente, Comentario, Promocion, Accesorio, AccesorioPromocion

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Auto)
admin.site.register(ModeloAuto)
admin.site.register(Cliente)
admin.site.register(Comentario)
admin.site.register(Promocion)
admin.site.register(Accesorio)
admin.site.register(AccesorioPromocion)