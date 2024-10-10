# Proyecto Django - Sitio Web Básico

Este proyecto consiste en una aplicación web básica desarrollada con Django, que incluye tres vistas principales: **Home**, **About**, y **Contact**. Se implementó un sistema de navegación utilizando Bootstrap para permitir una experiencia de usuario fluida entre las distintas páginas.

## Funcionalidades Principales

1. **Página Home**

   - Contiene un texto de bienvenida generado con Lorem Ipsum.
   - Incluye una barra de navegación para acceder a las páginas About y Contact.

2. **Página About**

   - Muestra información sobre el sitio web o la empresa (contenido ficticio utilizando Lorem Ipsum).
   - Navegación hacia las páginas Home y Contact.

3. **Página Contact**
   - Incluye un mini formulario de contacto con los siguientes campos:
     - Nombre
     - Correo electrónico
     - Mensaje
   - Permite al usuario enviar una solicitud de contacto (sin backend implementado).
   - Navegación hacia las páginas Home y About.

## Tecnologías Utilizadas

- **Django**: Framework principal utilizado para crear la aplicación web.
- **HTML**: Para estructurar las páginas web.
- **Bootstrap**: Framework CSS utilizado para estilizar las páginas y hacerlas responsivas.

## Estructura de Directorios

├── desafioGiado/
│ ├── **init**.py
│ ├── settings.py
│ ├── urls.py
│ ├── views.py
├── templates/
│ ├── home.html
│ ├── about.html
│ ├── contact.html
├── manage.py
└── requirements.txt
Instalación y Configuración

1. Clonar el repositorio
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>
1. Crear y activar el entorno virtual

python -m venv venv
source venv/bin/activate # En Windows: venv\Scripts\activate

1. Instalar las dependencias
   Ejecuta el siguiente comando para instalar las dependencias desde el archivo requirements.txt:

pip install -r requirements.txt

1. Migraciones de la base de datos
   Realiza las migraciones iniciales:

python manage.py migrate

1. Ejecutar la aplicación
   Inicia el servidor de desarrollo de Django:

python manage.py runserver
Accede a la aplicación desde tu navegador en http://127.0.0.1:8000.
