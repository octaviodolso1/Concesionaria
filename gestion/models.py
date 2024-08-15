from django.db import models
from django.contrib.auth.models import User

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Auto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    anio = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    kilometraje = models.IntegerField()
    estado = models.CharField(max_length=10, choices=[('Nuevo', 'Nuevo'), ('Usado', 'Usado')])
    imagen = models.ImageField(upload_to='autos/', null=True, blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"

class ModeloAuto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marca.nombre} {self.nombre}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Comentario(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.cliente.username} sobre {self.auto}"

class Respuesta(models.Model):
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    respuesta = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Respuesta de {self.autor.username} al comentario {self.comentario.id}"


class Promocion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, default=1)  # Ajusta el valor predeterminado según corresponda
    precio_promocional = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return f"{self.nombre} - {self.auto.modelo} ({self.fecha_inicio.date()} a {self.fecha_fin.date()})"
class AutoPromocion(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, null=True)
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.auto} - {self.promocion}"

class Accesorio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
    
class AccesorioPromocion(models.Model):
    accesorio = models.ForeignKey(Accesorio, on_delete=models.CASCADE)
    promocion = models.ForeignKey('Promocion', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.accesorio} - {self.promocion}"
