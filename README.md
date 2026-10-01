ExaPets - Sprint 1 

Instrucciones para levantar el entorno local

Sigue estos pasos para clonar y ejecutar el proyecto sin conflictos:

Clona el repositorio y entra a la carpeta:

git clone https://github.com/Isibv/Exapets-cc4401.git
cd exapets_project


Crea y activa el entorno virtual:

Windows: python -m venv venv y luego venv\Scripts\activate

Mac/Linux: python3 -m venv venv y luego source venv/bin/activate

Instala las dependencias:

pip install -r requirements.txt


Configura tus variables de entorno:

Crea un archivo llamado .env en la raíz del proyecto (junto a manage.py).

Solicita la SECRET_KEY a un administrador del repositorio por interno y pégala así:

SECRET_KEY=la_clave_que_te_envien
DEBUG=True


Aplica las migraciones iniciales:
¡Importante! Esto creará tu propia base de datos db.sqlite3 local.

python manage.py migrate


(Opcional: Crea tu usuario administrador local con python manage.py createsuperuser)

Inicia el servidor:

python manage.py runserver
