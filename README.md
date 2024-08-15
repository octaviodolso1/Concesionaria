Este proyecto es un sistema web completo desarrollado en Django, diseñado para gestionar una concesionaria de autos. Incluye funcionalidades para la administración de autos, promociones, comentarios de usuarios, y la gestión de usuarios con diferentes roles de acceso.

Requisitos Previos
Antes de comenzar, asegúrate de tener instalados los siguientes requisitos en tu entorno:

    Python 3
    Django 4
    Un entorno virtual (recomendado para aislar dependencias)
    SQLite3 (base de datos utilizada en este proyecto)

Instrucciones de Instalación y Configuración

Descarga el archivo ZIP del proyecto y descomprímelo en tu equipo.
Crear y Activar un Entorno Virtual
Es recomendable utilizar un entorno virtual para evitar conflictos de dependencias. Sigue estos pasos para crearlo y activarlo:

Crear el entorno virtual:
python3 -m venv env

Activar el entorno virtual:
source env/bin/activate

Instalación de Dependencias
Con el entorno virtual activado, instala las dependencias necesarias ejecutando:
pip install -r requirements.txt

Configuración de la Base de Datos
Aplica las migraciones para configurar la base de datos:
python manage.py migrate

Crear un Superusuario
Crea un superusuario para acceder al panel de administración de Django:
python manage.py createsuperuser

Ejecutar el Servidor de Desarrollo
Inicia el servidor de desarrollo de Django con:
python manage.py runserver




Descripción del Proyecto

El sistema permite a los administradores gestionar autos, promociones y usuarios, mientras que los usuarios registrados pueden explorar la oferta de autos, realizar comentarios y ver promociones.
Estructura de Modelos

    Autos: Gestión completa de autos, incluyendo información detallada como marca, modelo, año, precio, estado y fotos.
    Marcas: Gestión de las marcas de autos disponibles.
    Modelos de Autos: Modelos específicos de autos, asociados a marcas.
    Clientes: Gestión de usuarios registrados que pueden comentar y ver autos.
    Categorías: Clasificación de autos en distintas categorías.
    Comentarios: Sistema de comentarios donde los usuarios pueden dejar opiniones sobre los autos.
    Promociones: Gestión de promociones especiales en autos.
    Usuarios: Diferentes niveles de acceso para administradores y usuarios comunes.

Funcionalidades Implementadas
Usuarios Administradores (Staff)

    Gestión de Autos: Capacidad para agregar, editar y eliminar autos.
    Gestión de Promociones: Creación, edición y eliminación de promociones asociadas a los autos.
    Gestión de Comentarios: Ver y eliminar comentarios de usuarios, con la capacidad de responder a estos.

Usuarios Comunes

    Explorar Autos: Navegación y visualización de detalles de los autos disponibles.
    Realizar Comentarios: Posibilidad de comentar sobre los autos, así como editar y eliminar sus propios comentarios.
    Ver Promociones: Visualización de autos que están actualmente en promoción.

Funcionalidades Adicionales

    Autenticación: Sistema de registro e inicio de sesión para usuarios.
    Carga de Imágenes: Los administradores pueden subir imágenes al agregar o editar autos.
    Internacionalización (i18n): El proyecto soporta múltiples idiomas, incluyendo inglés y español.
    Respuestas a Comentarios: Los administradores pueden responder a los comentarios de los usuarios.
